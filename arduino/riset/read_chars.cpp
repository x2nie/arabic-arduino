// https://forum.arduino.cc/t/receive-binary-data-into-a-variable/135202/7

void loop()
{
  if ( Serial.available() == 8 )
  {
    byte bytes[8];
    for ( uint8_t i = 0; i < 8; i++ )
      bytes[i] = Serial.read();

    byte result = 0;
    for ( uint8_t i = 0; i < 8; i++ )
      result += bytes[7-i] << i;

    byte ID = (result & 0xF0) >> 4;
    if ( ID == ARDUINO_ID )
    {
      byte ASCII =  result & 0x0F;
      DisplayTo7Seg( ASCII );
    }
  }
}