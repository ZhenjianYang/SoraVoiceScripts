from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Bronco',                               # 9
        '飛行挺',                               # 10
        '飛行挺',                               # 11
        'Josette',                              # 12
        'Kyle',                                 # 13
        'Don',                                  # 14
        'Manoria Village',                      # 15
        'Ruan',                                 # 16
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
        "Function_4_6CE",          # 04, 4
        "Function_5_822",          # 05, 5
        "Function_6_97E",          # 06, 6
        "Function_7_AEC",          # 07, 7
        "Function_8_3263",         # 08, 8
        "Function_9_3FED",         # 09, 9
        "Function_10_4099",        # 0A, 10
        "Function_11_40D8",        # 0B, 11
        "Function_12_4117",        # 0C, 12
        "Function_13_4147",        # 0D, 13
        "Function_14_418B",        # 0E, 14
        "Function_15_41BB",        # 0F, 15
        "Function_16_421C",        # 10, 16
        "Function_17_4269",        # 11, 17
        "Function_18_42A9",        # 12, 18
        "Function_19_4892",        # 13, 19
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
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5FB"),
        (SWITCH_DEFAULT, "loc_61E"),
    )


    label("loc_5FB")

    Fade(500)
    OP_89(0x0, 76640, -6000, -19790, 319)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_61E")

    Battle(0xEDF, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 76640, -6000, -19790, 319)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_657"),
        (1, "loc_65A"),
        (SWITCH_DEFAULT, "loc_65D"),
    )


    label("loc_657")

    EventEnd(0x0)
    Return()

    label("loc_65A")

    OP_B4(0x0)
    Return()

    label("loc_65D")

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
        "\x07\x05Exterminated monster!\x02",
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

    def Function_4_6CE(): pass

    label("Function_4_6CE")

    OP_EA(0x2, 0xE2, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_73F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\xFA\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1304)
    Jump("loc_7A3")

    label("loc_73F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\xFA\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFA\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_7A3")

    Jump("loc_814")

    label("loc_7A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Watch out! This chest has nothing to lose!\x01",
            "There's no telling what it might do!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_814")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6CE end

    def Function_5_822(): pass

    label("Function_5_822")

    OP_EA(0x2, 0xE3, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3DB, 1)"), scpexpr(EXPR_END)), "loc_893")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\xDB\x03\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1305)
    Jump("loc_8F7")

    label("loc_893")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\xDB\x03\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xDB\x03\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_8F7")

    Jump("loc_970")

    label("loc_8FA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Inside the chest you find...blood. So much blood.\x01",
            "Why wasn't this here the first time?!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_970")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_822 end

    def Function_6_97E(): pass

    label("Function_6_97E")

    OP_EA(0x2, 0xE4, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A56")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x181, 1)"), scpexpr(EXPR_END)), "loc_9EF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\x81\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1306)
    Jump("loc_A53")

    label("loc_9EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\x81\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x81\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_A53")

    Jump("loc_ADE")

    label("loc_A56")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05I'll have you know that if you could take\x01",
            "multiple items from the same chest, the\x01",
            "economy would collapse.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_ADE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_97E end

    def Function_7_AEC(): pass

    label("Function_7_AEC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
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

    def lambda_B8E():
        OP_6D(42720, 10570, -45970, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B8E)
    OP_C8(0x200, 0x46, "C_PLAC18._CH", 0x1, 0x7D0)
    OP_DE("Gull Seaside Way")
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

    def lambda_C3D():
        OP_6D(65000, -5990, -39540, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C3D)

    def lambda_C55():
        OP_67(0, 8800, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C55)

    def lambda_C6D():
        OP_6C(232000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C6D)

    def lambda_C7D():
        OP_6E(287, 8000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_C7D)
    OP_43(0x102, 0x1, 0x0, 0xA)
    Sleep(1500)
    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(7500)
    WaitChrThread(0x101, 0x2)
    Fade(500)
    OP_C4(0x0, 0x2)
    OP_6D(69820, -5950, -38750, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(397, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Sleep(1000)
    OP_DC()

    ChrTalk(    #11
        0x102,
        (
            "#1033F#6PThis is goodbye, Estelle.\x02\x03",

            "Please do not chase after me anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1026F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#1035F#6PI was a little happy to see you\x01",
            "one last time, but...\x02\x03",

            "Even so, we should not be together.\x02\x03",

            "#1033FBeing with someone...like me...\x01",
            "will never be good for you.\x02\x03",

            "And, to be frank, you will only be\x01",
            "a burden to me.\x02\x03",

            "So--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1007F#6PYou're a terrible liar,\x01",
            "you know that?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    ChrTalk(    #15
        0x102,
        "#1034F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    OP_21()
    OP_1D(0x78)
    Sleep(500)

    def lambda_EA9():
        OP_6B(2200, 20000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA9)
    Sleep(1500)

    ChrTalk(    #16
        0x101,
        (
            "#1025F#6PJoshua...listen.\x02\x03",

            "I've seen and heard a lot since you left.\x02\x03",

            "#1012FAnd now? Now I think I understand.\x02\x03",

            "I understand the reason you left.\x01",
            "The real reason, the one you haven't\x01",
            "even admitted to yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#1034F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1019F#6PYou can't bear to be with me because\x01",
            "your heart's broken?\x02\x03",

            "You feel like being with me is someone else's\x01",
            "story that you can never, ever have?\x02\x03",

            "#1007FAnd come on, 'I'll be a bad influence on you'?\x02\x03",

            "Or 'you'll hold me back'? What?\x02\x03",

            "#1006FThat's all a bunch of lies. Every single one.\x01",
            "Especially that last one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        "#1032FThey aren't lies!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1012F#6PNo, Joshua... Really, listen.\x02\x03",

            "#1025FI understand now...\x01",
            "You're really, really scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#1034FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1025F#6PYou think it's your fault that your sister died.\x02\x03",

            "And you'd never, ever forgive yourself if\x01",
            "something happened to me.\x02\x03",

            "THAT'S why you ran away from me that night.\x02\x03",

            "#1016FEverything else was just pinned on\x01",
            "afterwards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1034F...\x02\x03",

            "#1035FHaha, that's ridiculous.\x02\x03",

            "#1045FWeissmann's conditioning left me incapable\x01",
            "of feeling fear.\x02\x03",

            "He took away my ability to feel it so that\x01",
            "I wouldn't hesitate during an operation.\x02\x03",

            "You're a little off target, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1007F#6PNo, darn it, I'm not talking about\x01",
            "something that superficial!\x02\x03",

            "#1015FJoshua...\x02\x03",

            "You said you can't help but feel like your\x01",
            "sister's death happened to someone else,\x01",
            "right?\x02\x03",

            "Do you know why that is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1033FOf course.\x02\x03",

            "It's because I'm...a broken wreck of\x01",
            "a human being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1002F#6PNuh-uh, no, no, wrongo.\x01",
            "We aren't letting self-pity get in the way here.\x02\x03",

            "#1007FJoshua, you...you just don't want to remember\x01",
            "how awful it was when your sister died.\x01",
            "How you blame yourself for it.\x02\x03",

            "Unconsciously you've been trying to think of it\x01",
            "as someone else's problem, to get away from it.\x01",
            "A lot of people do that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#1050F#3S...I!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1025F#6PAnd on that ship, don't tell me you weren't\x01",
            "afraid there!\x02\x03",

            "I mean, it was a lot of work just to sneak on\x01",
            "board, right?\x02\x03",

            "But you didn't even hesitate to help me escape...\x02\x03",

            "It's almost as if you were trying to get me away\x01",
            "from danger as fast as you possibly could.\x01",
            "Danger you were AFRAID of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        "#1033F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1012F#6PYou aren't a 'broken wreck,' Joshua.\x02\x03",

            "You're just scared, mostly because you care\x01",
            "for people so much it breaks your heart...\x01",
            "and you're lying to yourself about it.\x02\x03",

            "#1006FThat's how I see it, and I know I'm right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1050FBut I... That can't...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 300)
    Sleep(1000)

    ChrTalk(    #32
        0x102,
        "#1033F#6P#40WWhy...#1000W #40Wcan you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1006F#6PHave you forgotten, buster?\x01",
            "I'm Liberl's Number One Joshua-Watcher.\x02\x03",

            "Now that I know all about your past, too,\x01",
            "I'm the biggest authority on Joshua Astray\x01",
            "in the world!\x02\x03",

            "#1018FI know more than Weissmann or Loewe,\x01",
            "even!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        "#1033F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1025F#6PJoshua scared and Joshua brave.\x02\x03",

            "Joshua lying and Joshua honest.\x02\x03",

            "#1012FMy...beloved Joshua.\x02\x03",

            "#1017FI finally found you, Joshua.\x01",
            "I finally reached you.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)

    def lambda_1A07():
        OP_92(0x101, 0x102, 0x190, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A07)
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
        "#1050F#6P...Stop...\x02",
    )

    CloseMessageWindow()

    def lambda_1AAD():
        OP_6B(2200, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AAD)
    OP_99(0x102, 0x3, 0x6, 0x3E8)
    Sleep(1000)

    ChrTalk(    #37
        0x101,
        (
            "#1003F#4PBut I... I need to say this. I don't want to just\x01",
            "be one more person you feel like you have\x01",
            "to protect.\x02\x03",

            "As long as I'm a bracer, I can't stay\x01",
            "away from danger.\x02\x03",

            "#1025FThat's not gonna change even if you\x01",
            "leave again, Joshua.\x02\x03",

            "It's what I have to do to be who I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#1033F#6P...\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x7, 0x9, 0x5DC)
    Sleep(500)

    ChrTalk(    #39
        0x101,
        (
            "#1025F#4PAnd so...\x02\x03",

            "And so, Joshua? Let's make a promise.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0x9, 0xC, 0x5DC)
    Sleep(500)

    ChrTalk(    #40
        0x102,
        "#1034F#6PA...promise?\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0xD, 0xF, 0x3E8)
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1012F#4PLet's go forward together from now on\x01",
            "and protect each other. Equally.\x02\x03",

            "I'm strong enough to be able to cover your\x01",
            "back now, Joshua.\x02\x03",

            "And if you're at my side, there's nothing\x01",
            "I can't beat.\x02\x03",

            "No matter what kind of crazy nonsense the\x01",
            "society throws at me, I won't die.\x02\x03",

            "So... So you don't need to be afraid for me\x01",
            "anymore. I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1051F#6PEs...telle...\x02\x03",

            "#1039F...I...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0xF, 0x12, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0x13, 0x15, 0x3E8)
    SetChrSubChip(0x102, 21)
    Sleep(100)

    def lambda_1E1F():

        label("loc_1E1F")

        OP_99(0xFE, 0x24, 0x27, 0x3E8)
        OP_48()
        Jump("loc_1E1F")

    QueueWorkItem2(0x102, 2, lambda_1E1F)
    Sleep(1500)

    ChrTalk(    #43
        0x102,
        (
            "#1039F#6P#40WWhy... How...?\x02\x03",

            "#40WI...haven't been able to cry since...\x01",
            "since Karin died...\x02\x03",

            "#40WI could never even...shed tears as an act...\x01",
            "but now...\x02",
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
        "#1008F#4P#30WAh...it's okay.\x02",
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
    SetChrName("Estelle")

    AnonymousTalk(    #45
        (
            "\x07\x00#30WNo one's looking. Cry as long as you want.\x02\x03",

            "#40WAnd I'll...just hold you like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
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

    def lambda_20DB():
        OP_6D(69190, -5930, -39970, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20DB)
    OP_8F(0x101, 0x10D38, 0xFFFFE8CC, 0xFFFF6532, 0x3E8, 0x0)
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)
    Sleep(500)
    OP_DC()

    ChrTalk(    #46
        0x101,
        (
            "#1008F#4PAhaha...\x02\x03",

            "#1016FThat was, um, a little embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1053F#6PHaha... No kidding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1004F#4POh, right!\x02\x03",

            "#1006FHere, let me return this.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 8)
    SetChrFlags(0x101, 0x2)

    def lambda_21C7():

        label("loc_21C7")

        OP_99(0xFE, 0x8, 0xF, 0x3E8)
        OP_48()
        Jump("loc_21C7")

    QueueWorkItem2(0x101, 1, lambda_21C7)
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
        "#1044F#6POh!\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x5, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #50
        0x101,
        (
            "#1007F#4PSeriously, Joshua.\x01",
            "This is your only memento of Karin, right?\x02\x03",

            "#1019FYou shouldn't just fob this off on others\x01",
            "without thinking, buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1043F#6PYes...\x02\x03",

            "#1040FIt was a bit thoughtless of me,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0x7, 0x8, 0x3E8)
    Sleep(1000)

    ChrTalk(    #52
        0x101,
        (
            "#1025F#4PI was kinda wondering.\x01",
            "What kind of person was she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#1053F#6PWhat kind of person? Hmm.\x02\x03",

            "#1040FShe was friendly to everyone she met...\x01",
            "kind almost to a fault...and she had dignity\x01",
            "born of humility.\x02\x03",

            "She and Loewe--the Loewe of back then--\x01",
            "were perfect together. I was always a little\x01",
            "jealous of them as a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1015F#4PFriendly, kind, and dignified...\x02\x03",

            "#1004FSo she was kind of like Kloe, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#1054F#6PHaha. It's a good comparison,\x01",
            "thinking about it.\x02\x03",

            "#1053FKarin didn't look like Kloe--she had my eyes\x01",
            "and hair--but they were similar in spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1015F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        "#1044F#6PEstelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1013F#4POh, uh, nothing.\x02\x03",

            "#1019FOh, speakin' of KLOE.\x01",
            "You realize you worried her and everyone\x01",
            "else sick too and not just me, right?\x02\x03",

            "You have some serious groveling to do\x01",
            "when we get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1043F#6PEstelle... I do--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1002F#4PIf you say something like 'Oh, I don't have\x01",
            "the right to go back,' I'm gonna just drag\x01",
            "you back by your hair, 'kay?\x02\x03",

            "Sure, you were Weissmann's spy.\x01",
            "But you didn't even know it, right?\x02\x03",

            "#1007FEven helping the bandits get their ship\x01",
            "back was done to try and stop the society,\x01",
            "right?\x02\x03",

            "#1006FIf you tell Dad about the society's plans,\x01",
            "that'll make it even.\x02\x03",

            "That's what they call a plea bargain,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1052F#6PThat's...not quite how a plea bargain\x01",
            "works...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1006F#4PBesides, even if you want to stop the society,\x01",
            "you can't get back on that ship, can you?\x02\x03",

            "In that case, your only option is to work\x01",
            "with us, buster!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1048F#6P...And if you hadn't been abducted,\x01",
            "I could have destroyed the Glorious as\x01",
            "I originally planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1007F#4PUrk. Uh, yeah, sorry.\x02\x03",

            "#1020FEr! Wait, hold on, how can you\x01",
            "say 'destroy the Glorious' so easily?!\x02\x03",

            "I know it's the society we're talking about,\x01",
            "but were you really going to kill them all?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1043F#6PIt will take nothing less to stop\x01",
            "Weissmann and Loewe.\x02\x03",

            "#1035FAnd even then, there's a decent chance\x01",
            "that they'd survive the destruction of\x01",
            "the Glorious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1007F#4PFor the love of...\x02\x03",

            "#1019FNo, actually, I think it's for the best\x01",
            "I got caught.\x02\x03",

            "You were going to do something\x01",
            "completely crazy, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        "#1053F#6PHeheh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1009F#4PMmmph! You're all 'Heh, Estelle's being\x01",
            "all cute and naive' again, aren't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#1041F#6PNo, not at all. It's just that...\x01",
            "you have matured a lot as a person\x01",
            "while we've been apart.\x02\x03",

            "But, ultimately, you're still Estelle.\x02\x03",

            "#1049FThat...makes me happier than\x01",
            "I thought possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1020F#4POh, ummm...\x02",
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
            "#1013F#6P(C-C'mon, Estelle!)\x02\x03",

            "(Why the heck does Joshua's smile still\x01",
            "make my heart race?!)\x02\x03",

            "#1007F(It's 'cause it's been a while, isn't it...\x01",
            "It still gets me, right there...)\x02\x03",

            "(...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        "#1044F#6PMm? Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1013F#6PH-Hey...\x02\x03",

            "You got along pretty well with\x01",
            "that tomboy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#1044F#6PTomboy? Oh, you mean Josette.\x02\x03",

            "#1053FWell, at first we had our...differences.\x02\x03",

            "Even so, we came to understand each\x01",
            "other pretty well by the end, I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1013F#6PUnderstand each...\x02\x03",

            "...\x02\x03",

            "...Did you kiss her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        "#1044F#6PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1019F#6PQuestion. Answer. GIVE.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1048F#6PR-Right...\x02\x03",

            "Of course I didn't.\x01",
            "Our relationship wasn't like THAT.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1013F#6POh. Umm, good. Well, um, then.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 300)
    Sleep(1000)

    ChrTalk(    #80
        0x101,
        "#1017F#4PCan I...request a do-over of that night?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x102,
        "#1043F#6PA do-over...? Oh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1013F#4PTh-Th-The first kiss is really important to\x01",
            "a girl, you know!\x02\x03",

            "And, and it was all your fault that mine\x01",
            "got wasted!\x02\x03",

            "So you've...you've to got take responsibility,\x01",
            "mister!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        "#1044F#6PEstelle...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x80)
    OP_99(0x102, 0xA, 0xD, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0xD, 0x10, 0x3E8)
    Sleep(1000)

    ChrTalk(    #84
        0x101,
        "#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#1056F#6P(Estelle... I suppose I do.)\x02\x03",

            "#1054F...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0x10, 0x12, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0x12, 0x15, 0x3E8)
    Sleep(500)

    ChrTalk(    #86
        0x101,
        "#2P(...Mmm...)\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x15, 0x19, 0x3E8)
    Sleep(100)
    Sleep(200)
    SetMessageWindowPos(50, 100, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #87
        "#3SHeeeey, Joshua!\x02",
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

    # Function_7_AEC end

    def Function_8_3263(): pass

    label("Function_8_3263")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
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

    def lambda_3354():
        OP_6D(76120, -6250, -54260, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3354)

    def lambda_336C():
        OP_67(0, 10670, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_336C)

    def lambda_3384():
        OP_6B(3500, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3384)

    def lambda_3394():
        OP_6C(180000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3394)

    def lambda_33A4():
        OP_6E(398, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33A4)
    LoadEffect(0x0, "map\\\\mp021_00.eff")
    FadeToBright(2000, 0)
    OP_C4(0x0, 0x2)

    def lambda_33D7():
        OP_8F(0xFE, 0x12156, 0xFFFFE890, 0xFFFF3738, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_33D7)
    Sleep(2000)

    def lambda_33F7():
        OP_8F(0xFE, 0x12156, 0xFFFFE890, 0xFFFF3738, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_33F7)
    PlayEffect(0x0, 0x0, 0xA, 0, -2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    Sleep(1000)

    def lambda_3451():
        OP_8F(0xFE, 0x12156, 0xFFFFE890, 0xFFFF3738, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3451)
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

    def lambda_34C4():
        OP_6D(71790, -6370, -56090, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34C4)

    def lambda_34DC():
        OP_67(0, 6280, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34DC)

    def lambda_34F4():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34F4)

    def lambda_3504():
        OP_6C(191000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3504)

    def lambda_3514():
        OP_6E(455, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3514)
    SetChrPos(0xB, 73580, -450, -50830, 315)
    SetChrBattleFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0xC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xB, 0x0)
    OP_DC()

    ChrTalk(    #88
        0x101,
        "#1005F#5PThe tomboy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xB,
        (
            "#213F#6PWhat--aw, heck, you got away too, huh?\x02\x03",

            "#210F*sigh* I was hoping you'd stay caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1019F#1PGee, maybe I should've thrown you at them\x01",
            "as a distraction. But I don't think they'd like\x01",
            "grimy tomboys.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, 73100, -450, -51090, 315)
    SetChrPos(0xD, 73100, -450, -51090, 315)

    ChrTalk(    #91
        0xC,
        "#4PC'mon, Josette. Don't start a fight.\x02",
    )

    CloseMessageWindow()

    def lambda_369C():
        OP_6D(71160, -6550, -57510, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_369C)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0xD)
    Sleep(1500)
    OP_43(0xD, 0x1, 0x0, 0xE)
    WaitChrThread(0xD, 0x1)
    Sleep(500)

    ChrTalk(    #92
        0xD,
        (
            "#490F#6PYou won't object to a brief truce,\x01",
            "I hope, Miss Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1007F#5PYeah, well, you guys did save us back\x01",
            "there, after all.\x02\x03",

            "#1006FSo...thank you. Really.\x01",
            "We wouldn't have made it without you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        "#191F#6PHahaha! There's no need to thank us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        (
            "#210F#6PPsh, I don't remember saving YOU.\x02\x03",

            "So just keep your thanks to yourself, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1019F#5PGrrr. Okay, one of you is getting dragged\x01",
            "off to prison after all, it looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xC,
        (
            "#200F#6PThat aside. Astray, what are your\x01",
            "plans now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1026F#5PHuh?\x02",
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
            "#204F#7PWe came to ask again if you wanted\x01",
            "to come with us, but...\x02\x03",

            "#200FI'm thinking it looks like we\x01",
            "don't even need to ask, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        (
            "#1035F#2PYes...forgive me.\x02\x03",

            "#1040FI'm not really certain how things will\x01",
            "go from here...\x02\x03",

            "Right now, though, I will be traveling\x01",
            "with Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1025F#2PJoshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        "#490F#7PHeh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        (
            "#215F#7P...\x02\x03",

            "#413FAh, whatever.\x01",
            "At least there's still a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1019F#2PWhat?\x02",
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
            "#211F#6PJoshua, remember!\x02\x03",

            "You get tired of Miss Airhead over there,\x01",
            "just come on back to us!\x02\x03",

            "#415FYou'll always have a place on the Bobcat.\x01",
            "Okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1005F#5PWalk over here and call me an airhead\x01",
            "ONE MORE TIME, you greasy tomboy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        (
            "#1049F#1PHaha. Thank you, Josette!\x02\x03",

            "#1041FDon, Kyle! I owe all of you so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        "#490F#6PHah! That's our line!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xC,
        (
            "#202F#6PGood luck, and stay safe!\x01",
            "Hopefully we'll meet again someday!\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
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

    def lambda_3D79():
        OP_6D(71340, -4000, -49430, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D79)

    def lambda_3D91():
        OP_67(0, 14800, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D91)

    def lambda_3DA9():
        OP_8F(0xFE, 0x12156, 0x0, 0xFFFF3738, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3DA9)
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

    def lambda_3E9D():
        OP_6D(68970, -2760, -60770, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E9D)

    def lambda_3EB5():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3EB5)
    Sleep(200)

    def lambda_3ED5():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3ED5)
    Sleep(200)

    def lambda_3EF5():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3EF5)
    Sleep(100)

    def lambda_3F15():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F15)
    Sleep(100)

    def lambda_3F35():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F35)
    Sleep(100)

    def lambda_3F55():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F55)
    Sleep(100)

    def lambda_3F75():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F75)
    Sleep(100)

    def lambda_3F95():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F95)
    Sleep(100)

    def lambda_3FB5():
        OP_8F(0xFE, 0xC5BC, 0xBB8, 0xFFFE50A2, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3FB5)
    WaitChrThread(0xA, 0x1)
    SetMapFlags(0x2000000)
    OP_DC()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FC)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3263 end

    def Function_9_3FED(): pass

    label("Function_9_3FED")


    def lambda_3FF3():
        OP_8C(0xFE, 202, 5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3FF3)
    Sleep(400)

    def lambda_4006():
        OP_8C(0xFE, 202, 10)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4006)
    Sleep(400)

    def lambda_4019():
        OP_8C(0xFE, 202, 15)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4019)
    Sleep(400)

    def lambda_402C():
        OP_8C(0xFE, 202, 20)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_402C)
    Sleep(400)

    def lambda_403F():
        OP_8C(0xFE, 202, 30)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_403F)
    Sleep(3500)

    def lambda_4052():
        OP_8C(0xFE, 202, 20)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4052)
    Sleep(700)

    def lambda_4065():
        OP_8C(0xFE, 202, 15)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4065)
    Sleep(600)

    def lambda_4078():
        OP_8C(0xFE, 202, 10)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4078)
    Sleep(500)

    def lambda_408B():
        OP_8C(0xFE, 202, 5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_408B)
    WaitChrThread(0xA, 0x3)
    Return()

    # Function_9_3FED end

    def Function_10_4099(): pass

    label("Function_10_4099")

    ClearChrFlags(0x102, 0x80)
    SetChrPos(0x102, 51690, -4200, -43010, 90)
    OP_8E(0x102, 0xEEAC, 0xFFFFE67E, 0xFFFF5E5C, 0x7D0, 0x0)
    OP_8F(0x102, 0x111D4, 0xFFFFE8C2, 0xFFFF66B8, 0x7D0, 0x0)
    Return()

    # Function_10_4099 end

    def Function_11_40D8(): pass

    label("Function_11_40D8")

    ClearChrFlags(0x101, 0x80)
    SetChrPos(0x101, 51690, -4200, -43010, 90)
    OP_8E(0x101, 0xEEAC, 0xFFFFE67E, 0xFFFF5E5C, 0x7D0, 0x0)
    OP_8F(0x101, 0x10A2C, 0xFFFFE8CC, 0xFFFF6654, 0x7D0, 0x0)
    Return()

    # Function_11_40D8 end

    def Function_12_4117(): pass

    label("Function_12_4117")

    OP_8E(0xFE, 0x11C24, 0xFFFFFE3E, 0xFFFF3EA4, 0xBB8, 0x0)
    OP_8E(0xFE, 0x122A0, 0xFFFFFF56, 0xFFFF4A20, 0xBB8, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_12_4117 end

    def Function_13_4147(): pass

    label("Function_13_4147")

    SetChrBattleFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    OP_8E(0xC, 0x11B48, 0xFFFFFE3E, 0xFFFF3EC2, 0x7D0, 0x0)
    OP_8E(0xC, 0x12098, 0x14, 0xFFFF452A, 0x7D0, 0x0)
    OP_8C(0xC, 315, 400)
    Return()

    # Function_13_4147 end

    def Function_14_418B(): pass

    label("Function_14_418B")

    SetChrBattleFlags(0xD, 0x20)
    ClearChrFlags(0xD, 0x1)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x80)
    OP_8E(0xD, 0x11B48, 0xFFFFFE3E, 0xFFFF3EC2, 0x7D0, 0x0)
    OP_8C(0xD, 315, 400)
    Return()

    # Function_14_418B end

    def Function_15_41BB(): pass

    label("Function_15_41BB")

    OP_8E(0xFE, 0x12156, 0x28, 0xFFFF450C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x11C10, 0xFFFFFE3E, 0xFFFF3EFE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x11D8C, 0xFFFFFE3E, 0xFFFF386E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x12084, 0xFFFFFE3E, 0xFFFF3684, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_41BB end

    def Function_16_421C(): pass

    label("Function_16_421C")

    OP_8E(0xFE, 0x11A80, 0xFFFFFE3E, 0xFFFF3E2C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x11D8C, 0xFFFFFE3E, 0xFFFF386E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x12084, 0xFFFFFE3E, 0xFFFF3684, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_421C end

    def Function_17_4269(): pass

    label("Function_17_4269")

    OP_8C(0xD, 135, 400)
    OP_8E(0xFE, 0x11D8C, 0xFFFFFE3E, 0xFFFF386E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x12084, 0xFFFFFE3E, 0xFFFF3684, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_4269 end

    def Function_18_42A9(): pass

    label("Function_18_42A9")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 20)
    SetChrSubChip(0x102, 0)
    OP_82(0x80, 0x0)
    OP_C4(0x0, 0x2)
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

    def lambda_435E():
        OP_6D(71660, -5970, -39280, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_435E)

    def lambda_4376():
        OP_67(0, 5600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4376)
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
        "#1043F#6P...Estelle.\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x0, 0x2, 0x5DC)
    Sleep(500)

    ChrTalk(    #111
        0x101,
        "#1017F#4PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#1035FYou do understand that the enemies we've\x01",
            "made are overwhelmingly powerful.\x02\x03",

            "You were captured primarily as bait to\x01",
            "lure me out, I suspect.\x02\x03",

            "#1042FThat way, the Glorious wouldn't be\x01",
            "destroyed in Weissmann's absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1020F#4POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#1043F#6PAnd to be honest, Loewe probably could\x01",
            "have saved the ship AFTER kicking our\x01",
            "bodies into the sea.\x02\x03",

            "I'm fairly sure the reason he didn't...\x01",
            "was out of pity. Pity at how weak I was,\x01",
            "I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1026F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#1042FAll of the Enforcers are the same.\x02\x03",

            "In terms of pure power, they are all masters,\x01",
            "far stronger than me. Even Renne.\x02\x03",

            "We have picked what will probably be\x01",
            "the hardest fight of our lives.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x2, 0x4, 0x5DC)
    Sleep(500)

    ChrTalk(    #117
        0x101,
        "#1003F#4PYeah...\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x2, 0x4, 0x5DC)
    Sleep(300)

    ChrTalk(    #118
        0x102,
        (
            "#1053F#6PBut I do promise.\x02\x03",

            "#1040FI promise I won't ever run from\x01",
            "reality again.\x02\x03",

            "I will walk with you until the very end.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x4, 0x2, 0x5DC)
    Sleep(500)

    ChrTalk(    #119
        0x101,
        (
            "#1008F#4PJoshua...\x02\x03",

            "#1017FI promise, too! To the very end!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x2)
    OP_3F(0x411, 1)
    OP_AD(0x2400B3, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1CA9)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x128), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_EA(0x13, 0x0, 0x0, 0x0)

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4857")
    ShowSaveMenu()

    label("loc_4857")

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

    # Function_18_42A9 end

    def Function_19_4892(): pass

    label("Function_19_4892")

    EventBegin(0x1)

    ChrTalk(    #120
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_48BE():
        OP_6D(57640, -6680, -64840, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_48BE)

    def lambda_48D6():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_48D6)

    def lambda_48E6():
        OP_6C(20000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_48E6)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #121
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_498C")
    OP_C0(0xE, 0x16, 0xE9AC, 0xFFFFE5CA, 0xFFFF05F6, 0xFA, 0xD8B8, 0xFFFFE9D0, 0xFFFEFE94)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_499B")

    label("loc_498C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_499B")
    EventEnd(0x1)

    label("loc_499B")

    Return()

    # Function_19_4892 end

    SaveToFile()

Try(main)
