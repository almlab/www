<?php
    $now = shell_exec("date");
    $git_status = shell_exec("git status 2>&1");
    $git_pull = shell_exec("git pull 2>&1");
    $make_result = shell_exec("make 2>&1");
    print_r($now);
    print_r("<br><br>");
    print_r(nl2br($git_status));
    print_r("<br><br>");
    print_r(nl2br($git_pull));
    print_r("<br><br>");
    print_r(nl2br($make_result));
?>
