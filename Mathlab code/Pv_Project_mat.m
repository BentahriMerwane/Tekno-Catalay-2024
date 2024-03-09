%PV project%

l=50.29 ;% local Latitude
Lst= 15 ; % standard longitude for the time zone
Lloc = 5.56 ; % local longitude
Ea = 1366; %extraterrestrial irradiance
sunalt = zeros(365,1440); % altitude sun angle
sunazy = zeros(365,1440); % Azymuth sun angle
anginc = zeros(365,1440); % angle of incidence
tilt = 35 ;  % tilt angle
modazy = 90; % module azymuth angle
di = irradpv{:,3} ; % Diffusive irradiance
globi = irradpv{:,2} ; % global irradiance
DHI = zeros(365,1440); % diffusive matrice data
GHI = zeros(365,1440); % global mat data
DNI = zeros(365,1440); % normal mat data
MinirradSf = zeros(365,1440); % irradiance on Pannel each minute
x=0;
%for s = 1:50
 %   tilt = s-1;
 for i = 1:365
        B = 2*pi*(i-81)/365; % Day number coefficient
        EOT = 9.87*sin(2*B) - 7.53*cos(B) -1.5*sin(B); % Equation of Time
        delta = 23.45*sin(2*pi*(i+284)/365) ; % declination angle
        for j = 1:1440
            solartime= (j-1)/60 + (4*(Lst-Lloc)+EOT)/60;
            h = (solartime-12)*15;
            Sunalt = asind(cosd(l)*cosd(h)*cosd(delta) + sind(l)*sind(delta)); % sun altitude angle
            if Sunalt < 0
                sunalt(i,j) = 0;
            else
                sunalt(i,j) = Sunalt;
            end
            if h<0
                sunazy(i,j) = -1*acosd((sind(sunalt(i,j))*sind(l)-sind(delta))/(cosd(sunalt(i,j))*cosd(l)));
            end
            if h>0
                sunazy(i,j) = acosd((sind(sunalt(i,j))*sind(l)-sind(delta))/(cosd(sunalt(i,j))*cosd(l)));
            end
            Anginc = acosd(cosd(sunalt(i,j))*cosd(sunazy(i,j)-modazy)*sind(tilt)+sind(sunalt(i,j))*cosd(tilt));
            if Anginc > 89
                anginc(i,j) = 90;
            else
                anginc(i,j) = Anginc;
            end
%             DHI(i,j) = 200;            
%             DNI(i,j) = 1000;
%             GHI(i,j) = DNI(i,j)*cosd(90 - sunalt(i,j)) + DHI(i,j);

            
            DHI(i,j) = di((i-1)*1440+j);
            GHI(i,j) = globi((i-1)*1440+j);
            a=DHI(i,j);
            b=GHI(i,j);
           
            if (a > b) || (sunalt(i,j) <0)

               DNI(i,j) = 0;
               GHI(i,j) = DHI(i,j);
            
            else 
                DNI(i,j) = (GHI(i,j)-DHI(i,j))/cosd(90 - Sunalt);
            end
            if Anginc > 89
                MinirradSf(i,j) = DHI(i,j) *((1+cosd(tilt))/2);
            else
                MinirradSf(i,j) = DHI(i,j)*(DNI(i,j)/Ea*cosd(anginc(i,j))+(1-DNI(i,j)/Ea)*(1+cosd(tilt))/2*(1+sqrt((DNI(i,j)*cosd(90-sunalt(i,j)))/GHI(i,j))*(sind(tilt/2))^3));
            end
            if GHI(i,j) == 0
                MinirradSf(i,j) = 0;
            end
            
        end
  %  end
%x(s) = sum(sum(Minirrad));
plot(Minirrad(1,:))
%hold on
%plot(anginc(210,:))
end
%plot(x)
