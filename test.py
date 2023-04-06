def parse_string(s):
    stack = []
    current_obj = {}
    for token in s.split():
        
        if token == '(':
            stack.append(current_obj)
            current_obj = {}
        elif token == ')':
            if stack:
                parent_obj = stack.pop()
                parent_obj[current_obj['name']] = current_obj['elements']
                current_obj = parent_obj
        else:
            if 'name' not in current_obj:
                current_obj['name'] = token
                current_obj['elements'] = {}
            else:
                current_obj['elements'][token] = None
    return current_obj['elements']


kicad_obj = (parse_string("""
(lib_symbols
  (symbol "MCU_ST_STM32G4:STM32G431CBUx" (in_bom yes) (on_board yes)
    (property "Reference" "U" (at -12.7 44.45 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "STM32G431CBUx" (at 10.16 44.45 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm" (at -12.7 -40.64 0)
      (effects (font (size 1.27 1.27)) (justify right) hide)
    )
    (property "Datasheet" "https://www.st.com/resource/en/datasheet/stm32g431cb.pdf" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_locked" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "ki_keywords" "Arm Cortex-M4 STM32G4 STM32G4x1" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "STMicroelectronics Arm Cortex-M4 MCU, 128KB flash, 32KB RAM, 170 MHz, 1.71-3.6V, 42 GPIO, UFQFPN48" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_fp_filters" "QFN*1EP*7x7mm*P0.5mm*" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "STM32G431CBUx_0_1"
      (rectangle (start -12.7 -40.64) (end 15.24 43.18)
        (stroke (width 0.254) (type default))
        (fill (type background))
      )
    )
    (symbol "STM32G431CBUx_1_1"
      (pin power_in line (at -2.54 45.72 270) (length 2.54)
        (name "VBAT" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin bidirectional line (at 17.78 35.56 180) (length 2.54)
        (name "PA2" (effects (font (size 1.27 1.27))))
        (number "10" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN3" bidirectional line)
        (alternate "COMP2_INM" bidirectional line)
        (alternate "COMP2_OUT" bidirectional line)
        (alternate "LPUART1_TX" bidirectional line)
        (alternate "OPAMP1_VOUT" bidirectional line)
        (alternate "RCC_LSCO" bidirectional line)
        (alternate "SYS_WKUP4" bidirectional line)
        (alternate "TIM15_CH1" bidirectional line)
        (alternate "TIM2_CH3" bidirectional line)
        (alternate "UCPD1_FRSTX1" bidirectional line)
        (alternate "UCPD1_FRSTX2" bidirectional line)
        (alternate "USART2_TX" bidirectional line)
      )
      (pin bidirectional line (at 17.78 33.02 180) (length 2.54)
        (name "PA3" (effects (font (size 1.27 1.27))))
        (number "11" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN4" bidirectional line)
        (alternate "COMP2_INP" bidirectional line)
        (alternate "LPUART1_RX" bidirectional line)
        (alternate "OPAMP1_VINM" bidirectional line)
        (alternate "OPAMP1_VINM0" bidirectional line)
        (alternate "OPAMP1_VINM_SEC" bidirectional line)
        (alternate "OPAMP1_VINP" bidirectional line)
        (alternate "OPAMP1_VINP_SEC" bidirectional line)
        (alternate "SAI1_CK1" bidirectional line)
        (alternate "SAI1_MCLK_A" bidirectional line)
        (alternate "TIM15_CH2" bidirectional line)
        (alternate "TIM2_CH4" bidirectional line)
        (alternate "USART2_RX" bidirectional line)
      )
      (pin bidirectional line (at 17.78 30.48 180) (length 2.54)
        (name "PA4" (effects (font (size 1.27 1.27))))
        (number "12" (effects (font (size 1.27 1.27))))
        (alternate "ADC2_IN17" bidirectional line)
        (alternate "COMP1_INM" bidirectional line)
        (alternate "DAC1_OUT1" bidirectional line)
        (alternate "I2S3_WS" bidirectional line)
        (alternate "SAI1_FS_B" bidirectional line)
        (alternate "SPI1_NSS" bidirectional line)
        (alternate "SPI3_NSS" bidirectional line)
        (alternate "TIM3_CH2" bidirectional line)
        (alternate "USART2_CK" bidirectional line)
      )
      (pin bidirectional line (at 17.78 27.94 180) (length 2.54)
        (name "PA5" (effects (font (size 1.27 1.27))))
        (number "13" (effects (font (size 1.27 1.27))))
        (alternate "ADC2_IN13" bidirectional line)
        (alternate "COMP2_INM" bidirectional line)
        (alternate "DAC1_OUT2" bidirectional line)
        (alternate "OPAMP2_VINM" bidirectional line)
        (alternate "OPAMP2_VINM0" bidirectional line)
        (alternate "OPAMP2_VINM_SEC" bidirectional line)
        (alternate "SPI1_SCK" bidirectional line)
        (alternate "TIM2_CH1" bidirectional line)
        (alternate "TIM2_ETR" bidirectional line)
        (alternate "UCPD1_FRSTX1" bidirectional line)
        (alternate "UCPD1_FRSTX2" bidirectional line)
      )
      (pin bidirectional line (at 17.78 25.4 180) (length 2.54)
        (name "PA6" (effects (font (size 1.27 1.27))))
        (number "14" (effects (font (size 1.27 1.27))))
        (alternate "ADC2_IN3" bidirectional line)
        (alternate "COMP1_OUT" bidirectional line)
        (alternate "LPUART1_CTS" bidirectional line)
        (alternate "OPAMP2_VOUT" bidirectional line)
        (alternate "SPI1_MISO" bidirectional line)
        (alternate "TIM16_CH1" bidirectional line)
        (alternate "TIM1_BKIN" bidirectional line)
        (alternate "TIM3_CH1" bidirectional line)
        (alternate "TIM8_BKIN" bidirectional line)
      )
      (pin bidirectional line (at 17.78 22.86 180) (length 2.54)
        (name "PA7" (effects (font (size 1.27 1.27))))
        (number "15" (effects (font (size 1.27 1.27))))
        (alternate "ADC2_IN4" bidirectional line)
        (alternate "COMP2_INP" bidirectional line)
        (alternate "COMP2_OUT" bidirectional line)
        (alternate "OPAMP1_VINP" bidirectional line)
        (alternate "OPAMP1_VINP_SEC" bidirectional line)
        (alternate "OPAMP2_VINP" bidirectional line)
        (alternate "OPAMP2_VINP_SEC" bidirectional line)
        (alternate "SPI1_MOSI" bidirectional line)
        (alternate "TIM17_CH1" bidirectional line)
        (alternate "TIM1_CH1N" bidirectional line)
        (alternate "TIM3_CH2" bidirectional line)
        (alternate "TIM8_CH1N" bidirectional line)
        (alternate "UCPD1_FRSTX1" bidirectional line)
        (alternate "UCPD1_FRSTX2" bidirectional line)
      )
      (pin bidirectional line (at -15.24 22.86 0) (length 2.54)
        (name "PC4" (effects (font (size 1.27 1.27))))
        (number "16" (effects (font (size 1.27 1.27))))
        (alternate "ADC2_IN5" bidirectional line)
        (alternate "I2C2_SCL" bidirectional line)
        (alternate "TIM1_ETR" bidirectional line)
        (alternate "USART1_TX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 2.54 0) (length 2.54)
        (name "PB0" (effects (font (size 1.27 1.27))))
        (number "17" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN15" bidirectional line)
        (alternate "COMP4_INP" bidirectional line)
        (alternate "OPAMP2_VINP" bidirectional line)
        (alternate "OPAMP2_VINP_SEC" bidirectional line)
        (alternate "OPAMP3_VINP" bidirectional line)
        (alternate "OPAMP3_VINP_SEC" bidirectional line)
        (alternate "TIM1_CH2N" bidirectional line)
        (alternate "TIM3_CH3" bidirectional line)
        (alternate "TIM8_CH2N" bidirectional line)
        (alternate "UCPD1_FRSTX1" bidirectional line)
        (alternate "UCPD1_FRSTX2" bidirectional line)
      )
      (pin bidirectional line (at -15.24 0 0) (length 2.54)
        (name "PB1" (effects (font (size 1.27 1.27))))
        (number "18" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN12" bidirectional line)
        (alternate "COMP1_INP" bidirectional line)
        (alternate "COMP4_OUT" bidirectional line)
        (alternate "LPUART1_DE" bidirectional line)
        (alternate "LPUART1_RTS" bidirectional line)
        (alternate "OPAMP3_VOUT" bidirectional line)
        (alternate "TIM1_CH3N" bidirectional line)
        (alternate "TIM3_CH4" bidirectional line)
        (alternate "TIM8_CH3N" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -2.54 0) (length 2.54)
        (name "PB2" (effects (font (size 1.27 1.27))))
        (number "19" (effects (font (size 1.27 1.27))))
        (alternate "ADC2_IN12" bidirectional line)
        (alternate "COMP4_INM" bidirectional line)
        (alternate "I2C3_SMBA" bidirectional line)
        (alternate "LPTIM1_OUT" bidirectional line)
        (alternate "OPAMP3_VINM" bidirectional line)
        (alternate "OPAMP3_VINM0" bidirectional line)
        (alternate "OPAMP3_VINM_SEC" bidirectional line)
        (alternate "RTC_OUT2" bidirectional line)
      )
      (pin bidirectional line (at -15.24 12.7 0) (length 2.54)
        (name "PC13" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
        (alternate "RTC_OUT1" bidirectional line)
        (alternate "RTC_TAMP1" bidirectional line)
        (alternate "RTC_TS" bidirectional line)
        (alternate "SYS_WKUP2" bidirectional line)
        (alternate "TIM1_BKIN" bidirectional line)
        (alternate "TIM1_CH1N" bidirectional line)
        (alternate "TIM8_CH4N" bidirectional line)
      )
      (pin input line (at -15.24 40.64 0) (length 2.54)
        (name "VREF+" (effects (font (size 1.27 1.27))))
        (number "20" (effects (font (size 1.27 1.27))))
        (alternate "VREFBUF_OUT" bidirectional line)
      )
      (pin power_in line (at 7.62 45.72 270) (length 2.54)
        (name "VDDA" (effects (font (size 1.27 1.27))))
        (number "21" (effects (font (size 1.27 1.27))))
      )
      (pin bidirectional line (at -15.24 -22.86 0) (length 2.54)
        (name "PB10" (effects (font (size 1.27 1.27))))
        (number "22" (effects (font (size 1.27 1.27))))
        (alternate "DAC1_EXTI10" bidirectional line)
        (alternate "DAC3_EXTI10" bidirectional line)
        (alternate "LPUART1_RX" bidirectional line)
        (alternate "OPAMP3_VINM" bidirectional line)
        (alternate "OPAMP3_VINM1" bidirectional line)
        (alternate "OPAMP3_VINM_SEC" bidirectional line)
        (alternate "SAI1_SCK_A" bidirectional line)
        (alternate "TIM1_BKIN" bidirectional line)
        (alternate "TIM2_CH3" bidirectional line)
        (alternate "USART3_TX" bidirectional line)
      )
      (pin power_in line (at 0 45.72 270) (length 2.54)
        (name "VDD" (effects (font (size 1.27 1.27))))
        (number "23" (effects (font (size 1.27 1.27))))
      )
      (pin bidirectional line (at -15.24 -25.4 0) (length 2.54)
        (name "PB11" (effects (font (size 1.27 1.27))))
        (number "24" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_EXTI11" bidirectional line)
        (alternate "ADC1_IN14" bidirectional line)
        (alternate "ADC2_EXTI11" bidirectional line)
        (alternate "ADC2_IN14" bidirectional line)
        (alternate "LPUART1_TX" bidirectional line)
        (alternate "TIM2_CH4" bidirectional line)
        (alternate "USART3_RX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -27.94 0) (length 2.54)
        (name "PB12" (effects (font (size 1.27 1.27))))
        (number "25" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN11" bidirectional line)
        (alternate "I2C2_SMBA" bidirectional line)
        (alternate "I2S2_WS" bidirectional line)
        (alternate "LPUART1_DE" bidirectional line)
        (alternate "LPUART1_RTS" bidirectional line)
        (alternate "SPI2_NSS" bidirectional line)
        (alternate "TIM1_BKIN" bidirectional line)
        (alternate "USART3_CK" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -30.48 0) (length 2.54)
        (name "PB13" (effects (font (size 1.27 1.27))))
        (number "26" (effects (font (size 1.27 1.27))))
        (alternate "I2S2_CK" bidirectional line)
        (alternate "LPUART1_CTS" bidirectional line)
        (alternate "OPAMP3_VINP" bidirectional line)
        (alternate "OPAMP3_VINP_SEC" bidirectional line)
        (alternate "SPI2_SCK" bidirectional line)
        (alternate "TIM1_CH1N" bidirectional line)
        (alternate "USART3_CTS" bidirectional line)
        (alternate "USART3_NSS" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -33.02 0) (length 2.54)
        (name "PB14" (effects (font (size 1.27 1.27))))
        (number "27" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN5" bidirectional line)
        (alternate "COMP4_OUT" bidirectional line)
        (alternate "OPAMP2_VINP" bidirectional line)
        (alternate "OPAMP2_VINP_SEC" bidirectional line)
        (alternate "SPI2_MISO" bidirectional line)
        (alternate "TIM15_CH1" bidirectional line)
        (alternate "TIM1_CH2N" bidirectional line)
        (alternate "USART3_DE" bidirectional line)
        (alternate "USART3_RTS" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -35.56 0) (length 2.54)
        (name "PB15" (effects (font (size 1.27 1.27))))
        (number "28" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_EXTI15" bidirectional line)
        (alternate "ADC2_EXTI15" bidirectional line)
        (alternate "ADC2_IN15" bidirectional line)
        (alternate "COMP3_OUT" bidirectional line)
        (alternate "I2S2_SD" bidirectional line)
        (alternate "RTC_REFIN" bidirectional line)
        (alternate "SPI2_MOSI" bidirectional line)
        (alternate "TIM15_CH1N" bidirectional line)
        (alternate "TIM15_CH2" bidirectional line)
        (alternate "TIM1_CH3N" bidirectional line)
      )
      (pin bidirectional line (at -15.24 20.32 0) (length 2.54)
        (name "PC6" (effects (font (size 1.27 1.27))))
        (number "29" (effects (font (size 1.27 1.27))))
        (alternate "I2S2_MCK" bidirectional line)
        (alternate "TIM3_CH1" bidirectional line)
        (alternate "TIM8_CH1" bidirectional line)
      )
      (pin bidirectional line (at -15.24 10.16 0) (length 2.54)
        (name "PC14" (effects (font (size 1.27 1.27))))
        (number "3" (effects (font (size 1.27 1.27))))
        (alternate "RCC_OSC32_IN" bidirectional line)
      )
      (pin bidirectional line (at 17.78 20.32 180) (length 2.54)
        (name "PA8" (effects (font (size 1.27 1.27))))
        (number "30" (effects (font (size 1.27 1.27))))
        (alternate "I2C2_SDA" bidirectional line)
        (alternate "I2C3_SCL" bidirectional line)
        (alternate "I2S2_MCK" bidirectional line)
        (alternate "RCC_MCO" bidirectional line)
        (alternate "SAI1_CK2" bidirectional line)
        (alternate "SAI1_SCK_A" bidirectional line)
        (alternate "TIM1_CH1" bidirectional line)
        (alternate "TIM4_ETR" bidirectional line)
        (alternate "USART1_CK" bidirectional line)
      )
      (pin bidirectional line (at 17.78 17.78 180) (length 2.54)
        (name "PA9" (effects (font (size 1.27 1.27))))
        (number "31" (effects (font (size 1.27 1.27))))
        (alternate "DAC1_EXTI9" bidirectional line)
        (alternate "DAC3_EXTI9" bidirectional line)
        (alternate "I2C2_SCL" bidirectional line)
        (alternate "I2C3_SMBA" bidirectional line)
        (alternate "I2S3_MCK" bidirectional line)
        (alternate "SAI1_FS_A" bidirectional line)
        (alternate "TIM15_BKIN" bidirectional line)
        (alternate "TIM1_CH2" bidirectional line)
        (alternate "TIM2_CH3" bidirectional line)
        (alternate "UCPD1_DBCC1" bidirectional line)
        (alternate "USART1_TX" bidirectional line)
      )
      (pin bidirectional line (at 17.78 15.24 180) (length 2.54)
        (name "PA10" (effects (font (size 1.27 1.27))))
        (number "32" (effects (font (size 1.27 1.27))))
        (alternate "CRS_SYNC" bidirectional line)
        (alternate "DAC1_EXTI10" bidirectional line)
        (alternate "DAC3_EXTI10" bidirectional line)
        (alternate "I2C2_SMBA" bidirectional line)
        (alternate "SAI1_D1" bidirectional line)
        (alternate "SAI1_SD_A" bidirectional line)
        (alternate "SPI2_MISO" bidirectional line)
        (alternate "TIM17_BKIN" bidirectional line)
        (alternate "TIM1_CH3" bidirectional line)
        (alternate "TIM2_CH4" bidirectional line)
        (alternate "TIM8_BKIN" bidirectional line)
        (alternate "UCPD1_DBCC2" bidirectional line)
        (alternate "USART1_RX" bidirectional line)
      )
      (pin bidirectional line (at 17.78 12.7 180) (length 2.54)
        (name "PA11" (effects (font (size 1.27 1.27))))
        (number "33" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_EXTI11" bidirectional line)
        (alternate "ADC2_EXTI11" bidirectional line)
        (alternate "COMP1_OUT" bidirectional line)
        (alternate "FDCAN1_RX" bidirectional line)
        (alternate "I2S2_SD" bidirectional line)
        (alternate "SPI2_MOSI" bidirectional line)
        (alternate "TIM1_BKIN2" bidirectional line)
        (alternate "TIM1_CH1N" bidirectional line)
        (alternate "TIM1_CH4" bidirectional line)
        (alternate "TIM4_CH1" bidirectional line)
        (alternate "USART1_CTS" bidirectional line)
        (alternate "USART1_NSS" bidirectional line)
        (alternate "USB_DM" bidirectional line)
      )
      (pin bidirectional line (at 17.78 10.16 180) (length 2.54)
        (name "PA12" (effects (font (size 1.27 1.27))))
        (number "34" (effects (font (size 1.27 1.27))))
        (alternate "COMP2_OUT" bidirectional line)
        (alternate "FDCAN1_TX" bidirectional line)
        (alternate "I2S_CKIN" bidirectional line)
        (alternate "TIM16_CH1" bidirectional line)
        (alternate "TIM1_CH2N" bidirectional line)
        (alternate "TIM1_ETR" bidirectional line)
        (alternate "TIM4_CH2" bidirectional line)
        (alternate "USART1_DE" bidirectional line)
        (alternate "USART1_RTS" bidirectional line)
        (alternate "USB_DP" bidirectional line)
      )
      (pin power_in line (at 2.54 45.72 270) (length 2.54)
        (name "VDD" (effects (font (size 1.27 1.27))))
        (number "35" (effects (font (size 1.27 1.27))))
      )
      (pin bidirectional line (at 17.78 7.62 180) (length 2.54)
        (name "PA13" (effects (font (size 1.27 1.27))))
        (number "36" (effects (font (size 1.27 1.27))))
        (alternate "I2C1_SCL" bidirectional line)
        (alternate "IR_OUT" bidirectional line)
        (alternate "SAI1_SD_B" bidirectional line)
        (alternate "SYS_JTMS-SWDIO" bidirectional line)
        (alternate "TIM16_CH1N" bidirectional line)
        (alternate "TIM4_CH3" bidirectional line)
        (alternate "USART3_CTS" bidirectional line)
        (alternate "USART3_NSS" bidirectional line)
      )
      (pin bidirectional line (at 17.78 5.08 180) (length 2.54)
        (name "PA14" (effects (font (size 1.27 1.27))))
        (number "37" (effects (font (size 1.27 1.27))))
        (alternate "I2C1_SDA" bidirectional line)
        (alternate "LPTIM1_OUT" bidirectional line)
        (alternate "SAI1_FS_B" bidirectional line)
        (alternate "SYS_JTCK-SWCLK" bidirectional line)
        (alternate "TIM1_BKIN" bidirectional line)
        (alternate "TIM8_CH2" bidirectional line)
        (alternate "USART2_TX" bidirectional line)
      )
      (pin bidirectional line (at 17.78 2.54 180) (length 2.54)
        (name "PA15" (effects (font (size 1.27 1.27))))
        (number "38" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_EXTI15" bidirectional line)
        (alternate "ADC2_EXTI15" bidirectional line)
        (alternate "I2C1_SCL" bidirectional line)
        (alternate "I2S3_WS" bidirectional line)
        (alternate "SPI1_NSS" bidirectional line)
        (alternate "SPI3_NSS" bidirectional line)
        (alternate "SYS_JTDI" bidirectional line)
        (alternate "TIM1_BKIN" bidirectional line)
        (alternate "TIM2_CH1" bidirectional line)
        (alternate "TIM2_ETR" bidirectional line)
        (alternate "TIM8_CH1" bidirectional line)
        (alternate "USART2_RX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 17.78 0) (length 2.54)
        (name "PC10" (effects (font (size 1.27 1.27))))
        (number "39" (effects (font (size 1.27 1.27))))
        (alternate "DAC1_EXTI10" bidirectional line)
        (alternate "DAC3_EXTI10" bidirectional line)
        (alternate "I2S3_CK" bidirectional line)
        (alternate "SPI3_SCK" bidirectional line)
        (alternate "TIM8_CH1N" bidirectional line)
        (alternate "USART3_TX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 7.62 0) (length 2.54)
        (name "PC15" (effects (font (size 1.27 1.27))))
        (number "4" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_EXTI15" bidirectional line)
        (alternate "ADC2_EXTI15" bidirectional line)
        (alternate "RCC_OSC32_OUT" bidirectional line)
      )
      (pin bidirectional line (at -15.24 15.24 0) (length 2.54)
        (name "PC11" (effects (font (size 1.27 1.27))))
        (number "40" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_EXTI11" bidirectional line)
        (alternate "ADC2_EXTI11" bidirectional line)
        (alternate "I2C3_SDA" bidirectional line)
        (alternate "SPI3_MISO" bidirectional line)
        (alternate "TIM8_CH2N" bidirectional line)
        (alternate "USART3_RX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -5.08 0) (length 2.54)
        (name "PB3" (effects (font (size 1.27 1.27))))
        (number "41" (effects (font (size 1.27 1.27))))
        (alternate "CRS_SYNC" bidirectional line)
        (alternate "I2S3_CK" bidirectional line)
        (alternate "SAI1_SCK_B" bidirectional line)
        (alternate "SPI1_SCK" bidirectional line)
        (alternate "SPI3_SCK" bidirectional line)
        (alternate "SYS_JTDO-SWO" bidirectional line)
        (alternate "TIM2_CH2" bidirectional line)
        (alternate "TIM3_ETR" bidirectional line)
        (alternate "TIM4_ETR" bidirectional line)
        (alternate "TIM8_CH1N" bidirectional line)
        (alternate "USART2_TX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -7.62 0) (length 2.54)
        (name "PB4" (effects (font (size 1.27 1.27))))
        (number "42" (effects (font (size 1.27 1.27))))
        (alternate "SAI1_MCLK_B" bidirectional line)
        (alternate "SPI1_MISO" bidirectional line)
        (alternate "SPI3_MISO" bidirectional line)
        (alternate "SYS_JTRST" bidirectional line)
        (alternate "TIM16_CH1" bidirectional line)
        (alternate "TIM17_BKIN" bidirectional line)
        (alternate "TIM3_CH1" bidirectional line)
        (alternate "TIM8_CH2N" bidirectional line)
        (alternate "UCPD1_CC2" bidirectional line)
        (alternate "USART2_RX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -10.16 0) (length 2.54)
        (name "PB5" (effects (font (size 1.27 1.27))))
        (number "43" (effects (font (size 1.27 1.27))))
        (alternate "I2C1_SMBA" bidirectional line)
        (alternate "I2C3_SDA" bidirectional line)
        (alternate "I2S3_SD" bidirectional line)
        (alternate "LPTIM1_IN1" bidirectional line)
        (alternate "SAI1_SD_B" bidirectional line)
        (alternate "SPI1_MOSI" bidirectional line)
        (alternate "SPI3_MOSI" bidirectional line)
        (alternate "TIM16_BKIN" bidirectional line)
        (alternate "TIM17_CH1" bidirectional line)
        (alternate "TIM3_CH2" bidirectional line)
        (alternate "TIM8_CH3N" bidirectional line)
        (alternate "USART2_CK" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -12.7 0) (length 2.54)
        (name "PB6" (effects (font (size 1.27 1.27))))
        (number "44" (effects (font (size 1.27 1.27))))
        (alternate "COMP4_OUT" bidirectional line)
        (alternate "LPTIM1_ETR" bidirectional line)
        (alternate "SAI1_FS_B" bidirectional line)
        (alternate "TIM16_CH1N" bidirectional line)
        (alternate "TIM4_CH1" bidirectional line)
        (alternate "TIM8_BKIN2" bidirectional line)
        (alternate "TIM8_CH1" bidirectional line)
        (alternate "TIM8_ETR" bidirectional line)
        (alternate "UCPD1_CC1" bidirectional line)
        (alternate "USART1_TX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -15.24 0) (length 2.54)
        (name "PB7" (effects (font (size 1.27 1.27))))
        (number "45" (effects (font (size 1.27 1.27))))
        (alternate "COMP3_OUT" bidirectional line)
        (alternate "I2C1_SDA" bidirectional line)
        (alternate "LPTIM1_IN2" bidirectional line)
        (alternate "SYS_PVD_IN" bidirectional line)
        (alternate "TIM17_CH1N" bidirectional line)
        (alternate "TIM3_CH4" bidirectional line)
        (alternate "TIM4_CH2" bidirectional line)
        (alternate "TIM8_BKIN" bidirectional line)
        (alternate "USART1_RX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -17.78 0) (length 2.54)
        (name "PB8" (effects (font (size 1.27 1.27))))
        (number "46" (effects (font (size 1.27 1.27))))
        (alternate "COMP1_OUT" bidirectional line)
        (alternate "FDCAN1_RX" bidirectional line)
        (alternate "I2C1_SCL" bidirectional line)
        (alternate "SAI1_CK1" bidirectional line)
        (alternate "SAI1_MCLK_A" bidirectional line)
        (alternate "TIM16_CH1" bidirectional line)
        (alternate "TIM1_BKIN" bidirectional line)
        (alternate "TIM4_CH3" bidirectional line)
        (alternate "TIM8_CH2" bidirectional line)
        (alternate "USART3_RX" bidirectional line)
      )
      (pin bidirectional line (at -15.24 -20.32 0) (length 2.54)
        (name "PB9" (effects (font (size 1.27 1.27))))
        (number "47" (effects (font (size 1.27 1.27))))
        (alternate "COMP2_OUT" bidirectional line)
        (alternate "DAC1_EXTI9" bidirectional line)
        (alternate "DAC3_EXTI9" bidirectional line)
        (alternate "FDCAN1_TX" bidirectional line)
        (alternate "I2C1_SDA" bidirectional line)
        (alternate "IR_OUT" bidirectional line)
        (alternate "SAI1_D2" bidirectional line)
        (alternate "SAI1_FS_A" bidirectional line)
        (alternate "TIM17_CH1" bidirectional line)
        (alternate "TIM1_CH3N" bidirectional line)
        (alternate "TIM4_CH4" bidirectional line)
        (alternate "TIM8_CH3" bidirectional line)
        (alternate "USART3_TX" bidirectional line)
      )
      (pin power_in line (at 5.08 45.72 270) (length 2.54)
        (name "VDD" (effects (font (size 1.27 1.27))))
        (number "48" (effects (font (size 1.27 1.27))))
      )
      (pin power_in line (at 2.54 -43.18 90) (length 2.54)
        (name "VSS" (effects (font (size 1.27 1.27))))
        (number "49" (effects (font (size 1.27 1.27))))
      )
      (pin bidirectional line (at -15.24 30.48 0) (length 2.54)
        (name "PF0" (effects (font (size 1.27 1.27))))
        (number "5" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN10" bidirectional line)
        (alternate "I2C2_SDA" bidirectional line)
        (alternate "I2S2_WS" bidirectional line)
        (alternate "RCC_OSC_IN" bidirectional line)
        (alternate "SPI2_NSS" bidirectional line)
        (alternate "TIM1_CH3N" bidirectional line)
      )
      (pin bidirectional line (at -15.24 27.94 0) (length 2.54)
        (name "PF1" (effects (font (size 1.27 1.27))))
        (number "6" (effects (font (size 1.27 1.27))))
        (alternate "ADC2_IN10" bidirectional line)
        (alternate "COMP3_INM" bidirectional line)
        (alternate "I2S2_CK" bidirectional line)
        (alternate "RCC_OSC_OUT" bidirectional line)
        (alternate "SPI2_SCK" bidirectional line)
      )
      (pin bidirectional line (at -15.24 35.56 0) (length 2.54)
        (name "PG10" (effects (font (size 1.27 1.27))))
        (number "7" (effects (font (size 1.27 1.27))))
        (alternate "DAC1_EXTI10" bidirectional line)
        (alternate "DAC3_EXTI10" bidirectional line)
        (alternate "RCC_MCO" bidirectional line)
      )
      (pin bidirectional line (at 17.78 40.64 180) (length 2.54)
        (name "PA0" (effects (font (size 1.27 1.27))))
        (number "8" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN1" bidirectional line)
        (alternate "ADC2_IN1" bidirectional line)
        (alternate "COMP1_INM" bidirectional line)
        (alternate "COMP1_OUT" bidirectional line)
        (alternate "COMP3_INP" bidirectional line)
        (alternate "RTC_TAMP2" bidirectional line)
        (alternate "SYS_WKUP1" bidirectional line)
        (alternate "TIM2_CH1" bidirectional line)
        (alternate "TIM2_ETR" bidirectional line)
        (alternate "TIM8_BKIN" bidirectional line)
        (alternate "TIM8_ETR" bidirectional line)
        (alternate "USART2_CTS" bidirectional line)
        (alternate "USART2_NSS" bidirectional line)
      )
      (pin bidirectional line (at 17.78 38.1 180) (length 2.54)
        (name "PA1" (effects (font (size 1.27 1.27))))
        (number "9" (effects (font (size 1.27 1.27))))
        (alternate "ADC1_IN2" bidirectional line)
        (alternate "ADC2_IN2" bidirectional line)
        (alternate "COMP1_INP" bidirectional line)
        (alternate "OPAMP1_VINP" bidirectional line)
        (alternate "OPAMP1_VINP_SEC" bidirectional line)
        (alternate "OPAMP3_VINP" bidirectional line)
        (alternate "OPAMP3_VINP_SEC" bidirectional line)
        (alternate "RTC_REFIN" bidirectional line)
        (alternate "TIM15_CH1N" bidirectional line)
        (alternate "TIM2_CH2" bidirectional line)
        (alternate "USART2_DE" bidirectional line)
        (alternate "USART2_RTS" bidirectional line)
      )
    )
  )
)

(no_connect (at 133.35 91.44) (uuid 60694280-f2fe-428e-bf2b-e6f21e5d711d))
(hierarchical_label "OSC_IN" (shape input) (at 100.33 91.44 180) (fields_autoplaced)
  (effects (font (size 1.27 1.27)) (justify right))
  (uuid 8a4d312a-68dd-4dbf-b402-9024df1f2c68)
)
(hierarchical_label "OSC_OUT" (shape input) (at 100.33 93.98 180) (fields_autoplaced)
  (effects (font (size 1.27 1.27)) (justify right))
  (uuid 0761ddd3-8392-4c37-9ada-195d1489b3ca)
)
(no_connect (at 133.35 93.98) (uuid 0190b951-a828-4d66-b3c7-d826247a6e99))
(symbol (lib_id "MCU_ST_STM32G4:STM32G431CBUx") (at 115.57 101.6 0) (unit 1)
  (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
  (uuid 70da3530-6e9d-46db-a71b-937355ee1452)
  (property "Reference" "U1" (at 120.0659 144.78 0)
    (effects (font (size 1.27 1.27)) (justify left))
  )
  (property "Value" "STM32G431CBUx" (at 120.0659 147.32 0)
    (effects (font (size 1.27 1.27)) (justify left))
  )
  (property "Footprint" "Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.15x5.15mm" (at 102.87 142.24 0)
    (effects (font (size 1.27 1.27)) (justify right) hide)
  )
  (property "Datasheet" "https://www.st.com/resource/en/datasheet/stm32g431cb.pdf" (at 115.57 101.6 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (pin "1" (uuid 2348b18d-fb1f-4883-b30c-23ed414dca2f))
  (pin "10" (uuid cdb9d6ce-dc7a-4ae7-ab7a-cbbee9d06513))
  (pin "11" (uuid 4c699b47-3b6e-46f7-a4b7-becd95707415))
  (pin "12" (uuid 3ea5227b-921b-4bcc-809a-db13d52df92f))
  (pin "13" (uuid fb675463-ab86-4d27-bdc9-342845a78d3e))
  (pin "14" (uuid e31670e7-c59d-401d-ac61-f5d3247d45a5))
  (pin "15" (uuid dd15aacb-51ca-441c-be88-285a5a84f4ad))
  (pin "16" (uuid 2f2f23aa-ef27-4cbb-bb56-d100edd6ba1b))
  (pin "17" (uuid 133ede3a-1de4-45a6-b5c4-8d930cf98dd2))
  (pin "18" (uuid f639f594-b1b6-4e58-92d8-912bc1b045ba))
  (pin "19" (uuid 8444973b-6e27-4072-b51e-a89c99617173))
  (pin "2" (uuid 187e4133-b972-4c2d-9507-462b0802a080))
  (pin "20" (uuid 77113ead-feb9-4c54-a049-7dc9313c8ab5))
  (pin "21" (uuid 7ab43ad6-79d6-4281-ac7b-44ee18ad269c))
  (pin "22" (uuid fa532dc1-fb64-4d7b-a388-fe951f2667b1))
  (pin "23" (uuid 72931423-94cc-4be9-b016-913598a4551f))
  (pin "24" (uuid fd47caac-38af-4666-abd4-beab95540d25))
  (pin "25" (uuid 1d21e9e6-0cc7-4501-a9e1-79f5556c00bd))
  (pin "26" (uuid d98d13ec-2115-4931-a541-aa256fc6b932))
  (pin "27" (uuid 8ec0f206-6a6b-491e-801b-28cdb6607422))
  (pin "28" (uuid ec9485a0-cd48-4d1e-b4e2-e19149106f8c))
  (pin "29" (uuid 8aa6fdd2-1eec-426c-b7cc-a91cb2e2dd42))
  (pin "3" (uuid be8a8d2d-28fa-4263-b69f-1373bc9e418d))
  (pin "30" (uuid c5bbb437-5410-49d7-aa87-2d974ecc9ba8))
  (pin "31" (uuid 9b9dd9fb-1e19-4ebf-b2aa-5e54c830f851))
  (pin "32" (uuid 57dcb808-e3a3-4bf1-a64c-ff5852a6fc75))
  (pin "33" (uuid 66637549-32a2-40ea-8eae-d6f92bea8b9d))
  (pin "34" (uuid 7ebac216-8855-47e1-96f0-56f1dd02c335))
  (pin "35" (uuid 22474e89-bf68-4770-8ca4-d83901b59da7))
  (pin "36" (uuid 7bc705f9-4a72-4a0f-8776-b42c259aef43))
  (pin "37" (uuid 402701b2-a06c-440f-91ed-2efd39479e9c))
  (pin "38" (uuid 65848429-c280-461b-ba32-fef066b58b2c))
  (pin "39" (uuid 521be910-774c-42bf-ba11-04afc67be68e))
  (pin "4" (uuid c2b68369-a4af-4c1b-be43-b10801845be9))
  (pin "40" (uuid 93945fd3-dd6a-4f06-9099-ed6dc743fc57))
  (pin "41" (uuid 820225cd-473c-406a-a906-d5b6a7400d90))
  (pin "42" (uuid bda77582-ea1f-4015-8a60-937756236e67))
  (pin "43" (uuid 1ede9e69-b81c-4018-8ba3-54794663365b))
  (pin "44" (uuid 3b177ecb-49c9-4113-9032-cbe1ecab5039))
  (pin "45" (uuid c7e992fa-001f-4cc1-ab81-0a11c1c49956))
  (pin "46" (uuid 33bf4937-d87a-4d54-8385-a9077f8730cc))
  (pin "47" (uuid 7227f316-90f3-45de-9ec8-51f408ff8feb))
  (pin "48" (uuid 25843827-91a5-4ea4-b216-e29df911295c))
  (pin "49" (uuid c0a13131-7ddb-494e-9b5b-88ffc4bdef3f))
  (pin "5" (uuid 21afac53-9075-4b24-a04b-5e4af01f875c))
  (pin "6" (uuid 2fe0926e-0a55-48c8-b388-fe388fa1e3ee))
  (pin "7" (uuid 18ee50f2-b669-43ed-a9ae-e3ad481407c8))
  (pin "8" (uuid 44d66e56-abb8-4b2d-a395-f8dcd40b6436))
  (pin "9" (uuid b296d392-27bb-423f-974e-38c69dbb8667))
  (instances
    (project "IR-HeatCam-G431-Demo"
      (path "/d7419abf-bd2c-48c5-bd92-239791049f9e"
        (reference "U1") (unit 1)
      )
    )
  )
)

"""))

print(kicad_obj)