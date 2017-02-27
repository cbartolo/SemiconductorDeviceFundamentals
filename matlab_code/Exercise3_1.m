% mobility vs Dopant concentratino for silicon at 300K
% Fit parameters
 NDref=1.3e17; NAref=2.35e17;
 miun_min=92; miup_min=54.3;
 miun0=1268; miup0=406.9;
 an=0.91; ap=0.88;
 
 % MObility calculation
 %{
 N=logspace(14,19);
 miun=miun_min+miun0./(1+(N/NDref).^an);
 miup=miup_min+miup0./(1+(N/NAref).^ap);
 
 %Plotting results
 close
 loglog(N,miun,N,miup);  grid;
 axis([1.0e14 1.0e19 1.0e1 1.0e4]);
 xlabel('NA or ND (cm-3)');
 ylabel('Mobility (cm2/V-sec)');
 text(1.0e15,1500, 'Electrons' );
 text (1.0e15, 500, 'Holes');
 text(1.0e18,2000, 'Si,300K');
 %}
 
 
 
 T=logspace(200,500);
 N_T=[10e14 10e15 10e16 10e17 10e18];
 miun=miun_min+miun0./(1+(N_T/NDref).^an);
 miup=miup_min+miup0./(1+(N_T/NAref).^ap);
 
 NDref_T=NDref.*(T/300).^2.4;
 NAref_T=NAref.*(T/300).^2.4;
 miun_min_T=miun_min.*(T/300).^-0.57;
 miup_min_T=miup_min.*(T/300).^-0.57;
 miun0_T=miun0.*(T/300).^-2.33;
 miup0_T=miup0.*(T/300).^-2.23;
 an_T=an.*(T/300).^-0.146;
 ap_T=ap.*(T/300).^-0.146;


 
 miun_T=miun_min_T+miun0_T./(1+(N_T/NDref_T).^an);
 miup_T=miup_min_T+miup0_T./(1+(N_T/NAref_T).^ap);
 
