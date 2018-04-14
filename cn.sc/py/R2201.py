from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2201   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2201.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60029",
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
        '飞球',                                 # 9
        '飞船',                                 # 10
        '飞船',                                 # 11
        '乔丝特',                               # 12
        '吉尔',                                 # 13
        '多伦',                                 # 14
        '玛诺利亚村方向',                       # 15
        '卢安方向',                             # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT09/CH10160 ._CH',             # 00
        'ED6_DT09/CH10161 ._CH',             # 01
        'ED6_DT09/CH10450 ._CH',             # 02
        'ED6_DT09/CH10451 ._CH',             # 03
        'ED6_DT09/CH10220 ._CH',             # 04
        'ED6_DT09/CH10221 ._CH',             # 05
        'ED6_DT09/CH10470 ._CH',             # 06
        'ED6_DT09/CH10471 ._CH',             # 07
        'ED6_DT09/CH10480 ._CH',             # 08
        'ED6_DT09/CH10481 ._CH',             # 09
        'ED6_DT09/CH10160 ._CH',             # 0A
        'ED6_DT09/CH10161 ._CH',             # 0B
        'ED6_DT09/CH10460 ._CH',             # 0C
        'ED6_DT09/CH10461 ._CH',             # 0D
        'ED6_DT27/CH03100 ._CH',             # 0E
        'ED6_DT07/CH02120 ._CH',             # 0F
        'ED6_DT07/CH02110 ._CH',             # 10
        'ED6_DT26/CH20390 ._CH',             # 11
        'ED6_DT26/CH20389 ._CH',             # 12
        'ED6_DT26/CH20388 ._CH',             # 13
        'ED6_DT26/CH20391 ._CH',             # 14
        'ED6_DT26/CH20407 ._CH',             # 15
        'ED6_DT09/CH11030 ._CH',             # 16
        'ED6_DT09/CH11031 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT09/CH10160P._CP',             # 00
        'ED6_DT09/CH10161P._CP',             # 01
        'ED6_DT09/CH10450P._CP',             # 02
        'ED6_DT09/CH10451P._CP',             # 03
        'ED6_DT09/CH10220P._CP',             # 04
        'ED6_DT09/CH10221P._CP',             # 05
        'ED6_DT09/CH10470P._CP',             # 06
        'ED6_DT09/CH10471P._CP',             # 07
        'ED6_DT09/CH10480P._CP',             # 08
        'ED6_DT09/CH10481P._CP',             # 09
        'ED6_DT09/CH10160P._CP',             # 0A
        'ED6_DT09/CH10160P._CP',             # 0B
        'ED6_DT09/CH10460P._CP',             # 0C
        'ED6_DT09/CH10461P._CP',             # 0D
        'ED6_DT27/CH03100P._CP',             # 0E
        'ED6_DT07/CH02120P._CP',             # 0F
        'ED6_DT07/CH02110P._CP',             # 10
        'ED6_DT26/CH20390P._CP',             # 11
        'ED6_DT26/CH20389P._CP',             # 12
        'ED6_DT26/CH20388P._CP',             # 13
        'ED6_DT26/CH20391P._CP',             # 14
        'ED6_DT26/CH20407P._CP',             # 15
        'ED6_DT09/CH11030P._CP',             # 16
        'ED6_DT09/CH11031P._CP',             # 17
    )

    DeclNpc(
        X                   = 73200,
        Z                   = -6020,
        Y                   = -15060,
        Direction           = 147,
        Unknown2            = 22,
        Unknown3            = 1441792,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5600,
        Z                   = -2000,
        Y                   = 30080,
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
        X                   = 117910,
        Z                   = -2020,
        Y                   = -87790,
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
        X                   = 36840,
        Z                   = -2000,
        Y                   = 16600,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 41480,
        Z                   = -6090,
        Y                   = 11430,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x187,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 83840,
        Z                   = -2000,
        Y                   = -19430,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 103150,
        Z                   = -6030,
        Y                   = -53480,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x188,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 73280,
        Z                   = -5940,
        Y                   = -40040,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 73200,
        Y                   = -7000,
        Z                   = -15060,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 79840,
        TriggerZ            = -6030,
        TriggerY            = -14200,
        TriggerRange        = 1000,
        ActorX              = 80360,
        ActorZ              = -6040,
        ActorY              = -13800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 112050,
        TriggerZ            = -6010,
        TriggerY            = -68270,
        TriggerRange        = 1000,
        ActorX              = 112550,
        ActorZ              = -5940,
        ActorY              = -68770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 66590,
        TriggerZ            = -6050,
        TriggerY            = -4800,
        TriggerRange        = 1000,
        ActorX              = 65960,
        ActorZ              = -5100,
        ActorY              = -4960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55480,
        TriggerZ            = -6680,
        TriggerY            = -65900,
        TriggerRange        = 5000,
        ActorX              = 55480,
        ActorZ              = -6680,
        ActorY              = -65900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_3F8",          # 01, 1
        "Function_2_4E9",          # 02, 2
        "Function_3_4FF",          # 03, 3
        "Function_4_6BA",          # 04, 4
        "Function_5_7D1",          # 05, 5
        "Function_6_8E8",          # 06, 6
        "Function_7_9FF",          # 07, 7
        "Function_8_27D3",         # 08, 8
        "Function_9_3359",         # 09, 9
        "Function_10_3405",        # 0A, 10
        "Function_11_3444",        # 0B, 11
        "Function_12_3483",        # 0C, 12
        "Function_13_34B3",        # 0D, 13
        "Function_14_34F7",        # 0E, 14
        "Function_15_3527",        # 0F, 15
        "Function_16_3588",        # 10, 16
        "Function_17_35D5",        # 11, 17
        "Function_18_3615",        # 12, 18
        "Function_19_3AFF",        # 13, 19
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3C2")
    OP_A3(0x10F0)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_3F7")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_3DE")
    OP_A3(0x10F2)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_3F7")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3F7")
    OP_A3(0x10F1)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)

    label("loc_3F7")

    Return()

    # Function_0_3A6 end

    def Function_1_3F8(): pass

    label("Function_1_3F8")

    OP_16(0x2, 0xFA0, 0xFFFEFA48, 0xFFFDA288, 0x230027)
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C8, 0x1, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x385, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_436")
    OP_B1("R2201_1")
    Jump("loc_43F")

    label("loc_436")

    OP_B1("R2201_2")

    label("loc_43F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_451")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)

    label("loc_451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463")
    OP_6F(0x0, 0)
    Jump("loc_46A")

    label("loc_463")

    OP_6F(0x0, 60)

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C")
    OP_6F(0x1, 0)
    Jump("loc_483")

    label("loc_47C")

    OP_6F(0x1, 60)

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495")
    OP_6F(0x2, 0)
    Jump("loc_49C")

    label("loc_495")

    OP_6F(0x2, 60)

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BA")
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_4CC")

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CC")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x395, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_23(0x1C8)

    label("loc_4E8")

    Return()

    # Function_1_3F8 end

    def Function_2_4E9(): pass

    label("Function_2_4E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4E9")

    label("loc_4FE")

    Return()

    # Function_2_4E9 end

    def Function_3_4FF(): pass

    label("Function_3_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 4)), scpexpr(EXPR_END)), "loc_507")
    Return()

    label("loc_507")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5EC"),
        (SWITCH_DEFAULT, "loc_60F"),
    )


    label("loc_5EC")

    Fade(500)
    OP_89(0x0, 76640, -6000, -19790, 319)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_60F")

    Battle(0xEDF, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 76640, -6000, -19790, 319)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_648"),
        (1, "loc_64B"),
        (SWITCH_DEFAULT, "loc_64E"),
    )


    label("loc_648")

    EventEnd(0x0)
    Return()

    label("loc_64B")

    OP_B4(0x0)
    Return()

    label("loc_64E")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x12FC)
    OP_28(0xA3, 0x4, 0x10)
    OP_28(0xA3, 0x4, 0x2)
    OP_28(0xA3, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_4FF end

    def Function_4_6BA(): pass

    label("Function_4_6BA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_792")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_729")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1304)
    Jump("loc_78F")

    label("loc_729")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFA\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_78F")

    Jump("loc_7C3")

    label("loc_792")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6BA end

    def Function_5_7D1(): pass

    label("Function_5_7D1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3DB, 1)"), scpexpr(EXPR_END)), "loc_840")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xDB\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1305)
    Jump("loc_8A6")

    label("loc_840")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xDB\x03\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xDB\x03\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_8A6")

    Jump("loc_8DA")

    label("loc_8A9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8DA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7D1 end

    def Function_6_8E8(): pass

    label("Function_6_8E8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x181, 1)"), scpexpr(EXPR_END)), "loc_957")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\x81\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1306)
    Jump("loc_9BD")

    label("loc_957")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\x81\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x81\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_9BD")

    Jump("loc_9F1")

    label("loc_9C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9F1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8E8 end

    def Function_7_9FF(): pass

    label("Function_7_9FF")

    EventBegin(0x0)
    OP_82(0x80, 0x0)
    OP_6D(13200, 10570, 10650, 0)
    OP_67(0, 13040, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(68000, 0)
    OP_6E(665, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_72(0x3, 0x4)
    OP_A1(0x9, 0x3)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 51850, -7500, -42660, 265)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 1140)
    LoadEffect(0x0, "map\\\\mp021_00.eff")

    def lambda_A96():
        OP_6D(42720, 10570, -45970, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A96)
    OP_C8(0x200, 0x46, "C_PLAC18._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6D(52300, -4200, -42780, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(224000, 0)
    OP_6E(589, 0)
    Sleep(1300)
    OP_22(0xFD, 0x0, 0x64)
    OP_B0(0x3, 0x32)
    OP_6F(0x3, 1140)
    OP_70(0x3, 0x4B0)
    OP_73(0x3)

    def lambda_B33():
        OP_6D(65000, -5990, -39540, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B33)

    def lambda_B4B():
        OP_67(0, 8800, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B4B)

    def lambda_B63():
        OP_6C(232000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B63)

    def lambda_B73():
        OP_6E(287, 8000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_B73)
    OP_43(0x102, 0x1, 0x0, 0xA)
    Sleep(1500)
    OP_43(0x101, 0x1, 0x0, 0xB)
    WaitChrThread(0x101, 0x2)
    Fade(500)
    OP_6D(69820, -5950, -38750, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(397, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #11
        0x102,
        (
            "#1033F#5P……别了，艾丝蒂尔。\x02\x03",

            "请不要再\x01",
            "继续追寻我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1026F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#1035F#5P能和你再度相会\x01",
            "虽然非常开心……\x02\x03",

            "但我们两人始终\x01",
            "不该在一起。\x02\x03",

            "#1033F有我这样的人在\x01",
            "只会害了你……\x02\x03",

            "说实话，你跟着我\x01",
            "也只是累赘而已。\x02\x03",

            "所以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1007F#6P……你说谎。\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    ChrTalk(    #15
        0x102,
        "#1034F#5P咦……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    OP_21()
    OP_1D(0x78)
    Sleep(500)

    def lambda_D2B():
        OP_6B(2200, 20000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D2B)
    Sleep(1500)

    ChrTalk(    #16
        0x101,
        (
            "#1025F#6P嗯…约修亚。\x02\x03",

            "我呢，听说了许多东西，\x01",
            "然后终于明白了一件事。\x02\x03",

            "#1012F为什么约修亚\x01",
            "会从我面前消失……\x02\x03",

            "或许，连约修亚自己\x01",
            "都没察觉到真正的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#1034F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1019F#6P因为心灵崩溃了，\x01",
            "和我在一起就觉得痛苦？\x02\x03",

            "就算和我在一起也只觉得\x01",
            "好像是别人的事情一样？\x02\x03",

            "#1007F约修亚在身边\x01",
            "会害了我？\x02\x03",

            "我跟着你\x01",
            "也只是累赘？\x02\x03",

            "#1006F这些全部，都是谎言吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        "#1032F怎么会是谎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1012F#6P好了，你听我说。\x02\x03",

            "#1025F要我说……\x01",
            "约修亚只是在害怕而已哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#1034F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1025F#6P深信自己\x01",
            "害死了姐姐……\x02\x03",

            "因此无法忍受\x01",
            "同样的事发生在我身上……\x02\x03",

            "所以，在那个夜晚，约修亚\x01",
            "才会从我的面前消失。\x02\x03",

            "#1016F其它的理由只不过是强加上去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1034F………………………………\x02\x03",

            "#1035F哈哈，你说什么呢……\x02\x03",

            "#1045F自从被教授调整以后\x01",
            "我就从未感到过恐惧。\x02\x03",

            "似乎是为了避免在执行任务中产生恐惧\x01",
            "而被调整为这样子。\x02\x03",

            "你的指责……完全偏离了重点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1007F#6P不，我要说的不是\x01",
            "那么表面化的东西。\x02\x03",

            "#1015F……我问你，约修亚。\x02\x03",

            "为什么你会觉得\x01",
            "姐姐死去的事情\x01",
            "就像是别人的事一样……\x02\x03",

            "你明白真正的理由吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1033F那是因为……\x02\x03",

            "我的心……已经坏掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1002F#6P不，不是的。\x02\x03",

            "#1007F约修亚……\x01",
            "只是不愿意回想起\x01",
            "姐姐死去时所受的打击。\x02\x03",

            "所以在潜意识中强制自己\x01",
            "将其认定为别人的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#1050F#3S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1025F#6P这和刚才救我的事情\x01",
            "是一样的。\x02\x03",

            "为了潜入战舰\x01",
            "你一定费了很大功夫吧？\x02\x03",

            "但你却毫不犹豫地\x01",
            "现身救我……\x02\x03",

            "那是因为你强烈盼望我能\x01",
            "早一刻脱离险境啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        "#1033F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1012F#6P约修亚的心并没有坏掉。\x02\x03",

            "只是因为恐惧……\x01",
            "所以在欺骗自己而已。\x02\x03",

            "#1006F现在的我\x01",
            "可以很有把握地肯定这一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1050F怎么会……但是……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 300)
    Sleep(1000)

    ChrTalk(    #32
        0x102,
        (
            "#1033F#5P#40W为什么你……#1000W\x01",
            "#40W……连这种事都……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1006F#6P以前我不是就说过嘛～\x01",
            "我可是最擅长观察约修亚的人呢。\x02\x03",

            "何况现在又知道了约修亚过去的身世，\x01",
            "已经没人会比我更了解约修亚了。\x02\x03",

            "#1018F即便是教授和莱维\x01",
            "我也绝对不会输给他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        "#1033F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1025F#6P胆怯又勇敢的约修亚。\x02\x03",

            "喜欢说谎，本性却又这么诚实的约修亚。\x02\x03",

            "#1012F我……最喜欢的约修亚。\x02\x03",

            "#1017F终于……\x01",
            "回到我的身边了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)

    def lambda_1523():
        OP_92(0x101, 0x102, 0x190, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1523)
    Sleep(600)
    Fade(500)
    OP_6D(68080, -6690, -40950, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(225000, 0)
    OP_6E(379, 0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    SetChrFlags(0x101, 0x80)
    SetChrChipByIndex(0x102, 18)
    SetChrSubChip(0x102, 0)
    SetChrFlags(0x102, 0x2)
    OP_99(0x102, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #36
        0x102,
        "#1050F#6P……！………\x02",
    )

    CloseMessageWindow()

    def lambda_15CB():
        OP_6B(2200, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15CB)
    OP_99(0x102, 0x3, 0x6, 0x3E8)
    Sleep(1000)

    ChrTalk(    #37
        0x101,
        (
            "#1003F#2P但是我……\x01",
            "并不是仅仅需要你的保护。\x02\x03",

            "因为我知道，作为一名游击士，\x01",
            "时刻都伴随着危险。\x02\x03",

            "#1025F无论有没有约修亚，\x01",
            "这都是无法改变的事实。\x02\x03",

            "这是我自己\x01",
            "选择的道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#1033F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x7, 0x9, 0x5DC)
    Sleep(500)

    ChrTalk(    #39
        0x101,
        (
            "#1025F#2P所以……\x02\x03",

            "所以约修亚，答应我。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0x9, 0xC, 0x5DC)
    Sleep(500)

    ChrTalk(    #40
        0x102,
        "#1034F#6P……什么…………\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0xD, 0xF, 0x3E8)
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1012F#2P让我们彼此守护，\x01",
            "一起向前吧。\x02\x03",

            "我已经变强了，\x01",
            "足以保护约修亚。\x02\x03",

            "只要有约修亚在身边，\x01",
            "我的力量就会增大好几倍呢。\x02\x03",

            "就算是『结社』想要加害，\x01",
            "也绝对不会死的……\x02\x03",

            "所以呢……\x01",
            "你已经不需要再害怕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1051F#6P……艾丝……蒂尔………\x02\x03",

            "#1039F…………啊…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0xF, 0x12, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0x13, 0x15, 0x3E8)
    SetChrSubChip(0x102, 21)
    Sleep(100)

    def lambda_1867():

        label("loc_1867")

        OP_99(0xFE, 0x24, 0x27, 0x3E8)
        OP_48()
        Jump("loc_1867")

    QueueWorkItem2(0x102, 2, lambda_1867)
    Sleep(1500)

    ChrTalk(    #43
        0x102,
        (
            "#1039F#6P#40W为什……么……\x02\x03",

            "#40W……眼泪会……\x01",
            "姐姐死后……\x02\x03",

            "#40W即使是在演戏时……\x01",
            "也从来……都没流过的……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x2)
    SetChrSubChip(0x102, 36)
    Sleep(200)
    SetChrSubChip(0x102, 22)
    Sleep(200)
    SetChrSubChip(0x102, 23)
    Sleep(200)
    SetChrSubChip(0x102, 24)
    Sleep(200)
    OP_99(0x102, 0x28, 0x2B, 0x5DC)
    Sleep(1000)

    ChrTalk(    #44
        0x101,
        "#1008F#2P#30W嘿嘿……是吗……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 43)
    Sleep(100)
    SetChrSubChip(0x102, 25)
    Sleep(100)
    SetChrSubChip(0x102, 26)
    Sleep(100)
    SetChrSubChip(0x102, 27)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #45
        (
            "\x07\x00#30W我什么都没有看到哦……\x01",
            "你就尽情哭吧……\x02\x03",

            "#40W我会一直这样……\x01",
            "……抱紧你的……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0x1388)
    OP_21()
    Sleep(2000)
    OP_6D(75980, -5890, -51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(225000, 0)
    OP_6E(317, 0)
    OP_82(0x80, 0x0)
    SetChrSubChip(0x102, 6)
    OP_1D(0x75)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_6D(69420, -5960, -39640, 6000)
    Fade(1000)
    OP_6D(69420, -5960, -39640, 0)
    OP_67(0, 6950, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(201000, 0)
    OP_6E(317, 0)
    OP_0D()
    Sleep(1000)
    OP_99(0x102, 0x6, 0x9, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0x9, 0xC, 0x3E8)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x101, 0x80)
    OP_8C(0x102, 225, 0)
    OP_8C(0x101, 45, 0)

    def lambda_1AF5():
        OP_6D(69190, -5930, -39970, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AF5)
    OP_8F(0x101, 0x10D38, 0xFFFFE8CC, 0xFFFF6532, 0x3E8, 0x0)
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)
    Sleep(500)

    ChrTalk(    #46
        0x101,
        (
            "#1008F#2P嘿嘿……\x02\x03",

            "#1016F好、好难为情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1053F#6P嗯……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1004F#2P啊……对了！\x02\x03",

            "#1006F这个，还给你。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 8)
    SetChrFlags(0x101, 0x2)

    def lambda_1BBA():

        label("loc_1BBA")

        OP_99(0xFE, 0x8, 0xF, 0x3E8)
        OP_48()
        Jump("loc_1BBA")

    QueueWorkItem2(0x101, 1, lambda_1BBA)
    OP_8F(0x101, 0x10EE6, 0xFFFFE8AE, 0xFFFF6582, 0x1F4, 0x0)
    OP_44(0x101, 0x1)
    Fade(500)
    SetChrFlags(0x101, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 17)
    SetChrSubChip(0x102, 0)
    OP_99(0x102, 0x1, 0x2, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0x3, 0x4, 0x3E8)
    Sleep(500)

    ChrTalk(    #49
        0x102,
        "#1044F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x5, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #50
        0x101,
        (
            "#1007F#2P真是的……\x01",
            "这可是姐姐的遗物吧？\x02\x03",

            "#1019F怎么能随便给别人呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1043F#6P嗯……\x02\x03",

            "#1040F确实太随便了。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0x7, 0x8, 0x3E8)
    Sleep(1000)

    ChrTalk(    #52
        0x101,
        (
            "#1025F#2P你的姐姐……\x01",
            "是个怎么样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#1053F#6P嗯……这个嘛……\x02\x03",

            "#1040F气质优雅又温柔，\x01",
            "但又有凛然的威严……\x02\x03",

            "和莱维很相配，\x01",
            "小时候我还有点嫉妒呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1015F#2P气质优雅又温柔，\x01",
            "威严凛然的类型……\x02\x03",

            "#1004F那不就是……\x01",
            "像科洛丝那种感觉吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#1054F#6P哈哈……是啊。\x02\x03",

            "#1053F虽然长相完全不同，\x01",
            "但性格上也许很相近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1015F#2P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        "#1044F#6P……艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1013F#2P没、没什么。\x02\x03",

            "#1019F……话说在前，\x01",
            "科洛丝，还有大家\x01",
            "也都非常担心你呢。\x02\x03",

            "回去之后要好好向他们道歉哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1043F#6P艾丝蒂尔……我……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1002F#2P我可不想听你说什么\x01",
            "没有资格回去之类的话。\x02\x03",

            "就算是做了教授的工具，\x01",
            "那也不是有意去做的啊！\x02\x03",

            "#1007F空贼艇的抢夺事件\x01",
            "也只是为了潜入调查。\x02\x03",

            "#1006F只要你把『结社』的情报\x01",
            "告诉老爸，不就功过相抵了嘛。\x02\x03",

            "这就是所谓的公平交易吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        "#1052F#6P这好像是不一样的吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1006F#2P而且，你的计划已经暴露，\x01",
            "也没办法再潜回那艘船了吧？\x02\x03",

            "这样的话，就只有和我们\x01",
            "一起行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1048F#6P……要不是你来捣乱，\x01",
            "我早就可以按照原定计划\x01",
            "把『古罗力亚斯号』炸毁了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1007F#2P唔……抱歉哦。\x02\x03",

            "#1020F喂！别再说爆破之类\x01",
            "的话吓唬人啦！\x02\x03",

            "就算是对抗『结社』，\x01",
            "也没必要用上这种极端手段吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1043F#6P……不这么做\x01",
            "是无法打倒教授和莱维的啊。\x02\x03",

            "#1035F不过，就算爆破成功，\x01",
            "能杀死他们的可能性也很低……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1007F#2P唉，真是的……\x02\x03",

            "#1019F幸好我被\x01",
            "抓住了。\x02\x03",

            "不然约修亚就会\x01",
            "做出无可挽回的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        "#1053F#6P呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1009F#2P啊～你刚才觉得我\x01",
            "『又在说这么天真的话』\x01",
            "没有错吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#1041F#6P不，一阵子没见，\x01",
            "你好像成熟了不少……\x02\x03",

            "不过艾丝蒂尔还是\x01",
            "原来的艾丝蒂尔呢。\x02\x03",

            "#1049F真让人开心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1020F#2P唔……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x101, 0x2)
    TurnDirection(0x101, 0x102, 0)
    ClearChrFlags(0x101, 0x80)
    SetChrSubChip(0x102, 9)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 225, 600)
    Sleep(1000)

    ChrTalk(    #71
        0x101,
        (
            "#1013F#5P（我、我这是怎么了！）\x02\x03",

            "(为什么到现在，看到约修亚的笑容\x01",
            "  还会心跳不已啊～！)\x02\x03",

            "#1007F（啊啊，也许是好久不见了，\x01",
            "  有些控制不住了吧……)\x02\x03",

            "(………………………………)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        "#1044F#6P？艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1013F#5P对了、对了……\x02\x03",

            "约修亚和那个男人婆\x01",
            "关系相当好了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#1044F#6P男人婆……\x01",
            "啊啊，你是说乔丝特吗。\x02\x03",

            "#1053F是啊，虽然一开始\x01",
            "她好像十分讨厌我的样子……\x02\x03",

            "不过到后来，很意外地\x01",
            "融洽相处了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1013F#5P融洽相处……\x02\x03",

            "………………………………\x02\x03",

            "……那是不是，接过吻了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        "#1044F#6P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1019F#5P不要支支吾吾，快回答！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1048F#6P啊、啊啊……\x02\x03",

            "当然没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1013F#5P那、那么……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 300)
    Sleep(1000)

    ChrTalk(    #80
        0x101,
        (
            "#1017F#2P在这里……\x01",
            "那天晚上的要求…\x01",
            "重来一次可以吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x102,
        "#1043F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1013F#2P因、因为第一次\x01",
            "对于女孩子来说很重要嘛……\x02\x03",

            "都、都怪约修亚，\x01",
            "竟然给搞成那个样子……\x02\x03",

            "你要……负责任哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        "#1044F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x80)
    OP_99(0x102, 0xA, 0xD, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0xD, 0x10, 0x3E8)
    Sleep(1000)

    ChrTalk(    #84
        0x101,
        "#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#1056F#6P（……艾丝蒂尔……）\x02\x03",

            "#1054F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0x10, 0x12, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0x12, 0x15, 0x3E8)
    Sleep(500)

    ChrTalk(    #86
        0x101,
        "#2P（……啊………）\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x15, 0x19, 0x3E8)
    Sleep(100)
    Sleep(200)
    SetMessageWindowPos(50, 100, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #87
        "#3S喂，约修亚！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0x102, 0x1B, 0x1E, 0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1CA5)
    SetMapFlags(0x2000000)
    OP_A2(0x10FD)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_9FF end

    def Function_8_27D3(): pass

    label("Function_8_27D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_82(0x80, 0x0)
    SetChrPos(0x101, 68830, -5930, -39840, 135)
    SetChrPos(0x102, 70100, -5950, -39240, 135)
    OP_72(0x3, 0x4)
    OP_A1(0x9, 0x3)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 51850, -7500, -42660, 265)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 1200)
    OP_B0(0x3, 0xA)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    OP_6D(79640, -6290, -56570, 0)
    OP_67(0, 9360, -10000, 0)
    OP_6B(4070, 0)
    OP_6C(155000, 0)
    OP_6E(551, 0)
    OP_A1(0xA, 0x4)
    SetChrPos(0xA, 74070, 6000, -51400, 45)
    OP_72(0x4, 0x4)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 360)
    OP_70(0x4, 0x1CC)

    def lambda_28C3():
        OP_6D(76120, -6250, -54260, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28C3)

    def lambda_28DB():
        OP_67(0, 10670, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28DB)

    def lambda_28F3():
        OP_6B(3500, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28F3)

    def lambda_2903():
        OP_6C(180000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2903)

    def lambda_2913():
        OP_6E(398, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2913)
    LoadEffect(0x0, "map\\\\mp021_00.eff")
    FadeToBright(2000, 0)

    def lambda_2940():
        OP_8F(0xFE, 0x12156, 0xFFFFE890, 0xFFFF3738, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2940)
    Sleep(2000)

    def lambda_2960():
        OP_8F(0xFE, 0x12156, 0xFFFFE890, 0xFFFF3738, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2960)
    PlayEffect(0x0, 0x0, 0xA, 0, -2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    Sleep(1000)

    def lambda_29BA():
        OP_8F(0xFE, 0x12156, 0xFFFFE890, 0xFFFF3738, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_29BA)
    OP_72(0x4, 0x20)
    OP_73(0x4)
    OP_82(0x0, 0x2)
    OP_6F(0x4, 460)
    OP_70(0x4, 0x28A)
    OP_73(0x4)
    OP_23(0x79)
    OP_23(0xCC)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x4, 1)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    Sleep(500)

    def lambda_2A2D():
        OP_6D(71790, -6370, -56090, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A2D)

    def lambda_2A45():
        OP_67(0, 6280, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A45)

    def lambda_2A5D():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A5D)

    def lambda_2A6D():
        OP_6C(191000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A6D)

    def lambda_2A7D():
        OP_6E(455, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2A7D)
    SetChrPos(0xB, 73580, -450, -50830, 315)
    SetChrBattleFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0xC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xB, 0x0)

    ChrTalk(    #88
        0x101,
        "#1005F#5P男、男人婆！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xB,
        (
            "#213F#5P怎么，你也\x01",
            "一起逃出来了啊。\x02\x03",

            "#210F真是的……\x01",
            "继续被关着不是挺好嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1019F#1P你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xC, 73100, -450, -51090, 315)
    SetChrPos(0xD, 73100, -450, -51090, 315)

    ChrTalk(    #91
        0xC,
        (
            "#4P好啦，乔丝特。\x01",
            "别再没事挑衅啦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B9C():
        OP_6D(71160, -6550, -57510, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B9C)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0xD)
    Sleep(1500)
    OP_43(0xD, 0x1, 0x0, 0xE)
    WaitChrThread(0xD, 0x1)
    Sleep(500)

    ChrTalk(    #92
        0xD,
        (
            "#490F#5P游击士小姑娘，\x01",
            "你们暂且休战一下吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1007F#5P嗯，唔……\x01",
            "刚才承蒙你们相救，\x02\x03",

            "#1006F再次感谢。\x01",
            "真是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        "#191F#5P哈哈哈，这种小事不值一提啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        (
            "#210F#5P哼，我才没打算\x01",
            "救你呢。\x02\x03",

            "不用谢我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1019F#5P哼……你这男人婆，\x01",
            "真想把你抓起来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xC,
        (
            "#200F#5P对了，约修亚。\x01",
            "之后你要怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1026F#5P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(68910, -5930, -41190, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(202000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x101, 2)
    SetChrChipByIndex(0x101, 21)
    OP_0D()
    Sleep(500)

    ChrTalk(    #99
        0xC,
        (
            "#204F#7P我们本是来\x01",
            "邀请你和我们一起走的……\x02\x03",

            "#200F不过，看这种样子…\x01",
            "这句话也没必要问了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        (
            "#1035F#6P嗯……抱歉。\x02\x03",

            "#1040F今后的事情会变成怎样，\x01",
            "我还无法确定……\x02\x03",

            "但我现在想\x01",
            "和艾丝蒂尔一起回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1025F#2P约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        "#490F#7P嘿，是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        (
            "#215F#7P……………………………\x02\x03",

            "#413F唉，也好。\x01",
            "反正还有机会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1019F#2P哼。\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x2, 0x1, 0x7D0)
    Sleep(100)
    Fade(500)
    OP_6D(71160, -6550, -57510, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(191000, 0)
    OP_6E(455, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #105
        0xB,
        (
            "#211F#5P约修亚，记住！\x02\x03",

            "要是以后厌烦了这个无脑女，\x01",
            "随时都可以回到我们这里哦！\x02\x03",

            "#415F我们会热烈欢迎你的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1005F#5P谁、谁是无脑女呀！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        (
            "#1049F#1P哈哈……\x01",
            "多谢了，乔丝特！\x02\x03",

            "#1041F多伦兄、吉尔兄！\x01",
            "感谢你们多日来的关照！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        "#490F#5P嘿，彼此彼此啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xC,
        (
            "#202F#5P那，再见啦！\x01",
            "后会有期！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x0, 0x11)
    Sleep(1000)
    OP_43(0xC, 0x1, 0x0, 0x10)
    Sleep(1000)
    OP_43(0xB, 0x1, 0x0, 0xF)
    WaitChrThread(0xB, 0x1)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    OP_22(0xE6, 0x0, 0x64)
    OP_73(0x4)
    Sleep(1000)
    Fade(1000)
    OP_6D(71340, -6240, -49430, 0)
    OP_67(0, 9140, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(179000, 0)
    OP_6E(664, 0)
    OP_0D()

    def lambda_30E6():
        OP_6D(71340, -4000, -49430, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30E6)

    def lambda_30FE():
        OP_67(0, 14800, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30FE)

    def lambda_3116():
        OP_8F(0xFE, 0x12156, 0x0, 0xFFFF3738, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3116)
    OP_43(0xA, 0x2, 0x0, 0x9)
    PlayEffect(0x0, 0x0, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_22(0x79, 0x1, 0x64)
    Sleep(1500)
    OP_B0(0x4, 0xA)
    OP_6F(0x4, 160)
    OP_70(0x4, 0xF0)
    OP_73(0x4)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 240)
    OP_70(0x4, 0x154)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0x101, 0x1)
    OP_82(0x0, 0x2)
    OP_23(0xCC)
    Fade(500)
    OP_6D(74870, -2760, -45440, 0)
    OP_67(0, 9140, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(34000, 0)
    OP_6E(664, 0)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    OP_0D()

    def lambda_320A():
        OP_6D(68970, -2760, -60770, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_320A)

    def lambda_3222():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3222)
    Sleep(200)

    def lambda_3242():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3242)
    Sleep(200)

    def lambda_3262():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3262)
    Sleep(100)

    def lambda_3282():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3282)
    Sleep(100)

    def lambda_32A2():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_32A2)
    Sleep(100)

    def lambda_32C2():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_32C2)
    Sleep(100)

    def lambda_32E2():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_32E2)
    Sleep(100)

    def lambda_3302():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3302)
    Sleep(100)

    def lambda_3322():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3322)
    WaitChrThread(0xA, 0x1)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FC)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_27D3 end

    def Function_9_3359(): pass

    label("Function_9_3359")


    def lambda_335F():
        OP_8C(0xFE, 202, 5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_335F)
    Sleep(400)

    def lambda_3372():
        OP_8C(0xFE, 202, 10)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3372)
    Sleep(400)

    def lambda_3385():
        OP_8C(0xFE, 202, 15)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3385)
    Sleep(400)

    def lambda_3398():
        OP_8C(0xFE, 202, 20)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3398)
    Sleep(400)

    def lambda_33AB():
        OP_8C(0xFE, 202, 30)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_33AB)
    Sleep(3500)

    def lambda_33BE():
        OP_8C(0xFE, 202, 20)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_33BE)
    Sleep(700)

    def lambda_33D1():
        OP_8C(0xFE, 202, 15)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_33D1)
    Sleep(600)

    def lambda_33E4():
        OP_8C(0xFE, 202, 10)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_33E4)
    Sleep(500)

    def lambda_33F7():
        OP_8C(0xFE, 202, 5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_33F7)
    WaitChrThread(0xA, 0x3)
    Return()

    # Function_9_3359 end

    def Function_10_3405(): pass

    label("Function_10_3405")

    ClearChrFlags(0x102, 0x80)
    SetChrPos(0x102, 51690, -4200, -43010, 90)
    OP_8E(0x102, 0xEEAC, 0xFFFFE67E, 0xFFFF5E5C, 0x7D0, 0x0)
    OP_8F(0x102, 0x111D4, 0xFFFFE8C2, 0xFFFF66B8, 0x7D0, 0x0)
    Return()

    # Function_10_3405 end

    def Function_11_3444(): pass

    label("Function_11_3444")

    ClearChrFlags(0x101, 0x80)
    SetChrPos(0x101, 51690, -4200, -43010, 90)
    OP_8E(0x101, 0xEEAC, 0xFFFFE67E, 0xFFFF5E5C, 0x7D0, 0x0)
    OP_8F(0x101, 0x10A2C, 0xFFFFE8CC, 0xFFFF6654, 0x7D0, 0x0)
    Return()

    # Function_11_3444 end

    def Function_12_3483(): pass

    label("Function_12_3483")

    OP_8E(0xFE, 0x11C24, 0xFFFFFE3E, 0xFFFF3EA4, 0xBB8, 0x0)
    OP_8E(0xFE, 0x122A0, 0xFFFFFF56, 0xFFFF4A20, 0xBB8, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_12_3483 end

    def Function_13_34B3(): pass

    label("Function_13_34B3")

    SetChrBattleFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    OP_8E(0xC, 0x11B48, 0xFFFFFE3E, 0xFFFF3EC2, 0x7D0, 0x0)
    OP_8E(0xC, 0x12098, 0x14, 0xFFFF452A, 0x7D0, 0x0)
    OP_8C(0xC, 315, 400)
    Return()

    # Function_13_34B3 end

    def Function_14_34F7(): pass

    label("Function_14_34F7")

    SetChrBattleFlags(0xD, 0x20)
    ClearChrFlags(0xD, 0x1)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x80)
    OP_8E(0xD, 0x11B48, 0xFFFFFE3E, 0xFFFF3EC2, 0x7D0, 0x0)
    OP_8C(0xD, 315, 400)
    Return()

    # Function_14_34F7 end

    def Function_15_3527(): pass

    label("Function_15_3527")

    OP_8E(0xFE, 0x12156, 0x28, 0xFFFF450C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x11C10, 0xFFFFFE3E, 0xFFFF3EFE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x11D8C, 0xFFFFFE3E, 0xFFFF386E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x12084, 0xFFFFFE3E, 0xFFFF3684, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_3527 end

    def Function_16_3588(): pass

    label("Function_16_3588")

    OP_8E(0xFE, 0x11A80, 0xFFFFFE3E, 0xFFFF3E2C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x11D8C, 0xFFFFFE3E, 0xFFFF386E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x12084, 0xFFFFFE3E, 0xFFFF3684, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_3588 end

    def Function_17_35D5(): pass

    label("Function_17_35D5")

    OP_8C(0xD, 135, 400)
    OP_8E(0xFE, 0x11D8C, 0xFFFFFE3E, 0xFFFF386E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x12084, 0xFFFFFE3E, 0xFFFF3684, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_35D5 end

    def Function_18_3615(): pass

    label("Function_18_3615")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 20)
    SetChrSubChip(0x102, 0)
    OP_82(0x80, 0x0)
    OP_72(0x3, 0x4)
    OP_A1(0x9, 0x3)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 51850, -7500, -42660, 265)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 1200)
    OP_6D(76830, -6040, -37090, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(215000, 0)
    OP_6E(624, 0)
    SetChrPos(0x101, 70130, -5950, -39180, 180)
    SetChrPos(0x102, 71460, -5970, -39040, 180)

    def lambda_36C4():
        OP_6D(71660, -5970, -39280, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36C4)

    def lambda_36DC():
        OP_67(0, 5600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36DC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(70470, -5960, -39980, 0)
    OP_67(0, 4240, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(225000, 0)
    OP_6E(281, 0)
    OP_0D()
    Sleep(500)
    OP_99(0x102, 0x0, 0x2, 0x5DC)
    Sleep(500)

    ChrTalk(    #110
        0x102,
        "#1043F#6P……对了，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x0, 0x2, 0x5DC)
    Sleep(500)

    ChrTalk(    #111
        0x101,
        "#1017F#2P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#1035F……敌人实在太过强大了。\x02\x03",

            "我想，教授抓走艾丝蒂尔的用意\x01",
            "也是为了把我引诱出来吧。\x02\x03",

            "#1042F这样才能保证在自己离开时，\x01",
            "『古罗力亚斯号』不被攻破。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1020F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#1043F#6P莱维也是，\x01",
            "当时他完全可以在解决我们之后\x01",
            "再去阻止引擎的失控。\x02\x03",

            "他之所以没这样做……\x01",
            "应该就是因为觉得我太没用，\x01",
            "所以手下留情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1026F#2P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#1042F其他执行者也是一样……\x02\x03",

            "单论战斗力\x01",
            "都是在我之上的高手。\x02\x03",

            "说实话，今后还会面对无数的苦战。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x2, 0x4, 0x5DC)
    Sleep(500)

    ChrTalk(    #117
        0x101,
        "#1003F#2P嗯……\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x2, 0x4, 0x5DC)
    Sleep(300)

    ChrTalk(    #118
        0x102,
        (
            "#1053F#6P但是……我答应你。\x02\x03",

            "#1040F绝不会再一次……\x01",
            "逃避现实了。\x02\x03",

            "我会和你一起……\x01",
            "走到最后。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x4, 0x2, 0x5DC)
    Sleep(500)

    ChrTalk(    #119
        0x101,
        (
            "#1008F#2P约修亚……\x02\x03",

            "#1017F嗯……我也发誓！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_3F(0x411, 1)
    OP_AD(0x2400B3, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1CA9)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x128), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC4")
    ShowSaveMenu()

    label("loc_3AC4")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    OP_A3(0x1CA9)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C0705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3615 end

    def Function_19_3AFF(): pass

    label("Function_19_3AFF")

    EventBegin(0x1)

    ChrTalk(    #120
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_3B2B():
        OP_6D(57640, -6680, -64840, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B2B)

    def lambda_3B43():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3B43)

    def lambda_3B53():
        OP_6C(20000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3B53)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #121
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BDA")
    OP_C0(0xE, 0x16, 0xE9AC, 0xFFFFE5CA, 0xFFFF05F6, 0xFA, 0xD8B8, 0xFFFFE9D0, 0xFFFEFE94)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_3BE9")

    label("loc_3BDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BE9")
    EventEnd(0x1)

    label("loc_3BE9")

    Return()

    # Function_19_3AFF end

    SaveToFile()

Try(main)
