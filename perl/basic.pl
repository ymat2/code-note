use strict;
use warnings;

print("##### STDOUT #####\n");
print("Hello World\n");
print("Hello " , "World" . "\n");

print("##### IF-ELSE #####\n");
if (1) {
    print("Hello\n");
} else {
    print("Bye\n");
}

my $i = 12;
if ($i > 10) {
    print("i>10\n");
} elsif ($i > 8) {
    print("10>=i>8\n");
} else {
    print("8>=i\n");
}


print("##### AND/OR #####\n");
if (1 && 0) { print("1 && 0\n")};
if (1 || 0) { print("1 || 0\n")};
if (2 && !0) { print("2 && !0\n")};
if ('1' || !'0') { print("'1' || !'0'\n")};


print("##### ARRAY #####\n");
my @chrs = ("hoge", "fuga", "piyo");
print(join(", ", @chrs) . "\n");
print($chrs[0] . "\n");
print($chrs[-1] . "\n");

my @chrs2 = ("hoge", "fuga", "piyo", 1, -2, 3.14);
print($chrs2[0] . "\n");
print($chrs2[-1] . "\n");

pop @chrs;              # 末尾の要素を削除
push @chrs, "tail";     # 末尾に要素を追加

shift @chrs;            # 先頭の要素を削除
unshift @chrs, "head";  # 先頭に要素を追加
print(@chrs . "\n");

my $l = scalar @chrs2;
print($l . "\n");

print("##### HASH #####\n");
my %dict = ("a" => "hoge", "b" => "fuga", "c" => "piyo");
print($dict{"a"} . "\n");

$dict{"d"} = "koke";   # 要素を更新
delete $dict{"c"};     # 要素を削除
print($dict{"d"}. "\n");

my %dict2 = (
  "a" => [1, 2, 3],
  "b" => ["hoge", "fuga", "piyo"]
);
print($dict2{"a"}[1] . "\n");

foreach my $key (keys %dict) {
    my $value = $dict{$key};
    print("key = $key\n");
    print("value = $value\n");
}


print("##### LOOPING #####\n");
for my $i (1..5) {
    print("Hello world\n");
}

@chrs = ("hoge", "fuga", "piyo");
for my $i (@chrs) {
    print("$i\n");
}

@chrs = ("hoge", "fuga", "piyo");
for (@chrs) {
    print("$_\n");
}

my $i = 0;

while ($i < 5) {
  print($i . " is less than 5." . "\n");
  $i++;
}

until ($i > 7) {
  print($i . " is less than 7." . "\n");
  $i++;
}


print("##### FUNCTION #####\n");
sub cube {
    my $i = shift;
    return $i**3;
}
print(cube(3) . "\n")

print(&calcAverage(10, 8) . "\n");
&calcAverage(5, 17);

sub calcAverage{
  my $ave;
  $ave = ($_[0] + $_[1]) / 2;
  return $ave;
}
