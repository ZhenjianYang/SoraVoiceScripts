from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2400   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2400.x',
        MapIndex            = 103,
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
        'Ruan',                                 # 9
        'Air-Letten',                           # 10
        'Sapphirl Tower',                       # 11
        'Fungo',                                # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
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
        'ED6_DT09/CH10520 ._CH',             # 00
        'ED6_DT09/CH10521 ._CH',             # 01
        'ED6_DT29/CH12040 ._CH',             # 02
        'ED6_DT29/CH12041 ._CH',             # 03
        'ED6_DT09/CH10340 ._CH',             # 04
        'ED6_DT09/CH10341 ._CH',             # 05
        'ED6_DT09/CH11040 ._CH',             # 06
        'ED6_DT09/CH11041 ._CH',             # 07
        'ED6_DT09/CH11070 ._CH',             # 08
        'ED6_DT09/CH11071 ._CH',             # 09
        'ED6_DT09/CH11080 ._CH',             # 0A
        'ED6_DT09/CH11081 ._CH',             # 0B
        'ED6_DT09/CH11020 ._CH',             # 0C
        'ED6_DT09/CH11021 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT09/CH10520P._CP',             # 00
        'ED6_DT09/CH10521P._CP',             # 01
        'ED6_DT29/CH12040P._CP',             # 02
        'ED6_DT29/CH12041P._CP',             # 03
        'ED6_DT09/CH10340P._CP',             # 04
        'ED6_DT09/CH10341P._CP',             # 05
        'ED6_DT09/CH11040P._CP',             # 06
        'ED6_DT09/CH11041P._CP',             # 07
        'ED6_DT09/CH11070P._CP',             # 08
        'ED6_DT09/CH11071P._CP',             # 09
        'ED6_DT09/CH11080P._CP',             # 0A
        'ED6_DT09/CH11081P._CP',             # 0B
        'ED6_DT09/CH11020P._CP',             # 0C
        'ED6_DT09/CH11021P._CP',             # 0D
    )

    DeclNpc(
        X                   = -23690,
        Z                   = 0,
        Y                   = 116780,
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
        X                   = 15400,
        Z                   = 0,
        Y                   = 4440,
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
        X                   = -104100,
        Z                   = 10,
        Y                   = 74970,
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
        X                   = -8500,
        Z                   = 710,
        Y                   = 63340,
        Direction           = 264,
        Unknown2            = 12,
        Unknown3            = 786432,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -14830,
        Z                   = -70,
        Y                   = 77800,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28100,
        Z                   = 190,
        Y                   = 43720,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1A5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15760,
        Z                   = -60,
        Y                   = 37690,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1A7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28480,
        Z                   = 130,
        Y                   = 9940,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1A9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14420,
        Z                   = 200,
        Y                   = 18840,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40650,
        Z                   = 450,
        Y                   = 58610,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1A5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -66830,
        Z                   = 20,
        Y                   = 39070,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1AA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -8500,
        Y                   = -1000,
        Z                   = 63340,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -31880,
        TriggerZ            = 0,
        TriggerY            = 74800,
        TriggerRange        = 1500,
        ActorX              = -31880,
        ActorZ              = 1400,
        ActorY              = 74800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28300,
        TriggerZ            = 0,
        TriggerY            = 68920,
        TriggerRange        = 1500,
        ActorX              = -28300,
        ActorZ              = 1500,
        ActorY              = 68920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2C6",          # 00, 0
        "Function_1_2C7",          # 01, 1
        "Function_2_30A",          # 02, 2
        "Function_3_320",          # 03, 3
        "Function_4_4EF",          # 04, 4
        "Function_5_54C",          # 05, 5
    )


    def Function_0_2C6(): pass

    label("Function_0_2C6")

    Return()

    # Function_0_2C6 end

    def Function_1_2C7(): pass

    label("Function_1_2C7")

    OP_16(0x2, 0xFA0, 0xFFFD73A8, 0xFFFECF50, 0x230023)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F7")
    SetChrFlags(0xB, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_309")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309")
    ClearChrFlags(0xB, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_309")

    Return()

    # Function_1_2C7 end

    def Function_2_30A(): pass

    label("Function_2_30A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_30A")

    label("loc_31F")

    Return()

    # Function_2_30A end

    def Function_3_320(): pass

    label("Function_3_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 5)), scpexpr(EXPR_END)), "loc_328")
    Return()

    label("loc_328")

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
        (1, "loc_41C"),
        (SWITCH_DEFAULT, "loc_43F"),
    )


    label("loc_41C")

    Fade(500)
    OP_89(0x0, -15310, 0, 63620, 90)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_43F")

    Battle(0xEE0, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -15310, 0, 63620, 90)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_478"),
        (1, "loc_47B"),
        (SWITCH_DEFAULT, "loc_47E"),
    )


    label("loc_478")

    EventEnd(0x0)
    Return()

    label("loc_47B")

    OP_B4(0x0)
    Return()

    label("loc_47E")

    EventBegin(0x1)
    SetChrFlags(0xB, 0x80)
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
    OP_A2(0x12FD)
    OP_28(0xA4, 0x4, 0x10)
    OP_28(0xA4, 0x4, 0x2)
    OP_28(0xA4, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_320 end

    def Function_4_4EF(): pass

    label("Function_4_4EF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        (
            "\x07\x05West: Sapphirl Tower\x01",
            "※Beware of Monsters!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_4EF end

    def Function_5_54C(): pass

    label("Function_5_54C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x05North: City of Ruan - 105 selge\x01",
            "South: Air-Letten - 70 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_54C end

    SaveToFile()

Try(main)
