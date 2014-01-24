# $Id: Event.pm,v 1.1 2006-08-18 12:15:26 francis Exp $
package IRC::Event;

AUTOLOAD {
   return unless defined $AUTOLOAD;
   my $name = $AUTOLOAD;
   $name =~ s/.*:://;
   return if $name eq 'DESTROY';
   if($name && ref $_[0] && $_[0]->{server} && $_[0]->{channel}) {
      $_[0]->{server}->$name($_[0]->{channel}, @_[1..$#_]);
   }
}

sub new {
   my($class,$client) = (shift,shift);
   my $self = bless { }, $class;
   %$self = @_;
   $self->{server} = $client;
   return $self;
}

1;
