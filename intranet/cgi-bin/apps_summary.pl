#!/usr/bin/perl

print "Content-type: text/html\r\n\r\n";

my $contentType = "html";

my $isInList = 0;

our $vhosts;
our $databases;

open(FP, '/home/intranet/google-apps.html');
my $content = join("", <FP>);

my $html = do {local $/;<DATA>};
$html=~s/%CONTENT%/$content\n$1/;
print $html;

__DATA__
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-us" lang="en-us">
<head>
<title>summary of vhosts.pl</title>
<style type="text/css" media="all">
	@import url('https://secure.mysociety.org/intranet/pub/TWiki/PatternSkin/layout.css');
	@import url('https://secure.mysociety.org/intranet/pub/TWiki/PatternSkin/style.css');
	@import url('https://secure.mysociety.org/intranet/pub/TWiki/PatternSkin/colors.css');
	@import url("https://secure.mysociety.org/intranet/pub/TWiki/PatternSkin/print.css");
    table#db-table tr:nth-child(even){background-color: #ddd;}
    table#db-table table,th,td{padding:5px;border:1px solid black;vertical-align:top;}
    table#db-table th{text-align:left;}
    table{border-collapse:collapse; font-size:100%;}
	.vhosts-col{float:left; width:45%;}
	body{margin-top:10px;}
</style>
</head>
<body class="patternViewPage">
<div id="patternPage">
<div id="patternMainContents">
<div id="patternContent">
<div id="patternTopic">
%CONTENT%
</div>
</div>
</div>
</div>
</body>
</html>
