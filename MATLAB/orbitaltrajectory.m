% function orbitaltrajectory()
%
%This is a (developing) function by Alexander Winkles that will 
% model the orbit of a satellite around Earth.
%
% Call as [a,e,i,o,w,n] = orbitaltrajectory()
%
% Inputs
% r : the initial position vector
% v : the initial velocity vector
% t : time since Jan 1, 2000
%
% Outputs
%
%

function [a,emag,i,Omega,argp,nu] = orbitaltrajectory(rvec,vvec)

format long

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Constants utilized throughout the function        %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

mu = 398.6004418e12; % planetary gravitational constant (m^3 / s^2)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Conversion of state vectors into orbital elements %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

rmag = sqrt(dot(rvec,rvec)); % position magnitude
vmag = sqrt(dot(vvec,vvec)); % velocity magnitude

rhat = rvec/rmag; % position unit vector
vhat = vvec/vmag; % velocity unit vector

hvec = cross(rvec,vvec); % angular momentum vector
hmag = sqrt(dot(hvec,hvec)); % angular momentum magnitude
hhat = hvec/hmag; % angular momentum unit vector

nvec = cross([0 0 1],hvec); % node vector
nmag = sqrt(dot(nvec,nvec)); % node magnitude

evec = ((vmag^2 - mu/rmag)*rvec - dot(rvec,vvec)*vvec)/mu; % eccentricity vector
emag = sqrt(dot(evec,evec)); % eccentricity magnitude

E = vmag^2/2 - mu/rmag; % specific mechanical energy

if emag ~= 1
    a = -mu/(2*E); % semi-major axis
    p = a*(1-emag^2);
else
    p = hmag^2/mu;
    a = Inf;
end;

i = acos(hvec(3)/hmag)*(180/pi); % inclination in degrees

Omega = acos(nvec(1)/nmag)*(180/pi); % longitude of ascending node in degrees

if nvec(2) < 0
    Omega = 360 - Omega; 
end;

argp = acos(dot(nvec,evec)/(nmag*emag))*(180/pi); % argument of periapsis in degrees

if evec(3) < 0
    argp = 360 - argp;
end

nu = acos(dot(evec,rvec)/(emag*rmag))*(180/pi); % true anomoly in degrees

if dot(rvec,vvec) < 0
    nu = 360 - nu;
end;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Plots the resulting orbit for a given time frame  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

