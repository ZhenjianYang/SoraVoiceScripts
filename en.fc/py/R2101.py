from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2101.x',
        MapIndex            = 100,
        MapDefaultBGM       = "ed60020",
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
        'Manoria Village',                      # 10
        'Varenne Lighthouse',                   # 11
        'Krone Trail',                          # 12
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
        'ED6_DT09/CH10160 ._CH',             # 01
        'ED6_DT09/CH10161 ._CH',             # 02
        'ED6_DT09/CH10450 ._CH',             # 03
        'ED6_DT09/CH10451 ._CH',             # 04
        'ED6_DT09/CH10220 ._CH',             # 05
        'ED6_DT09/CH10221 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02320P._CP',             # 00
        'ED6_DT09/CH10160P._CP',             # 01
        'ED6_DT09/CH10161P._CP',             # 02
        'ED6_DT09/CH10450P._CP',             # 03
        'ED6_DT09/CH10451P._CP',             # 04
        'ED6_DT09/CH10220P._CP',             # 05
        'ED6_DT09/CH10221P._CP',             # 06
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

    DeclNpc(
        X                   = 13030,
        Z                   = -2070,
        Y                   = -137400,
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

    DeclNpc(
        X                   = -72540,
        Z                   = -1880,
        Y                   = -134520,
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

    DeclNpc(
        X                   = -18980,
        Z                   = -2000,
        Y                   = 6950,
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


    DeclMonster(
        X                   = -9560,
        Z                   = -2080,
        Y                   = -65670,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6390,
        Z                   = -2020,
        Y                   = -101440,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41930,
        Z                   = -1980,
        Y                   = -61650,
        Unknown_0C          = 180,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -75520,
        Z                   = -1990,
        Y                   = -83680,
        Unknown_0C          = 180,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
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
        X                   = -80580,
        Y                   = -3000,
        Z                   = -110630,
        Range               = -67150,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFE4666,
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
        "Function_0_27A",          # 00, 0
        "Function_1_292",          # 01, 1
        "Function_2_2FB",          # 02, 2
        "Function_3_622",          # 03, 3
        "Function_4_7CD",          # 04, 4
        "Function_5_7F0",          # 05, 5
        "Function_6_A8C",          # 06, 6
        "Function_7_AA8",          # 07, 7
        "Function_8_B5B",          # 08, 8
        "Function_9_BC5",          # 09, 9
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_291")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_291")

    Return()

    # Function_0_27A end

    def Function_1_292(): pass

    label("Function_1_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B4")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -16940, -1000, -44310, 135)

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0x41, 0x64, 0x82, 0x0, 0x0)

    label("loc_2D2")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFD0648, 0x3002C)
    OP_22(0x1C4, 0x1, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_292 end

    def Function_2_2FB(): pass

    label("Function_2_2FB")

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

    def lambda_37C():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_37C)

    def lambda_38C():
        OP_8E(0xFE, 0x2C06, 0xBB8, 0xFFFE7348, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_38C)
    Sleep(1000)

    def lambda_3AC():
        OP_8E(0xFE, 0x334A, 0xFFFFF827, 0xFFFE3022, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3AC)
    Sleep(500)

    def lambda_3CC():
        OP_8E(0xFE, 0x305C, 0xFFFFF876, 0xFFFE2BAE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CC)
    Sleep(500)

    def lambda_3EC():
        OP_8E(0xFE, 0x3642, 0xFFFFF808, 0xFFFE2BF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EC)
    Sleep(500)

    def lambda_40C():
        OP_8E(0xFE, 0x3296, 0xFFFFF827, 0xFFFE282A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_40C)
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

    def lambda_4C6():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C6)

    def lambda_4D4():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D4)
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
            "#050FHmph... Fine, then.\x02\x03",

            "I thought you were yankin' my\x01",
            "chain, but...I guess I'll tag\x01",
            "along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#007F#1PGeez, why don't you say\x01",
            "what you REALLY think?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #4
        0x102,
        (
            "#012F#4PAll that aside, we need to get\x01",
            "going after Sieg.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    EventEnd(0x0)
    Return()

    # Function_2_2FB end

    def Function_3_622(): pass

    label("Function_3_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CC")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x437)
    OP_28(0x3E, 0x1, 0x10)

    def lambda_644():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_644)

    def lambda_652():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_652)

    def lambda_660():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_660)

    def lambda_66E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_66E)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -17250, 2000, -38520, 315)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05I can hear his cries from here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_6E0():
        OP_6D(-16010, 2000, -39760, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6E0)

    def lambda_6F8():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_6F8)
    OP_97(0x8, 0xFFFFC162, 0xFFFF64C4, 0xFFFA81C0, 0x1F40, 0x1)
    OP_97(0x8, 0xFFFFC162, 0xFFFF64C4, 0xFFFA81C0, 0x1F40, 0x1)
    OP_97(0x8, 0xFFFFC162, 0xFFFF64C4, 0xFFFA81C0, 0x1F40, 0x1)

    def lambda_747():
        OP_8E(0x8, 0xFFFF7D10, 0x1388, 0xFFFF21DA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_747)
    Sleep(2000)
    OP_69(0x1, 0x7D0)

    ChrTalk(    #6
        0x101,
        "#004FWas that what I think it was...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#012FYeah... Let's go and check it out.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    SetChrFlags(0x8, 0x80)
    ClearMapFlags(0x2000000)

    label("loc_7CC")

    Return()

    # Function_3_622 end

    def Function_4_7CD(): pass

    label("Function_4_7CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EF")
    OP_97(0x8, 0xFFFFBDD4, 0xFFFF52EA, 0xFFFF15A0, 0x2328, 0x1)
    OP_48()
    Jump("Function_4_7CD")

    label("loc_7EF")

    Return()

    # Function_4_7CD end

    def Function_5_7F0(): pass

    label("Function_5_7F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_967")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B")

    ChrTalk(    #8
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
    Jump("loc_960")

    label("loc_88B")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #9
        0x106,
        (
            "#050FHey, where do you think you're\x01",
            "going?\x02\x03",

            "There's no time to just stop by\x01",
            "for a visit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F6():
        TurnDirection(0x105, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8F6)

    def lambda_904():
        TurnDirection(0x101, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_904)
    TurnDirection(0x102, 0x106, 400)

    ChrTalk(    #10
        0x102,
        (
            "#012FThat's true.\x02\x03",

            "We have to have faith in Sieg\x01",
            "and stay on his trail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_960")

    Call(0, 6)
    Jump("loc_A8B")

    label("loc_967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8B")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FD")
    TurnDirection(0x106, 0x1, 400)

    ChrTalk(    #11
        0x106,
        (
            "#050FThere's no time to just stop by \x01",
            "for a visit...\x02\x03",

            "We need to get back to the\x01",
            "lighthouse and settle this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A87")

    label("loc_9FD")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #12
        0x106,
        (
            "#050FNow hold up a sec. You think now's\x01",
            "the time to just go and take a little\x01",
            "stroll?\x02\x03",

            "We need to get back to the lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A87")

    Call(0, 6)

    label("loc_A8B")

    Return()

    # Function_5_7F0 end

    def Function_6_A8C(): pass

    label("Function_6_A8C")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_6_A8C end

    def Function_7_AA8(): pass

    label("Function_7_AA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x36)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5A")
    EventBegin(0x1)
    TurnDirection(0x137, 0x0, 400)

    ChrTalk(    #13
        0x137,
        (
            "I'm sorry, but would you please go\x01",
            "to Manoria Village at once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
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

    label("loc_B5A")

    Return()

    # Function_7_AA8 end

    def Function_8_B5B(): pass

    label("Function_8_B5B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
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

    # Function_8_B5B end

    def Function_9_BC5(): pass

    label("Function_9_BC5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05South: Varenne Lighthouse - 70 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_BC5 end

    SaveToFile()

Try(main)
