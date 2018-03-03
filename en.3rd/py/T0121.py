from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        'Rinon',                                # 9
        'Stella',                               # 10
        'Target Camera',                        # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT26/CH20789 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT26/CH20789P._CP',             # 02
    )

    DeclNpc(
        X                   = 3800,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -86130,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
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


    DeclActor(
        TriggerX            = 980,
        TriggerZ            = 0,
        TriggerY            = 118670,
        TriggerRange        = 1000,
        ActorX              = 980,
        ActorZ              = 1100,
        ActorY              = 118670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_146",          # 00, 0
        "Function_1_165",          # 01, 1
        "Function_2_16F",          # 02, 2
        "Function_3_185",          # 03, 3
        "Function_4_C31",          # 04, 4
        "Function_5_C8D",          # 05, 5
        "Function_6_D09",          # 06, 6
        "Function_7_D7D",          # 07, 7
    )


    def Function_0_146(): pass

    label("Function_0_146")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_164")

    Return()

    # Function_0_146 end

    def Function_1_165(): pass

    label("Function_1_165")

    OP_B1("T0121_n")
    Return()

    # Function_1_165 end

    def Function_2_16F(): pass

    label("Function_2_16F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_184")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_16F")

    label("loc_184")

    Return()

    # Function_2_16F end

    def Function_3_185(): pass

    label("Function_3_185")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(5930, 0, 2009, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 3480, 0, -260, 0)
    SetChrPos(0x155, 5120, 0, -7500, 0)
    OP_9F(0x155, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_20B():
        OP_6D(5930, 0, -2009, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_20B)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x155, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)

    ChrTalk(    #0
        0x155,
        "#291F#1PRinoooooon!\x02",
    )

    CloseMessageWindow()

    def lambda_25B():
        OP_6D(4800, 0, 2000, 2500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_25B)

    def lambda_273():
        OP_6C(40000, 2500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_273)

    def lambda_283():
        OP_6B(2900, 2500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_283)
    OP_62(0x155, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_2AA():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFF5D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2AA)

    def lambda_2C5():

        label("loc_2C5")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_2C5")

    QueueWorkItem2(0x10, 2, lambda_2C5)

    def lambda_2D6():

        label("loc_2D6")

        TurnDirection(0xFE, 0x155, 400)
        OP_48()
        Jump("loc_2D6")

    QueueWorkItem2(0x11, 2, lambda_2D6)
    WaitChrThread(0x155, 0x1)

    def lambda_2EC():
        OP_8E(0xFE, 0x19F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2EC)
    WaitChrThread(0x155, 0x1)

    def lambda_30C():
        OP_8E(0xFE, 0x19F0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_30C)
    WaitChrThread(0x155, 0x1)

    def lambda_32C():
        OP_8E(0xFE, 0x12C0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_32C)
    WaitChrThread(0x155, 0x1)

    ChrTalk(    #1
        0x10,
        (
            "#6PHeya, Estelle! Take it you're here to look\x01",
            "at sneakers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x155,
        "#290F#11PYou bet! Are there any new ones in?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "#6PWe sure do! ...Have nothing new at all.\x01",
            "Sorry, kiddo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#6POur next delivery's due...the 16th,\x01",
            "if my schedule's any indication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x155,
        "#296F#11PThe 16th? That's only a week away!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x155, 90, 500)
    Sleep(300)

    ChrTalk(    #6
        0x155,
        "#292F#5POne more week... Just one more week...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x11,
        "#6PUmm... Estelle?\x02",
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x155, 0x11, 500)

    ChrTalk(    #8
        0x155,
        "#293F#5POh, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        "#6PHeehee. You came at JUST the right time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#6PI've just found some clothes that I think would\x01",
            "look SO cute on you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#6PToday will be the day you finally get to realize\x01",
            "your potential as a girl with some nice clothes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x155,
        (
            "#292F#5PBut I can't wear them now.\x02\x03",

            "#295FI'm going bug catching! They'll just get dirty!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x155,
        (
            "#293F#5PWait! I'm going bug catching!\x02\x03",

            "#296FI almost forgot because I was thinkin'\x01",
            "about sneakers...\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x155,
        "#290F#5PBack to getting ingredients!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Go and See Elissa First\x01",      # 0
            "Hurry to Tio's House\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A06")

    ChrTalk(    #15
        0x155,
        (
            "#291F#5PTime to go see Elissa!\x02\x03",

            "Full speed ahead!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_821():
        OP_6D(5930, 0, -2009, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_821)

    def lambda_839():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_839)

    def lambda_849():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_849)
    OP_62(0x155, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_86B():
        OP_8E(0xFE, 0x19F0, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_86B)
    WaitChrThread(0x155, 0x1)

    def lambda_88B():
        OP_8E(0xFE, 0x19F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_88B)
    WaitChrThread(0x155, 0x1)

    def lambda_8AB():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFF5D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_8AB)
    WaitChrThread(0x155, 0x1)

    def lambda_8CB():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFE2B4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_8CB)
    Sleep(500)

    def lambda_8EB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_8EB)
    WaitChrThread(0x155, 0x1)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #16
        0x10,
        (
            "As if that little bundle of energy didn't\x01",
            "already have enough to power an airship.\x01",
            "Now she's got more than ever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "#6PI wonder what's gotten her so fired up.\x02",
    )

    CloseMessageWindow()

    def lambda_9E2():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_9E2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C30")

    label("loc_A06")


    ChrTalk(    #18
        0x155,
        (
            "#292F#5PTime to go meet up with Tio!\x02\x03",

            "#291FI've gotta hurry!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A4E():
        OP_6D(5930, 0, -2009, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_A4E)

    def lambda_A66():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A66)

    def lambda_A76():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A76)
    OP_62(0x155, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_A98():
        OP_8E(0xFE, 0x19F0, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_A98)
    WaitChrThread(0x155, 0x1)

    def lambda_AB8():
        OP_8E(0xFE, 0x19F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_AB8)
    WaitChrThread(0x155, 0x1)

    def lambda_AD8():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFF5D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_AD8)
    WaitChrThread(0x155, 0x1)

    def lambda_AF8():
        OP_8E(0xFE, 0x1400, 0x0, 0xFFFFE2B4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_AF8)
    Sleep(500)

    def lambda_B18():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_B18)
    WaitChrThread(0x155, 0x1)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #19
        0x10,
        (
            "As if that little bundle of energy didn't\x01",
            "already have enough to power an airship.\x01",
            "Now she's got more than ever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        "#6PI wonder what's gotten her so fired up.\x02",
    )

    CloseMessageWindow()

    def lambda_C0F():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_C0F)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_C30")

    Return()

    # Function_3_185 end

    def Function_4_C31(): pass

    label("Function_4_C31")

    OP_82(0x81, 0x2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #21
        "\x07\x05Received \x1F\x62\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_E3(0x4, 0x10, 0x1)
    OP_3E(0x362, 1)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_4_C31 end

    def Function_5_C8D(): pass

    label("Function_5_C8D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 4240, 0, 108560, 0)

    def lambda_CB4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CB4)

    def lambda_CC6():
        OP_8E(0xFE, 0xF6E, 0x0, 0x1AFC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CC6)
    WaitChrThread(0xFE, 0x2)
    OP_8E(0xFE, 0x456, 0x0, 0x1B94A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3F2, 0x0, 0x1BD28, 0x7D0, 0x0)
    Return()

    # Function_5_C8D end

    def Function_6_D09(): pass

    label("Function_6_D09")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 4240, 0, 108560, 0)

    def lambda_D35():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D35)

    def lambda_D47():
        OP_8E(0xFE, 0xF6E, 0x0, 0x1AFC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D47)
    WaitChrThread(0xFE, 0x2)
    OP_8E(0xFE, 0x316, 0x0, 0x1B79C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_D09 end

    def Function_7_D7D(): pass

    label("Function_7_D7D")

    Sleep(1500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 4240, 0, 108560, 0)

    def lambda_DA9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA9)

    def lambda_DBB():
        OP_8E(0xFE, 0xF6E, 0x0, 0x1AFC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DBB)
    WaitChrThread(0xFE, 0x2)
    OP_8E(0xFE, 0x8E8, 0x0, 0x1B652, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_7_D7D end

    SaveToFile()

Try(main)
