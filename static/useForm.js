document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.getElementById("upload-form");
    const imageUpload = document.getElementById("image-upload");
    const uploadedImage = document.getElementById("uploaded-image");
    const imagePreview = document.getElementById("image-preview");
    const convertButton = document.getElementById("convert-button");

    // Function to handle image preview
    function handleImagePreview() {
        const file = imageUpload.files[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                // Create an image element for resizing
                const img = new Image();
                img.src = e.target.result;

                img.onload = function () {
                    const maxWidth = imagePreview.clientWidth;
                    const maxHeight = imagePreview.clientHeight;

                    const widthRatio = maxWidth / img.width;
                    const heightRatio = maxHeight / img.height;

                    // Use the smaller of the two ratios to fit the image
                    const resizeRatio = Math.min(widthRatio, heightRatio);

                    // Set the resized image dimensions
                    img.width = img.width * resizeRatio;
                    img.height = img.height * resizeRatio;

                    // Display the resized image
                    uploadedImage.src = img.src;
                    imagePreview.style.display = "block";
                };
            };

            reader.readAsDataURL(file);
        }
    }

    // Listen for changes in the file input
    imageUpload.addEventListener("change", handleImagePreview);

    // Handle form submission
    uploadForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = new FormData(this);
        const response = await fetch("/image-to-speech", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const data = await response.json();
            const audioPlayer = document.getElementById("audio-player");
            audioPlayer.src = data.audio_path;
            audioPlayer.play();
        } else {
            console.error("Error processing the image.");
        }
    });
});