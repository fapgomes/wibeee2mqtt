# Overview

This program can be used to parse WIBEEE status (https://www.wibeee.com/), and publish to a mqtt server.

# Installation
Clone the repo
```
cd /opt
sudo git clone https://github.com/fapgomes/wibeee2mqtt.git
```
Copy the sample config file, and put your own configurations
```
cd /opt/wibeee2mqtt/
sudo cp wibeee2mqtt.conf-sample wibeee2mqtt.conf
```
Create the system file
```sudo vi /etc/systemd/system/wibeee2mqtt.service```
And add the following to this file:
```
[Unit]
Description=wibeee2mqtt
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/wibeee2mqtt/wibeee.py
WorkingDirectory=/opt/wibeee2mqtt
StandardOutput=inherit
StandardError=inherit
Restart=always
User=openhab

[Install]
WantedBy=multi-user.target
```
Reload systemd daemon
```
sudo systemctl daemon-reload
```
Start the service
```
sudo systemctl start wibeee2mqtt
```
# openhab mqtt config example
wibeee.things
```
Bridge mqtt:broker:mosquitto "MQTT Broker: Mosquitto"
[
    host="localhost",
    port=1883,
    secure="AUTO",
    username="openhab",
    password="testpassword"
]
{
    ///////
    // wibeee2mqtt
    ///////
    Thing topic wibeee2mqtt "WIBEEE" @ "Cave" {
    Channels:
        Type string     : model                         "WIBEEE model"                      [ stateTopic="wibeee/model" ]
        Type datetime   : timestamp                     "WIBEEE Timestamp"                  [ stateTopic="wibeee/time" ]
        Type number     : fase1_vrms                    "WIBEEE VRMS"                       [ stateTopic="wibeee/fase1_vrms" ]
        Type number     : fase1_irms                    "WIBEEE IRMS"                       [ stateTopic="wibeee/fase1_irms" ]
        Type number     : fase1_p_aparent               "WIBEEE P. Aparent"                 [ stateTopic="wibeee/fase1_p_aparent" ]
        Type number     : fase1_p_activa                "WIBEEE P. Active"                  [ stateTopic="wibeee/fase1_p_activa" ]
        Type number     : fase1_p_reactiva_ind          "WIBEEE P. Reactiva Ind."           [ stateTopic="wibeee/fase1_p_reactiva_ind" ]
        Type number     : fase1_p_reactiva_cap          "WIBEEE P. Reactiva Cap."           [ stateTopic="wibeee/fase1_p_reactiva_cap" ]
        Type number     : fase1_frecuencia              "WIBEEE Frequencia"                 [ stateTopic="wibeee/fase1_frecuencia" ]
        Type number     : fase1_factor_potencia         "WIBEEE Factor Potencia"            [ stateTopic="wibeee/fase1_factor_potencia" ]
        Type number     : fase1_energia_activa          "WIBEEE Energia Activa"             [ stateTopic="wibeee/fase1_energia_activa" ]
        Type number     : fase1_energia_reactiva_ind    "WIBEEE Energia Reactiva Ind."      [ stateTopic="wibeee/fase1_energia_reactiva_ind" ]
        Type number     : fase1_energia_reactiva_cap    "WIBEEE Energia Reactiva Cap."      [ stateTopic="wibeee/fase1_energia_reactiva_cap" ]
        Type number     : fase1_thd_fun_V               "WIBEEE Voltage"                    [ stateTopic="wibeee/fase1_thd_fun_V" ]
        Type number     : fase1_angle                   "WIBEEE Angle"                      [ stateTopic="wibeee/fase1_angle" ]
        Type number     : fase2_vrms                    "WIBEEE VRMS"                       [ stateTopic="wibeee/fase2_vrms" ]
        Type number     : fase2_irms                    "WIBEEE IRMS"                       [ stateTopic="wibeee/fase2_irms" ]
        Type number     : fase2_p_aparent               "WIBEEE P. Aparent"                 [ stateTopic="wibeee/fase2_p_aparent" ]
        Type number     : fase2_p_activa                "WIBEEE P. Active"                  [ stateTopic="wibeee/fase2_p_activa" ]
        Type number     : fase2_p_reactiva_ind          "WIBEEE P. Reactiva Ind."           [ stateTopic="wibeee/fase2_p_reactiva_ind" ]
        Type number     : fase2_p_reactiva_cap          "WIBEEE P. Reactiva Cap."           [ stateTopic="wibeee/fase2_p_reactiva_cap" ]
        Type number     : fase2_frecuencia              "WIBEEE Frequencia"                 [ stateTopic="wibeee/fase2_frecuencia" ]
        Type number     : fase2_factor_potencia         "WIBEEE Factor Potencia"            [ stateTopic="wibeee/fase2_factor_potencia" ]
        Type number     : fase2_energia_activa          "WIBEEE Energia Activa"             [ stateTopic="wibeee/fase2_energia_activa" ]
        Type number     : fase2_energia_reactiva_ind    "WIBEEE Energia Reactiva Ind."      [ stateTopic="wibeee/fase2_energia_reactiva_ind" ]
        Type number     : fase2_energia_reactiva_cap    "WIBEEE Energia Reactiva Cap."      [ stateTopic="wibeee/fase2_energia_reactiva_cap" ]
        Type number     : fase2_thd_fun_V               "WIBEEE Voltage"                    [ stateTopic="wibeee/fase2_thd_fun_V" ]
        Type number     : fase2_angle                   "WIBEEE Angle"                      [ stateTopic="wibeee/fase2_angle" ]
        Type number     : fase3_vrms                    "WIBEEE VRMS"                       [ stateTopic="wibeee/fase3_vrms" ]
        Type number     : fase3_irms                    "WIBEEE IRMS"                       [ stateTopic="wibeee/fase3_irms" ]
        Type number     : fase3_p_aparent               "WIBEEE P. Aparent"                 [ stateTopic="wibeee/fase3_p_aparent" ]
        Type number     : fase3_p_activa                "WIBEEE P. Active"                  [ stateTopic="wibeee/fase3_p_activa" ]
        Type number     : fase3_p_reactiva_ind          "WIBEEE P. Reactiva Ind."           [ stateTopic="wibeee/fase3_p_reactiva_ind" ]
        Type number     : fase3_p_reactiva_cap          "WIBEEE P. Reactiva Cap."           [ stateTopic="wibeee/fase3_p_reactiva_cap" ]
        Type number     : fase3_frecuencia              "WIBEEE Frequencia"                 [ stateTopic="wibeee/fase3_frecuencia" ]
        Type number     : fase3_factor_potencia         "WIBEEE Factor Potencia"            [ stateTopic="wibeee/fase3_factor_potencia" ]
        Type number     : fase3_energia_activa          "WIBEEE Energia Activa"             [ stateTopic="wibeee/fase3_energia_activa" ]
        Type number     : fase3_energia_reactiva_ind    "WIBEEE Energia Reactiva Ind."      [ stateTopic="wibeee/fase3_energia_reactiva_ind" ]
        Type number     : fase3_energia_reactiva_cap    "WIBEEE Energia Reactiva Cap."      [ stateTopic="wibeee/fase3_energia_reactiva_cap" ]
        Type number     : fase3_thd_fun_V               "WIBEEE Voltage"                    [ stateTopic="wibeee/fase3_thd_fun_V" ]
        Type number     : fase3_angle                   "WIBEEE Angle"                      [ stateTopic="wibeee/fase3_angle" ]
        Type number     : fase4_vrms                    "WIBEEE VRMS"                       [ stateTopic="wibeee/fase4_vrms" ]
        Type number     : fase4_irms                    "WIBEEE IRMS"                       [ stateTopic="wibeee/fase4_irms" ]
        Type number     : fase4_p_aparent               "WIBEEE P. Aparent"                 [ stateTopic="wibeee/fase4_p_aparent" ]
        Type number     : fase4_p_activa                "WIBEEE P. Active"                  [ stateTopic="wibeee/fase4_p_activa" ]
        Type number     : fase4_p_reactiva_ind          "WIBEEE P. Reactiva Ind."           [ stateTopic="wibeee/fase4_p_reactiva_ind" ]
        Type number     : fase4_p_reactiva_cap          "WIBEEE P. Reactiva Cap."           [ stateTopic="wibeee/fase4_p_reactiva_cap" ]
        Type number     : fase4_frecuencia              "WIBEEE Frequencia"                 [ stateTopic="wibeee/fase4_frecuencia" ]
        Type number     : fase4_factor_potencia         "WIBEEE Factor Potencia"            [ stateTopic="wibeee/fase4_factor_potencia" ]
        Type number     : fase4_energia_activa          "WIBEEE Energia Activa"             [ stateTopic="wibeee/fase4_energia_activa" ]
        Type number     : fase4_energia_reactiva_ind    "WIBEEE Energia Reactiva Ind."      [ stateTopic="wibeee/fase4_energia_reactiva_ind" ]
        Type number     : fase4_energia_reactiva_cap    "WIBEEE Energia Reactiva Cap."      [ stateTopic="wibeee/fase4_energia_reactiva_cap" ]
    }
 }
```
 wibeee.items
```
Group                   gWibeee                     "Wibeee"                                                    <energy>
String                  wibeeeModel                 "Model [%s]"                                                <settings>              (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:model" }
DateTime                wibeeeTimeStamp             "Time [%1$tY-%1$tm-%1$td  %1$tH:%1$tM]"                     <time>                  (gWibeee, gCheckProblems)                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:timestamp" }
Number                  wibeeeFase1Vrms             "Fase 1 Voltage [%.2f V]"                                   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_vrms" }
Number                  wibeeeFase1Irms             "Fase 1 Amp [%.2f A]"                                       <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_irms" }
Number                  wibeeeFase1PAparent         "Fase 1 Aparent [%.2f w]"                                   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_p_aparent" }
Number                  wibeeeFase1PActiva          "Fase 1 Activa [%.2f w]"                                    <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_p_activa" }
Number                  wibeeeFase1PReactivaInd     "Fase 1 Reactiva Ind [%.2f w]"                              <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_p_reactiva_ind" }
Number                  wibeeeFase1PReactivaCap     "Fase 1 Reactiva Cap [%.2f w]"                              <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_p_reactiva_cap" }
Number                  wibeeeFase1Frequencia       "Fase 1 Frequência [%.2f Hz]"                               <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_frecuencia" }
Number                  wibeeeFase1FactorPotencia   "Fase 1 Factor Potência [%.2f]"                             <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_factor_potencia" }
Number                  wibeeeFase1EnergiaActiva    "Fase 1 Energia Activa [JS(divide1000.js):%.1f kw]"         <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_energia_activa" }
Number                  wibeeeFase1EnergiaReactivaI "Fase 1 Energia Reactiva Ind [JS(divide1000.js):%.1f kw]"   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_energia_reactiva_ind" }
Number                  wibeeeFase1EnergiaReactivaC "Fase 1 Energia Reactiva Cap [JS(divide1000.js):%.1f kw]"   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_energia_reactiva_cap" }
Number                  wibeeeFase1Angle            "Fase 1 Angle [%d º]"                                       <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase1_angle" }
Number                  wibeeeFase2Vrms             "Fase 2 Voltage [%.2f V]"                                   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_vrms" }
Number                  wibeeeFase2Irms             "Fase 2 Amp [%.2f A]"                                       <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_irms" }
Number                  wibeeeFase2PAparent         "Fase 2 Aparent [%.2f w]"                                   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_p_aparent" }
Number                  wibeeeFase2PActiva          "Fase 2 Activa [%.2f w]"                                    <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_p_activa" }
Number                  wibeeeFase2PReactivaInd     "Fase 2 Reactiva Ind [%.2f w]"                              <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_p_reactiva_ind" }
Number                  wibeeeFase2PReactivaCap     "Fase 2 Reactiva Cap [%.2f w]"                              <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_p_reactiva_cap" }
Number                  wibeeeFase2Frequencia       "Fase 2 Frequência [%.2f Hz]"                               <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_frecuencia" }
Number                  wibeeeFase2FactorPotencia   "Fase 2 Factor Potência [%.2f]"                             <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_factor_potencia" }
Number                  wibeeeFase2EnergiaActiva    "Fase 2 Energia Activa [JS(divide1000.js):%.1f kw]"         <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_energia_activa" }
Number                  wibeeeFase2EnergiaReactivaI "Fase 2 Energia Reactiva Ind [JS(divide1000.js):%.1f kw]"   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_energia_reactiva_ind" }
Number                  wibeeeFase2EnergiaReactivaC "Fase 2 Energia Reactiva Cap [JS(divide1000.js):%.1f kw]"   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase2_energia_reactiva_cap" }
Number                  wibeeeFase3Vrms             "Fase 3 Voltage [%.2f V]"                                   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_vrms" }
Number                  wibeeeFase3Irms             "Fase 3 Amp [%.2f A]"                                       <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_irms" }
Number                  wibeeeFase3PAparent         "Fase 3 Aparent [%.2f w]"                                   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_p_aparent" }
Number                  wibeeeFase3PActiva          "Fase 3 Activa [%.2f w]"                                    <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_p_activa" }
Number                  wibeeeFase3PReactivaInd     "Fase 3 Reactiva Ind [%.2f w]"                              <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_p_reactiva_ind" }
Number                  wibeeeFase3PReactivaCap     "Fase 3 Reactiva Cap [%.2f w]"                              <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_p_reactiva_cap" }
Number                  wibeeeFase3Frequencia       "Fase 3 Frequência [%.2f Hz]"                               <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_frecuencia" }
Number                  wibeeeFase3FactorPotencia   "Fase 3 Factor Potência [%.2f]"                             <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_factor_potencia" }
Number                  wibeeeFase3EnergiaActiva    "Fase 3 Energia Activa [JS(divide1000.js):%.1f kw]"         <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_energia_activa" }
Number                  wibeeeFase3EnergiaReactivaI "Fase 3 Energia Reactiva Ind [JS(divide1000.js):%.1f kw]"   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_energia_reactiva_ind" }
Number                  wibeeeFase3EnergiaReactivaC "Fase 3 Energia Reactiva Cap [JS(divide1000.js):%.1f kw]"   <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_energia_reactiva_cap" }
Number                  wibeeeFase3Angle            "Fase 3 Angle [%d º]"                                       <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase3_angle" }
Number                  wibeeeFase4Vrms             "Total Voltage [%.2f V]"                                    <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_vrms" }
Number                  wibeeeFase4Irms             "Total Amp [%.2f A]"                                        <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_irms" }
Number                  wibeeeFase4PAparent         "Total Aparent [%.2f w]"                                    <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_p_aparent" }
Number                  wibeeeFase4PActiva          "Total Activa [%.2f w]"                                     <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_p_activa" }
Number                  wibeeeFase4PReactivaInd     "Total Reactiva Ind [%.2f w]"                               <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_p_reactiva_ind" }
Number                  wibeeeFase4PReactivaCap     "Total Reactiva Cap [%.2f w]"                               <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_p_reactiva_cap" }
Number                  wibeeeFase4Frequencia       "Total Frequência [%.2f Hz]"                                <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_frecuencia" }
Number                  wibeeeFase4FactorPotencia   "Total Factor Potência [%.2f]"                              <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_factor_potencia" }
Number                  wibeeeFase4EnergiaActiva    "Total Energia Activa [JS(divide1000.js):%.1f kw]"          <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_energia_activa" }
Number                  wibeeeFase4EnergiaReactivaI "Total Energia Reactiva Ind [JS(divide1000.js):%.1f kw]"    <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_energia_reactiva_ind" }
Number                  wibeeeFase4EnergiaReactivaC "Total Energia Reactiva Cap [JS(divide1000.js):%.1f kw]"    <energy>                (gWibeee)                                   { channel="mqtt:topic:mosquitto:wibeee2mqtt:fase4_energia_reactiva_cap" }

```

![Screenshot_20210522_165143](https://user-images.githubusercontent.com/39247306/119232689-0a3b3f00-bb1e-11eb-85dc-aad567e25ac5.png)
