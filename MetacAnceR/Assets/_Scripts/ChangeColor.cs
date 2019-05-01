using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeColor : MonoBehaviour {

    [SerializeField]
    private Color colorTurnTo = Color.white;

	public void ToggleColor()
    {
        Renderer rend = gameObject.GetComponent<Renderer>();
        Color currentColor = rend.material.color;
    }
}
