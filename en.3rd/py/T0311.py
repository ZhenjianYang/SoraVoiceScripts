from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0311   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Joshua',                               # 9
        'Target Camera',                        # 10
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
        'ED6_DT07/CH02750 ._CH',             # 00
        'ED6_DT06/CH20033 ._CH',             # 01
        'ED6_DT26/CH20338 ._CH',             # 02
        'ED6_DT26/CH20320 ._CH',             # 03
        'ED6_DT26/CH20787 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02750P._CP',             # 00
        'ED6_DT06/CH20033P._CP',             # 01
        'ED6_DT26/CH20338P._CP',             # 02
        'ED6_DT26/CH20320P._CP',             # 03
        'ED6_DT26/CH20787P._CP',             # 04
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
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


    ScpFunction(
        "Function_0_112",          # 00, 0
        "Function_1_150",          # 01, 1
        "Function_2_15B",          # 02, 2
        "Function_3_748",          # 03, 3
    )


    def Function_0_112(): pass

    label("Function_0_112")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_13D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_14F")

    label("loc_13D")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_14F")

    Return()

    # Function_0_112 end

    def Function_1_150(): pass

    label("Function_1_150")

    OP_78(0x8C, 0x8C, 0xB4)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    Return()

    # Function_1_150 end

    def Function_2_15B(): pass

    label("Function_2_15B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_22(0x11C, 0x0, 0x64)
    Sleep(10000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0 op#A op#5
        "\x18\x07\x00#35A#40WThe first week...\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(100)
    OP_23(0x11C)
    Sleep(1000)
    Sleep(800)
    SetChrName("Voice")

    AnonymousTalk(    #1
        "\x07\x05#40WWell, hello there.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Voice")

    AnonymousTalk(    #2
        (
            "\x07\x05#40WThere's no need to be so afraid.\x01",
            "I am but a humble magician.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Voice")

    AnonymousTalk(    #3
        "\x07\x05#40WI will heal your broken heart for you.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Voice")

    AnonymousTalk(    #4
        (
            "\x07\x05#40WProvided, of course...#500W\x01",
            "#40WI am compensated.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    SetChrPos(0x101, 8900, 0, 68780, 180)
    SetChrPos(0x10, 8550, 500, 67500, 270)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x1)
    OP_71(0x405, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_6F(0xA, 60)
    OP_6D(9420, 0, 68840, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    OP_1D(0xB2)
    Sleep(500)

    def lambda_3A3():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3A3)

    def lambda_3B3():
        OP_67(0, 5440, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3B3)
    FadeToBright(5000, 0)
    OP_0D()

    ChrTalk(    #5
        0x10,
        (
            "#303F#4P#40WUgh... Guh...\x02\x03",

            "Ugh... #3S#20WGaaaaaah!\x02",
        )
    )

    Sleep(500)

    def lambda_411():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_411)
    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#292F#5PJ-Joshua?! Are you okay?!\x02\x03",

            "#293FOh, your temperature's gone up again!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47F():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_47F)
    Sleep(1000)

    ChrTalk(    #7
        0x101,
        (
            "#292F#5PStay still!\x02\x03",

            "#295FWhere's a towel...? Where's a toweeel...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 500)
    Sleep(300)

    ChrTalk(    #8
        0x101,
        (
            "#294F#5PWait a sec, okay? I'll be right back with\x01",
            "some water!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_548():
        OP_8E(0xFE, 0x14AA, 0x0, 0x10CAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_548)
    WaitChrThread(0x101, 0x1)

    def lambda_568():
        OP_8E(0xFE, 0xBD6, 0x0, 0x10252, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_568)
    WaitChrThread(0x101, 0x1)
    OP_22(0x6, 0x0, 0x64)
    OP_63(0x101)

    def lambda_590():
        OP_8E(0xFE, 0xB7C, 0x0, 0xFBF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_590)

    def lambda_5AB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AB)
    WaitChrThread(0x101, 0x1)

    def lambda_5C2():
        OP_6B(2700, 10000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5C2)

    def lambda_5D2():
        OP_6D(9910, 0, 69150, 10000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5D2)
    Sleep(3000)

    ChrTalk(    #9 op#A
        0x10,
        (
            "#307F#11P#40W#26AKarin, I...\x02\x03",

            "#60W#18AI'm...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x18\x07\x0C#40WAll I could hear in my head during those days\x01",
            "were the same words repeating endlessly like\x01",
            "a broken record...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x18\x07\x0C#40WYet somehow, I had no idea who was saying\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #12
        "\x18\x07\x0C#40WAll I knew was that...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_15B end

    def Function_3_748(): pass

    label("Function_3_748")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(147950, 0, 146040, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 148030, 500, 144900, 180)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    SetChrPos(0x101, 145600, 100, 145350, 90)
    OP_6F(0x0, 15)
    OP_70(0x0, 0xF)
    SoundLoad(390)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(3000)
    SetChrSubChip(0x10, 1)
    Sleep(200)
    SetChrSubChip(0x10, 2)
    Sleep(200)
    SetChrSubChip(0x10, 10)
    Sleep(500)

    ChrTalk(    #13
        0x10,
        (
            "#1676F#11PI swear... Why does she do this every single\x01",
            "night?\x02\x03",

            "#1675FI wish she'd mind her own business...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_22(0x186, 0x0, 0x64)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x1)
    SetChrPos(0x10, 146350, 0, 144240, 270)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 400)
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)
    OP_63(0x101)

    def lambda_909():
        OP_8E(0xFE, 0x23A64, 0x0, 0x2350A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_909)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_22(0x186, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 2)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, 147790, 350, 145320, 270)
    SetChrPos(0x10, 146220, 0, 144900, 90)
    OP_62(0x101, 0xFFFFFED4, 1300, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_8C(0x10, 225, 400)

    def lambda_9B0():
        OP_8E(0xFE, 0x232D0, 0x0, 0x22876, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9B0)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 180, 500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_9E1():
        OP_8E(0xFE, 0x23258, 0x0, 0x220F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9E1)

    def lambda_9FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9FC)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_748 end

    SaveToFile()

Try(main)
