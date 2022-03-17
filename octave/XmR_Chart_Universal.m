%====================================================================
% XmR Charting with Octave - 1 Column Input Data From CSV File
%====================================================================
% Based on the information on: X Bar - Moving-Range Charts
%
%    "Understanding Variation - The Key To Managing Chaos"
%    Donald J. Wheeler, 1993, SPC Press, 1993
%
% Also see: Wheeler, D J,
%    https://www.qualitydigest.com/inside/quality-insider-column/individual-charts-done-right-and-wrong.html
%
% Total freeware, but remember this was: Written by an infinite number of Monkeys,
% in an infinite amount of time, SO BEWARE as Monkeys have no idea how to type.
%====================================================================
clear; clc;
pkg load statistics

%=====[ User Input ]=================================================
filename = "TestData.csv";

title_s = "XmR Control Chart with Octave"; % Main Title

measure_s = "Measureand";       % Y Axis Data Title

nBins = 10;                 % Number of Histogram bins to plot

%=====[ Calculation ]================================================
xyData = csvread(filename);

yMean = mean(xyData(:,1)); # Find mean of first column
meanData(1:length(xyData)) = yMean;

R = movingranges(xyData);
tempR = R;
tempR(1) = [];     %First value of ranges is NaN, remove it so mean will calculate properly.
mR = mean(tempR);
mRv(1:length(xyData)) = mR;
UCLr = mRv .* 3.27;

UNPL = yMean + (2.66 .* mRv);
LNPL = yMean - (2.66 .* mRv);

%=====[ Plotting ]===================================================

%===== Individual Values Chart =====
figure(1);
subplot (2, 1, 1, "align");
plot(xyData);
hold on;
plot(meanData, 'g--');

plot(UNPL, 'r--');
plot(LNPL, 'r--');

title(title_s, 'FontSize',24);
ylabel(strcat(measure_s, ' (X)'),'FontSize',18);

grid on;
axis tight;
ylim auto;
hold off;

%===== Range Chart =====
subplot (2, 1, 2, "align");
plot(R);
hold on;

plot (mRv, 'g--');
plot (UCLr, 'r--');

xlabel('Measured Sample Number', 'FontSize',18);
ylabel('Moving Ranges (mR)','FontSize',18);

grid on;
axis tight;
ylim auto;

hold off;

%===== Histogram =====

% Calculate Histogram Values
[numHits, binCenters] = hist(xyData, nBins);
yStd = std(xyData);

% Make a normal dist curve fit
xStep = (max(xyData) - min(xyData)) / (nBins * 10); 
xFitDat = [min(xyData): xStep : max(xyData)];
xHistFit = normpdf(xFitDat, yMean, 1);  % yStd);

% Scale the amplitude
maxHistFit = max(xHistFit);
maxHist = max(numHits);

xHistFit = xHistFit .* (maxHist / maxHistFit);

% Plot the histogram
figure(2);
bar(binCenters, numHits, "facecolor", "y");

hold on;

plot(xFitDat, xHistFit, 'r');

% Annotation
title(title_s, 'FontSize',24);
xlabel(measure_s, 'FontSize',18);
ylabel('Number of Occurrences','FontSize',18);

grid on;
axis tight;
ylim auto;
hold off;


