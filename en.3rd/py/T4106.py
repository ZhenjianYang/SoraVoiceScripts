from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4106   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4106.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Man in Black',                         # 9
        'Man in Black',                         # 10
        'Target Camera',                        # 11
        'Grancel - East Block',                 # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01010 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT27/CH03460 ._CH',             # 07
        'ED6_DT26/CH20686 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01010P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT27/CH03460P._CP',             # 07
        'ED6_DT26/CH20686P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51050,
        Z                   = 0,
        Y                   = 83440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 56800,
        TriggerZ            = 250,
        TriggerY            = 136940,
        TriggerRange        = 800,
        ActorX              = 58770,
        ActorZ              = 1750,
        ActorY              = 137000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53710,
        TriggerZ            = 250,
        TriggerY            = 137720,
        TriggerRange        = 800,
        ActorX              = 53710,
        ActorZ              = 2450,
        ActorY              = 137720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71160,
        TriggerZ            = -10000,
        TriggerY            = 151550,
        TriggerRange        = 800,
        ActorX              = 71160,
        ActorZ              = -8500,
        ActorY              = 151550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_207",          # 01, 1
        "Function_2_21A",          # 02, 2
        "Function_3_230",          # 03, 3
        "Function_4_231",          # 04, 4
        "Function_5_585",          # 05, 5
        "Function_6_694",          # 06, 6
        "Function_7_7E3",          # 07, 7
        "Function_8_8D3",          # 08, 8
        "Function_9_99F",          # 09, 9
        "Function_10_9BA",         # 0A, 10
        "Function_11_A8C",         # 0B, 11
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_206")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_206")

    Return()

    # Function_0_1DE end

    def Function_1_207(): pass

    label("Function_1_207")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x23005F)
    Return()

    # Function_1_207 end

    def Function_2_21A(): pass

    label("Function_2_21A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_21A")

    label("loc_22F")

    Return()

    # Function_2_21A end

    def Function_3_230(): pass

    label("Function_3_230")

    Return()

    # Function_3_230 end

    def Function_4_231(): pass

    label("Function_4_231")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(49660, 0, 123640, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(328000, 0)
    OP_6E(302, 0)
    SetChrPos(0x103, 51820, 0, 105560, 0)
    SetChrPos(0x151, 50340, 0, 107960, 0)
    SetChrFlags(0x151, 0x40)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, 51660, 0, 104060, 0)
    SetChrPos(0x11, 50520, 0, 103100, 0)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x11, 8)

    def lambda_2E7():
        OP_6B(3400, 7000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E7)

    def lambda_2F7():
        OP_6E(262, 7000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F7)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_311():
        OP_8E(0xFE, 0xC4A4, 0x0, 0x241F8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_311)
    Sleep(10)

    def lambda_331():
        OP_8E(0xFE, 0xCA6C, 0x0, 0x23898, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_331)
    Sleep(2000)

    def lambda_351():
        OP_8E(0xFE, 0xC9CC, 0x0, 0x232BC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_351)
    Sleep(10)

    def lambda_371():
        OP_8E(0xFE, 0xC558, 0x0, 0x22EFC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_371)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x151, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_6D(58980, 0, 142640, 0)
    OP_67(0, 6410, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(240000, 0)
    OP_6E(262, 0)
    SetChrPos(0x151, 51700, 0, 139060, 45)
    SetChrPos(0x103, 51200, 0, 134820, 0)
    SetChrPos(0x10, 51500, 0, 133460, 0)
    SetChrPos(0x11, 50360, 0, 132480, 0)
    Sleep(500)

    def lambda_432():
        OP_6D(57580, 0, 143960, 6000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_432)

    def lambda_44A():
        OP_6C(210000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_44A)
    FadeToBright(1000, 0)
    OP_43(0x151, 0x3, 0x0, 0x5)
    Sleep(500)
    OP_43(0x103, 0x3, 0x0, 0x6)
    Sleep(4000)
    OP_43(0x10, 0x3, 0x0, 0x7)
    OP_43(0x11, 0x3, 0x0, 0x8)
    Sleep(2000)

    def lambda_48E():
        OP_6D(58000, -3000, 160020, 2500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_48E)
    WaitChrThread(0x12, 0x0)
    Sleep(2000)
    Fade(500)
    OP_6D(58980, -2250, 151240, 0)
    Sleep(6600)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_4E2():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4E2)
    Sleep(200)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_50C():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_50C)
    Sleep(600)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)

    def lambda_529():
        OP_8E(0xFE, 0xE90C, 0x0, 0x22380, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_529)
    Sleep(200)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_553():
        OP_8E(0xFE, 0xE4C0, 0x0, 0x22560, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_553)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_231 end

    def Function_5_585(): pass

    label("Function_5_585")


    def lambda_58B():
        OP_8E(0xFE, 0xD5AC, 0x0, 0x22EFC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_58B)
    WaitChrThread(0x151, 0x1)

    def lambda_5AB():
        OP_8E(0xFE, 0xE510, 0x0, 0x22EFC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5AB)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 180, 500)
    Sleep(1000)
    OP_8C(0x151, 0, 500)
    Sleep(1200)

    def lambda_5E3():
        OP_8E(0xFE, 0xE7CC, 0xFFFFF448, 0x26340, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5E3)
    WaitChrThread(0x151, 0x1)
    SetChrPos(0x151, 59700, -3000, 149960, 0)
    Sleep(6800)

    def lambda_619():
        OP_8F(0xFE, 0xEFD8, 0xFFFFF448, 0x249F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_619)
    WaitChrThread(0x151, 0x1)

    def lambda_639():
        OP_8E(0xFE, 0xEFD8, 0xFFFFF448, 0x2579C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_639)
    WaitChrThread(0x151, 0x1)

    def lambda_659():
        OP_8F(0xFE, 0xE8D0, 0xFFFFF448, 0x2579C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_659)
    WaitChrThread(0x151, 0x1)

    def lambda_679():
        OP_8E(0xFE, 0xE8D0, 0x0, 0x22E5C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_679)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_5_585 end

    def Function_6_694(): pass

    label("Function_6_694")


    def lambda_69A():
        OP_8E(0xFE, 0xC8F0, 0x0, 0x21E1C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_69A)
    WaitChrThread(0x103, 0x1)

    def lambda_6BA():
        OP_8E(0xFE, 0xD200, 0x0, 0x22984, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BA)
    WaitChrThread(0x103, 0x1)

    def lambda_6DA():
        OP_8E(0xFE, 0xDC14, 0x0, 0x22984, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DA)
    WaitChrThread(0x103, 0x1)

    def lambda_6FA():
        OP_8E(0xFE, 0xE510, 0x0, 0x2358C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6FA)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 180, 500)
    Sleep(400)
    OP_8C(0x103, 0, 500)
    Sleep(200)

    def lambda_732():
        OP_8E(0xFE, 0xE7CC, 0xFFFFF448, 0x26340, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_732)
    WaitChrThread(0x103, 0x1)
    SetChrPos(0x103, 59700, -3000, 149960, 0)
    Sleep(6500)

    def lambda_768():
        OP_8F(0xFE, 0xEFD8, 0xFFFFF448, 0x249F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_768)
    WaitChrThread(0x103, 0x1)

    def lambda_788():
        OP_8E(0xFE, 0xEFD8, 0xFFFFF448, 0x2579C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_788)
    WaitChrThread(0x103, 0x1)

    def lambda_7A8():
        OP_8F(0xFE, 0xE4C0, 0xFFFFF448, 0x2579C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A8)
    WaitChrThread(0x103, 0x1)

    def lambda_7C8():
        OP_8E(0xFE, 0xE4C0, 0x0, 0x22E5C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C8)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_6_694 end

    def Function_7_7E3(): pass

    label("Function_7_7E3")


    def lambda_7E9():
        OP_8E(0xFE, 0xC92C, 0x0, 0x21F20, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7E9)
    WaitChrThread(0x10, 0x1)

    def lambda_809():
        OP_8E(0xFE, 0xD73C, 0x0, 0x22B64, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_809)
    WaitChrThread(0x10, 0x1)

    def lambda_829():
        OP_8E(0xFE, 0xE3E4, 0x0, 0x22B64, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_829)
    WaitChrThread(0x10, 0x1)

    def lambda_849():
        OP_8E(0xFE, 0xE90C, 0x0, 0x2308C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_849)
    WaitChrThread(0x10, 0x1)

    def lambda_869():
        OP_8E(0xFE, 0xE90C, 0xFFFFF448, 0x26200, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_869)
    WaitChrThread(0x10, 0x1)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 45, 500)
    Sleep(500)
    OP_8C(0x10, 315, 500)
    Sleep(500)
    OP_8C(0x10, 0, 500)
    Sleep(500)
    Return()

    # Function_7_7E3 end

    def Function_8_8D3(): pass

    label("Function_8_8D3")


    def lambda_8D9():
        OP_8E(0xFE, 0xC4B8, 0x0, 0x22100, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D9)
    WaitChrThread(0x11, 0x1)

    def lambda_8F9():
        OP_8E(0xFE, 0xCF08, 0x0, 0x22880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8F9)
    WaitChrThread(0x11, 0x1)

    def lambda_919():
        OP_8E(0xFE, 0xE038, 0x0, 0x22880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_919)
    WaitChrThread(0x11, 0x1)

    def lambda_939():
        OP_8E(0xFE, 0xE4C0, 0x0, 0x22D6C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_939)
    WaitChrThread(0x11, 0x1)

    def lambda_959():
        OP_8E(0xFE, 0xE4C0, 0xFFFFF448, 0x25FF8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_959)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 7)
    SetChrSubChip(0x11, 0)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_8_8D3 end

    def Function_9_99F(): pass

    label("Function_9_99F")

    Sleep(2000)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    Return()

    # Function_9_99F end

    def Function_10_9BA(): pass

    label("Function_10_9BA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Rolent\x01",
            "⇒ To Zeiss\x01",
            "⇒ To Calvard Republic\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #1
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_9BA end

    def Function_11_A8C(): pass

    label("Function_11_A8C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_A8C end

    SaveToFile()

Try(main)
