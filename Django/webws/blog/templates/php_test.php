{% csrf_token %}
<?php
  $rid = $_POST['rid'];
  $r1 = $_POST['r1'];
  $c1 = $_POST['c1'];
  $tt = $_PSOT['tt'];
?>

<!doctype html>
<html lang="ko">
  <head>
  <meta charset="utf-8">
    <title>HTML</title>
    <style>
      * {
        font-size: 16px;
        font-family: Consolas, sans-serif;
      }
    </style>
  </head>
  <body>
    <p><?php echo $_POST['rid']?></p>
    <p>당신은 <?php echo $color ?>직이시군요</p>
    <p>저도 <?php echo $sport ?>을 좋아한답니다</p>
    <p>자기소개서 잘 읽었습니다.</p>
    <p><?php echo $sport ?></p>
  </body>
</html>