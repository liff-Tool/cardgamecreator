<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>画像オーバーレイ</title>
<style>
    #container {
        position: relative;
        display: inline-block;
    }
    #text-overlay {
        position: absolute;
        top: 10px;
        left: 10px;
        color: white;
        font-size: 20px;
        background-color: rgba(0, 0, 0, 0.5);
        padding: 10px;
    }
</style>
</head>
<body>

<div>
    <label for="text-input">テキスト：</label>
    <input type="text" id="text-input" name="text-input" value="サンプルテキスト">
</div>

<div>
    <label for="overlay-input">オーバーレイ画像：</label>
    <input type="file" id="overlay-input" name="overlay-input">
</div>

<button onclick="overlayImage()">オーバーレイ追加</button>

<div id="container">
    <img id="base-image" src="path_to_your_image.jpg" alt="元画像">
    <div id="text-overlay">サンプルテキスト</div>
</div>

<script>
    // オーバーレイ画像を追加する関数
    function overlayImage() {
        var container = document.getElementById('container');
        var overlayImageInput = document.getElementById('overlay-input');
        var overlayText = document.getElementById('text-input').value;

        var overlayImage = document.createElement('img');
        overlayImage.src = URL.createObjectURL(overlayImageInput.files[0]);
        overlayImage.style.position = 'absolute';
        overlayImage.style.top = '50px'; // 必要に応じて位置を調整してください
        overlayImage.style.left = '50px'; // 必要に応じて位置を調整してください
        container.appendChild(overlayImage);

        var textOverlay = document.getElementById('text-overlay');
        textOverlay.innerText = overlayText;
    }
</script>

</body>
</html>