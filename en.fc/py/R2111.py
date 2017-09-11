from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2111   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2111.x',
        MapIndex            = 100,
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
        'Sieg',                                 # 9
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
        Unknown_3A              = 100,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02320 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02320P._CP',             # 00
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6130,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -16740,
        Y                   = -3000,
        Z                   = -43910,
        Range               = 3000,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -22290,
        Y                   = -3000,
        Z                   = -15520,
        Range               = -16120,
        Unknown_10          = 0x0,
        Unknown_14          = 0xFFFFCFEA,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -65300,
        Y                   = -3000,
        Z                   = -120400,
        Range               = -78400,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFE33D8,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = -16670,
        TriggerZ            = -1970,
        TriggerY            = -43720,
        TriggerRange        = 1500,
        ActorX              = -16670,
        ActorZ              = -300,
        ActorY              = -43720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20680,
        TriggerZ            = -2009,
        TriggerY            = -44860,
        TriggerRange        = 1500,
        ActorX              = -20680,
        ActorZ              = -350,
        ActorY              = -44860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_17A",          # 00, 0
        "Function_1_192",          # 01, 1
        "Function_2_1F2",          # 02, 2
        "Function_3_51E",          # 03, 3
        "Function_4_68D",          # 04, 4
        "Function_5_6B0",          # 05, 5
        "Function_6_94C",          # 06, 6
        "Function_7_968",          # 07, 7
        "Function_8_A1B",          # 08, 8
        "Function_9_A85",          # 09, 9
    )


    def Function_0_17A(): pass

    label("Function_0_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_191")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_191")

    Return()

    # Function_0_17A end

    def Function_1_192(): pass

    label("Function_1_192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B4")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -16940, -1000, -44310, 135)

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C9")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFD0648, 0x3002C)
    OP_22(0x1C4, 0x1, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_192 end

    def Function_2_1F2(): pass

    label("Function_2_1F2")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(10562, -2000, -118830, 0)
    OP_6C(270000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14150, 1000, -123720, 0)
    SetChrPos(0x101, 13220, -2000, -128560, 0)
    SetChrPos(0x102, 13220, -2000, -128560, 0)
    SetChrPos(0x105, 13220, -2000, -128560, 0)
    SetChrPos(0x106, 13220, -2000, -128560, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_278():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_278)

    def lambda_288():
        OP_8E(0xFE, 0x2C06, 0xBB8, 0xFFFE7348, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_288)
    Sleep(1000)

    def lambda_2A8():
        OP_8E(0xFE, 0x334A, 0xFFFFF827, 0xFFFE3022, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A8)
    Sleep(500)

    def lambda_2C8():
        OP_8E(0xFE, 0x305C, 0xFFFFF876, 0xFFFE2BAE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C8)
    Sleep(500)

    def lambda_2E8():
        OP_8E(0xFE, 0x3642, 0xFFFFF808, 0xFFFE2BF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E8)
    Sleep(500)

    def lambda_308():
        OP_8E(0xFE, 0x3296, 0xFFFFF827, 0xFFFE282A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_308)
    WaitChrThread(0x106, 0x1)

    ChrTalk(    #0
        0x106,
        (
            "#052FDoes seem like it's homing\x01",
            "in on something...but...\x02\x03",

            "C'mon, are we really following\x01",
            "that thing? If this is your idea\x01",
            "of a joke, it's not funny!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C2():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C2)

    def lambda_3D0():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D0)
    TurnDirection(0x105, 0x106, 400)

    ChrTalk(    #1
        0x105,
        (
            "#049F#2PIt's not a joke.\x02\x03",

            "The matron and the children are\x01",
            "like family to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x106,
        (
            "#552FHmph... Fine, then.\x02\x03",

            "I thought you were yankin' my\x01",
            "chain, but...I guess I'll tag\x01",
            "along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#007F#5PGeez, why don't you say\x01",
            "what you REALLY think?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #4
        0x102,
        (
            "#012F#2PAll that aside, we need to get\x01",
            "going after Sieg.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    EventEnd(0x0)
    Return()

    # Function_2_1F2 end

    def Function_3_51E(): pass

    label("Function_3_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x437)

    def lambda_53A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_53A)

    def lambda_548():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_548)

    def lambda_556():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_556)

    def lambda_564():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_564)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -17250, 2000, -38520, 315)
    OP_22(0x197, 0x0, 0x64)

    def lambda_58D():
        OP_6D(-16010, 2000, -39760, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_58D)

    def lambda_5A5():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5A5)
    OP_97(0x8, 0xFFFFC162, 0xFFFF64C4, 0xFFFA81C0, 0x1F40, 0x1)
    OP_22(0x8C, 0x0, 0x64)
    OP_97(0x8, 0xFFFFC162, 0xFFFF64C4, 0xFFFA81C0, 0x1F40, 0x1)
    OP_97(0x8, 0xFFFFC162, 0xFFFF64C4, 0xFFFA81C0, 0x1F40, 0x1)

    def lambda_5F9():
        OP_8E(0x8, 0xFFFF7D10, 0x1388, 0xFFFF21DA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5F9)
    OP_22(0x8C, 0x0, 0x64)
    Sleep(2000)
    OP_69(0x1, 0x7D0)

    ChrTalk(    #5
        0x101,
        (
            "#580FIsn't that...the way to the\x01",
            "lighthouse...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#012FHmm... Let's go and check it out.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    SetChrFlags(0x8, 0x80)
    ClearMapFlags(0x2000000)

    label("loc_68C")

    Return()

    # Function_3_51E end

    def Function_4_68D(): pass

    label("Function_4_68D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AF")
    OP_97(0x8, 0xFFFFBDD4, 0xFFFF52EA, 0xFFFF15A0, 0x2328, 0x1)
    OP_48()
    Jump("Function_4_68D")

    label("loc_6AF")

    Return()

    # Function_4_68D end

    def Function_5_6B0(): pass

    label("Function_5_6B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_827")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74B")

    ChrTalk(    #7
        0x106,
        (
            "#050FWe don't exactly have the\x01",
            "time for this...\x02\x03",

            "Bah. What choice is there?\x01",
            "I hope at least Sieg knows\x01",
            "where he's going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_820")

    label("loc_74B")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #8
        0x106,
        (
            "#050FHey, where do you think you're\x01",
            "going?\x02\x03",

            "There's no time to just stop by\x01",
            "for a visit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B6():
        TurnDirection(0x105, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B6)

    def lambda_7C4():
        TurnDirection(0x101, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C4)
    TurnDirection(0x102, 0x106, 400)

    ChrTalk(    #9
        0x102,
        (
            "#012FThat's true.\x02\x03",

            "We have to have faith in Sieg\x01",
            "and stay on his trail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_820")

    Call(0, 6)
    Jump("loc_94B")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94B")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD")
    TurnDirection(0x106, 0x1, 400)

    ChrTalk(    #10
        0x106,
        (
            "#050FThere's no time to just stop by \x01",
            "for a visit...\x02\x03",

            "We need to get back to the\x01",
            "lighthouse and settle this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_947")

    label("loc_8BD")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #11
        0x106,
        (
            "#050FNow hold up a sec. You think now's\x01",
            "the time to just go and take a little\x01",
            "stroll?\x02\x03",

            "We need to get back to the lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_947")

    Call(0, 6)

    label("loc_94B")

    Return()

    # Function_5_6B0 end

    def Function_6_94C(): pass

    label("Function_6_94C")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_6_94C end

    def Function_7_968(): pass

    label("Function_7_968")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x36)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1A")
    EventBegin(0x1)
    TurnDirection(0x137, 0x0, 400)

    ChrTalk(    #12
        0x137,
        (
            "I'm sorry, but would you please go\x01",
            "to Manoria Village at once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x137,
        (
            "Urgent business awaits in Grancel,\x01",
            "does it not?\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A1A")

    Return()

    # Function_7_968 end

    def Function_8_A1B(): pass

    label("Function_8_A1B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #14
        (
            "\x07\x05East: Ruan - 374 selge\x01",
            "      Manoria Village - 63 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_A1B end

    def Function_9_A85(): pass

    label("Function_9_A85")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05South: Varenne Lighthouse - 70 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_A85 end

    SaveToFile()

Try(main)
