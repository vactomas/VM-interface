# Copyright (C) 2014 SUSE Linux GmbH
# Copyright Red Hat
#
# This file is part of openqa-app-testing.
#
# openqa-app-testing is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 2 of
# the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
use strict;
use testapi;
use autotest;
use needle;
use File::Basename;
 
# distribution-specific implementations of expected methods
#my $distri = testapi::get_var("CASEDIR") . '/lib/fedoradistribution.pm';
#require $distri;
#testapi::set_distribution(fedoradistribution->new());
 
## UTILITY SUBROUTINES - unregister needles

# Stolen from openSUSE.
#sub unregister_needle_tags($) {
#    my $tag = shift;
#    my @a = @{needle::tags($tag)};
#    for my $n (@a) { $n->unregister(); }
#}

## Functions for laoding tests

sub load_tests() {
  autotest::loadtest "tests/boot.pm";
}

## Load tests

load_tests;

1;
