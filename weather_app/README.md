# 🌦️ Weather App

Mostra o clima atual e a previsão para a sua localização ou para um local digitado, usando as APIs da AccuWeather e do Mapbox.

## 🔑 Chaves de API

As chaves não ficam no código. Elas são lidas de variáveis de ambiente:

| Variável | Onde obter |
|---|---|
| `ACCUWEATHER_API_KEY` | https://developer.accuweather.com |
| `MAPBOX_TOKEN` | https://account.mapbox.com/access-tokens |

## ▶️ Como executar

```bash
pip install requests
export ACCUWEATHER_API_KEY="sua-chave"
export MAPBOX_TOKEN="seu-token"
python weather_app.py
```
