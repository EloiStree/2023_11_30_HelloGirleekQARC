## Exercice du jour

**Pour les étudiants orientés logique :**
- Créez un script qui modifie un système de particules.
- Créez un script qui crée un objet du niveau derrière la voiture.
- *Niveau intermédiaire :* Affichez sur la voiture une jauge d'informations :
  - Vitesse, nombre de collisions,
  - Distance avec des objets devant (voir Raycast).

**Pour les étudiants orientés couleur :**
- Utilisez Shader Graph pour personnaliser les couleurs de votre équipe ou de votre voiture.
  - *Niveau débutant :* Suivez un tutoriel sur Shader Graph pour créer le shader.
  - *Niveau intermédiaire :* Téléchargez des shaders depuis l'Asset Store et transformez-les pour URP.

*Optionnel, pour un expert :*
- Utilisez la clé Bluetooth sous Python pour communiquer avec la Xbox via le Brook.
- Utilisez un port série avec le TTL sous Python pour activer des relais Arduino.

# Qu'est-ce qu'un script ?

Un logiciel est constitué de millions de lignes de texte qui permettent de communiquer avec la machine. On appelle cela du code. Et quand il est massif, on appelle ça une architecture logicielle.

Pour permettre aux développeurs de travailler avec les game designers et les artistes, Unity3D a créé des scripts que l'on appelle des MonoBehaviour.

Ces scripts permettent :
- Aux développeurs juniors de commencer facilement sur Unity3D.
- Aux développeurs experts de prototyper rapidement.
- Aux designers de modifier les éléments du jeu sans devoir coder.
- Aux designers avec une connaissance du code de pouvoir adapter le jeu.
- ...

Dans cet atelier, je vais vous montrer comment, à l'aide de scripts, on peut affecter des particules et des objets dans Unity pour que vous personnalisiez votre modèle.

# Qu'est-ce que Shader Graph ?

Comme nous l'avons vu dans l'atelier précédent, les artistes peuvent créer des objets 3D et des objets 2D. Mais pour créer l'interaction de la lumière sur les triangles de l'objet, on a besoin de shaders. Avant, ce travail était celui d'un développeur, mais avec le no-code, c'est devenu un travail de graphiste.

Shader Graph est un outil fourni par Unity3D qui permet de très facilement fabriquer des effets complexes dans nos jeux sans connaître de code.

Dans cet atelier, je vais vous montrer les bases pour que vous puissiez créer vos propres shaders pour votre modèle 3D.



--------------------------------


# Send UDP message from Unity to external app

``` csharp

using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System;

public class UdpSender : MonoBehaviour
{
    public string ipAddress = "127.0.0.1";
    public int port = 12345;

    private UdpClient udpClient;
    public string m_quickStringTest;
    public string m_startWith;
    public string m_endWith;


    void Start()
    {
        udpClient = new UdpClient();
        SendStringUTF8("Hello, UDP!");
    }

    [ContextMenu("Quick String Test")]
    public void SendStringUTF8_StringTest() => SendStringUTF8(m_quickStringTest);
    [ContextMenu("Ping")]
    public void SendStringUTF8_Ping() => SendStringUTF8("Ping");
    [ContextMenu("Hello")]
    public void SendStringUTF8_Hello() => SendStringUTF8("Hello");
    [ContextMenu("Date")]
    public void SendStringUTF8_Date() => SendStringUTF8(DateTime.Now.ToString());

    public void SendStringUTF8(string message)
    {
        try
        {
            byte[] data = Encoding.UTF8.GetBytes(m_startWith+message+m_endWith);
            udpClient.Send(data, data.Length, ipAddress, port);
        }
        catch (Exception e)
        {
            Debug.LogError($"Error sending UDP message: {e.Message}");
        }
    }
    public void SendStringUnicode(string message)
    {
        try
        {
            byte[] data = Encoding.Unicode.GetBytes(m_startWith + message + m_endWith);
            udpClient.Send(data, data.Length, ipAddress, port);
        }
        catch (Exception e)
        {
            Debug.LogError($"Error sending UDP message: {e.Message}");
        }
    }

    void OnDestroy()
    {
        if (udpClient != null)
        {
            udpClient.Close();
        }
    }
}
```





# Send message with Websocket client


``` csharp

using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using NativeWebSocket;

public class WebsocketClientSender : MonoBehaviour
{
    public string m_websocketServer = "ws://localhost:2567";
    WebSocket websocket;
    public string m_quickStringTest;
    public string m_startWith;
    public string m_endWith;

    async void Start()
    {
        websocket = new WebSocket(m_websocketServer);

        websocket.OnOpen += () =>
        {
            Debug.Log("Connection open!");
        };

        websocket.OnError += (e) =>
        {
            Debug.Log("Error! " + e);
        };

        websocket.OnClose += (e) =>
        {
            Debug.Log("Connection closed!");
        };

        websocket.OnMessage += (bytes) =>
        {
            Debug.Log("OnMessage!");
            Debug.Log(bytes);

             //getting the message as a string
             var message = System.Text.Encoding.UTF8.GetString(bytes);
             Debug.Log("OnMessage! " + message);
        };

        // Keep sending messages at every 0.3s
        //InvokeRepeating("SendWebSocketMessage", 0.0f, 0.3f);

        // waiting for messages
        await websocket.Connect();
    }

    void Update()
    {
#if !UNITY_WEBGL || UNITY_EDITOR
        websocket.DispatchMessageQueue();
#endif
    }


    [ContextMenu("Quick String Test")]
    public void SendStringUTF8_StringTest() => SendWebSocketMessage(m_quickStringTest);

    [ContextMenu("Send Ping")]
    public void SendPing() { SendWebSocketMessage("Ping"); }

    [ContextMenu("Send Now")]
    public void SendNow() { SendWebSocketMessage(DateTime.Now.ToString()); }

    async void SendWebSocketMessage()
    {
        if (websocket.State == WebSocketState.Open)
        {
            // Sending bytes
            await websocket.Send(new byte[] { 10, 20, 30 });

            // Sending plain text
            await websocket.SendText("plain text message");
        }
    }
    async void SendWebSocketMessage(string message)
    {
        if (websocket.State == WebSocketState.Open)
        {
            await websocket.SendText(m_startWith+message+m_endWith);
        }
    }
    async void SendWebSocketMessage(byte[] bytes)
    {
        if (websocket.State == WebSocketState.Open)
        {
            await websocket.Send(bytes);
        }
    }

    private async void OnApplicationQuit()
    {
        await websocket.Close();
    }

}


```


