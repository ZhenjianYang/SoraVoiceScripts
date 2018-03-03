from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7200   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        'Sealing Stone 13',                     # 9
        'Muma Abarith',                         # 10
        'Greedy Widow',                         # 11
        'Greedy Widow',                         # 12
        'Greedy Widow',                         # 13
        'Greedy Widow',                         # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT29/CH14470 ._CH',             # 00
        'ED6_DT29/CH14471 ._CH',             # 01
        'ED6_DT29/CH15050 ._CH',             # 02
        'ED6_DT29/CH15051 ._CH',             # 03
        'ED6_DT29/CH15060 ._CH',             # 04
        'ED6_DT29/CH15061 ._CH',             # 05
        'ED6_DT29/CH14480 ._CH',             # 06
        'ED6_DT29/CH14481 ._CH',             # 07
        'ED6_DT29/CH14490 ._CH',             # 08
        'ED6_DT29/CH14491 ._CH',             # 09
        'ED6_DT29/CH14560 ._CH',             # 0A
        'ED6_DT29/CH14561 ._CH',             # 0B
        'ED6_DT29/CH14010 ._CH',             # 0C
        'ED6_DT29/CH14011 ._CH',             # 0D
        'ED6_DT26/CH20668 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT29/CH14470P._CP',             # 00
        'ED6_DT29/CH14471P._CP',             # 01
        'ED6_DT29/CH15050P._CP',             # 02
        'ED6_DT29/CH15051P._CP',             # 03
        'ED6_DT29/CH15060P._CP',             # 04
        'ED6_DT29/CH15061P._CP',             # 05
        'ED6_DT29/CH14480P._CP',             # 06
        'ED6_DT29/CH14481P._CP',             # 07
        'ED6_DT29/CH14490P._CP',             # 08
        'ED6_DT29/CH14491P._CP',             # 09
        'ED6_DT29/CH14560P._CP',             # 0A
        'ED6_DT29/CH14561P._CP',             # 0B
        'ED6_DT29/CH14010P._CP',             # 0C
        'ED6_DT29/CH14011P._CP',             # 0D
        'ED6_DT26/CH20668P._CP',             # 0E
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 110,
        Z                   = 0,
        Y                   = 52120,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35960,
        Z                   = 3550,
        Y                   = 84330,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36300,
        Z                   = -450,
        Y                   = 77900,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34730,
        Z                   = -4000,
        Y                   = 24760,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -450,
        Z                   = -13450,
        Y                   = 136360,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25510,
        Z                   = -9450,
        Y                   = 115850,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 26480,
        Z                   = -9450,
        Y                   = 117320,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -9450,
        TriggerY            = 91740,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -8150,
        ActorY              = 91740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7460,
        TriggerZ            = 0,
        TriggerY            = -130,
        TriggerRange        = 1000,
        ActorX              = 7460,
        ActorZ              = 2000,
        ActorY              = -130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36000,
        TriggerZ            = -450,
        TriggerY            = 78000,
        TriggerRange        = 1000,
        ActorX              = 36000,
        ActorZ              = 550,
        ActorY              = 78000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36000,
        TriggerZ            = 3550,
        TriggerY            = 84000,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = 4550,
        ActorY              = 84000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -25000,
        TriggerZ            = -9550,
        TriggerY            = 116000,
        TriggerRange        = 1000,
        ActorX              = -25000,
        ActorZ              = -8550,
        ActorY              = 116000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25000,
        TriggerZ            = -9550,
        TriggerY            = 116000,
        TriggerRange        = 1000,
        ActorX              = 25000,
        ActorZ              = -8550,
        ActorY              = 116000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -4000,
        TriggerY            = 78000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -3000,
        ActorY              = 78000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15820,
        TriggerZ            = -4450,
        TriggerY            = 26670,
        TriggerRange        = 1000,
        ActorX              = 15950,
        ActorZ              = -1450,
        ActorY              = 27790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3C6",          # 00, 0
        "Function_1_425",          # 01, 1
        "Function_2_5DC",          # 02, 2
        "Function_3_6F3",          # 03, 3
        "Function_4_82E",          # 04, 4
        "Function_5_96F",          # 05, 5
        "Function_6_A98",          # 06, 6
        "Function_7_C80",          # 07, 7
        "Function_8_2015",         # 08, 8
        "Function_9_207D",         # 09, 9
        "Function_10_20B1",        # 0A, 10
        "Function_11_20E5",        # 0B, 11
        "Function_12_2119",        # 0C, 12
        "Function_13_214D",        # 0D, 13
        "Function_14_2E3F",        # 0E, 14
        "Function_15_30BE",        # 0F, 15
        "Function_16_31AD",        # 10, 16
        "Function_17_328B",        # 11, 17
        "Function_18_3369",        # 12, 18
        "Function_19_3447",        # 13, 19
        "Function_20_3525",        # 14, 20
        "Function_21_35E1",        # 15, 21
        "Function_22_369D",        # 16, 22
        "Function_23_3759",        # 17, 23
        "Function_24_3815",        # 18, 24
        "Function_25_38D1",        # 19, 25
        "Function_26_39E7",        # 1A, 26
        "Function_27_3A35",        # 1B, 27
        "Function_28_3A8E",        # 1C, 28
        "Function_29_3CE1",        # 1D, 29
        "Function_30_3D9A",        # 1E, 30
    )


    def Function_0_3C6(): pass

    label("Function_0_3C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_411")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3EE"),
        (101, "loc_3F5"),
        (102, "loc_3FC"),
        (103, "loc_403"),
        (104, "loc_40A"),
        (SWITCH_DEFAULT, "loc_411"),
    )


    label("loc_3EE")

    Event(0, 15)
    Jump("loc_411")

    label("loc_3F5")

    Event(0, 16)
    Jump("loc_411")

    label("loc_3FC")

    Event(0, 19)
    Jump("loc_411")

    label("loc_403")

    Event(0, 18)
    Jump("loc_411")

    label("loc_40A")

    Event(0, 17)
    Jump("loc_411")

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_424")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_424")

    Return()

    # Function_0_3C6 end

    def Function_1_425(): pass

    label("Function_1_425")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF7360, 0x23008B)
    OP_1B(0x0, 0x0, 0x14)
    OP_1B(0x1, 0x0, 0x15)
    OP_1B(0x2, 0x0, 0x18)
    OP_1B(0x3, 0x0, 0x17)
    OP_1B(0x4, 0x0, 0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50C")
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 0, -8200, 91740, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x10, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_510")

    label("loc_50C")

    OP_64(0x0, 0x1)

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521")
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x84, 0x0)

    label("loc_521")

    OP_82(0x8A, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_534")
    OP_82(0x8B, 0x0)
    Jump("loc_537")

    label("loc_534")

    OP_82(0x8C, 0x0)

    label("loc_537")

    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570")
    OP_6F(0x5, 0)
    Jump("loc_577")

    label("loc_570")

    OP_6F(0x5, 60)

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589")
    OP_6F(0x6, 0)
    Jump("loc_590")

    label("loc_589")

    OP_6F(0x6, 60)

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A2")
    OP_6F(0x7, 0)
    Jump("loc_5A9")

    label("loc_5A2")

    OP_6F(0x7, 60)

    label("loc_5A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BB")
    OP_6F(0x8, 0)
    Jump("loc_5C2")

    label("loc_5BB")

    OP_6F(0x8, 60)

    label("loc_5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D4")
    OP_6F(0x9, 0)
    Jump("loc_5DB")

    label("loc_5D4")

    OP_6F(0x9, 60)

    label("loc_5DB")

    Return()

    # Function_1_425 end

    def Function_2_5DC(): pass

    label("Function_2_5DC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_64A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xFF\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A81)
    Jump("loc_6B2")

    label("loc_64A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xFF\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFF\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_6B2")

    Jump("loc_6E5")

    label("loc_6B5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05You're next.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xCC, 0x0)

    label("loc_6E5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_5DC end

    def Function_3_6F3(): pass

    label("Function_3_6F3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x160, 1)"), scpexpr(EXPR_END)), "loc_761")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x60\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A82)
    Jump("loc_7C9")

    label("loc_761")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x60\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x60\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_7C9")

    Jump("loc_820")

    label("loc_7CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Someone used to keep his magazine stash in here.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xCD, 0x0)

    label("loc_820")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_6F3 end

    def Function_4_82E(): pass

    label("Function_4_82E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_907")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x14E, 1)"), scpexpr(EXPR_END)), "loc_89C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x4E\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A83)
    Jump("loc_904")

    label("loc_89C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x4E\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x4E\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_904")

    Jump("loc_961")

    label("loc_907")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05I'll give ya 1,000 mira if you give back what ya took.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xCE, 0x0)

    label("loc_961")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_82E end

    def Function_5_96F(): pass

    label("Function_5_96F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A48")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x162, 1)"), scpexpr(EXPR_END)), "loc_9DD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x62\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A84)
    Jump("loc_A45")

    label("loc_9DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x62\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x62\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_A45")

    Jump("loc_A8A")

    label("loc_A48")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Your secrets are safe with me.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xCF, 0x0)

    label("loc_A8A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_96F end

    def Function_6_A98(): pass

    label("Function_6_A98")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B71")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16F, 1)"), scpexpr(EXPR_END)), "loc_B06")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\x6F\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A85)
    Jump("loc_B6E")

    label("loc_B06")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Found \x1F\x6F\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x6F\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_B6E")

    Jump("loc_C72")

    label("loc_B71")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05[16/36] His passing brought great sorrow to all but one: his son, who was\x01",
            "acutely aware that no one could surpass his father's talent. More than he\x01",
            "despised carpentry, he despised the crushing weight of his father's name.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xD0, 0x0)

    label("loc_C72")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A98 end

    def Function_7_C80(): pass

    label("Function_7_C80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp204_02.eff")
    LoadEffect(0x1, "map\\mp250_00.eff")
    LoadEffect(0x2, "map\\mp250_01.eff")
    OP_E0(238, 0x4F, 0x2)
    OP_E0(239, 0x50, 0x2)
    OP_E0(240, 0x51, 0x2)
    OP_E0(241, 0x52, 0x2)
    SetChrPos(0x10F, -150, -400, 800, 0)
    SetChrPos(0x101, 720, -400, 60, 0)
    SetChrPos(0xF0, -1190, -400, -360, 0)
    SetChrPos(0xF1, -170, -400, -1190, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(290, -400, 370, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(44000, 0)
    OP_6E(220, 0)
    Sleep(1000)
    FadeToBright(2000, 0)

    def lambda_D9A():
        OP_6D(370, -400, 390, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_D9A)

    def lambda_DB2():
        OP_67(0, 9180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_DB2)

    def lambda_DCA():
        OP_6B(3610, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_DCA)

    def lambda_DDA():
        OP_6E(250, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DDA)
    OP_0D()
    PlayEffect(0x0, 0xFF, 0xFF, -20, -400, -150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(300)

    def lambda_E2F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E2F)

    def lambda_E41():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E41)

    def lambda_E53():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E53)

    def lambda_E65():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E65)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    def lambda_E81():
        OP_6D(530, 0, 7780, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_E81)

    def lambda_E99():
        OP_67(0, 6180, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_E99)

    def lambda_EB1():
        OP_6B(3600, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_EB1)

    def lambda_EC1():
        OP_6E(255, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EC1)
    OP_43(0x10F, 0x0, 0x0, 0x9)
    Sleep(50)
    OP_43(0x101, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x0, 0xB)
    Sleep(280)
    OP_43(0xF1, 0x0, 0x0, 0xC)
    WaitChrThread(0x10F, 0x1)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #15
        0x101,
        "#1004F#6PWhere are we now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        "#1443F#5PIt seems to be another enclosed dimensional space.\x02",
    )

    CloseMessageWindow()
    OP_1D(0xDF)
    Sleep(300)
    Fade(1000)
    OP_6D(130, 0, 7670, 0)
    OP_67(0, 8820, -10000, 0)
    OP_6B(4160, 0)
    OP_6C(45000, 0)
    OP_6E(357, 0)

    def lambda_FB5():
        OP_6D(-500, -1250, 12020, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_FB5)

    def lambda_FCD():
        OP_6B(8380, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_FCD)

    def lambda_FDD():
        OP_6E(480, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_FDD)
    WaitChrThread(0x10F, 0x0)
    Fade(1000)
    OP_6D(0, 0, 10000, 0)
    OP_67(0, 7440, -10000, 0)
    OP_6B(8380, 0)
    OP_6C(0, 0)
    OP_6E(480, 0)
    SetChrPos(0x10F, -600, 0, 7870, 270)
    SetChrPos(0x101, 640, 0, 7780, 45)
    SetChrPos(0xF0, -930, 0, 5900, 225)
    SetChrPos(0xF1, 960, 0, 5870, 180)

    def lambda_1078():
        OP_6D(0, -1850, 107440, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1078)

    def lambda_1090():
        OP_67(0, 7830, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1090)

    def lambda_10A8():
        OP_6B(13020, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_10A8)

    def lambda_10B8():
        OP_6E(539, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_10B8)
    OP_C8(0x200, 0x46, "C_PLAC33._CH", 0x1, 0x3E8)
    WaitChrThread(0x10F, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(890, 0, 8130, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(45000, 0)
    OP_6E(250, 0)
    SetChrPos(0x10F, -1190, 0, 7470, 0)
    SetChrPos(0x101, 440, 0, 7580, 0)
    SetChrPos(0xF0, -1430, 0, 5900, 0)
    SetChrPos(0xF1, 460, 0, 5870, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x10F,
        (
            "#1446F#6PLike a giant labyrinth of marble in a rift between\x01",
            "dimensions.\x02\x03",

            "#1443FOr at least, that's how it appears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1007F#12PYeah... This'll be a blast to go through.\x02\x03",

            "#1002FWe're gonna need to put our backs into\x01",
            "this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        "#1446F#6PIndeed...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x10F,
        "#1441F#6PAnd quite immediately, too.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #21
        0x101,
        "#1004F#11PHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xFF, -280, 100, 14530, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_0D()

    def lambda_1324():
        OP_6D(80, 0, 11280, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1324)

    def lambda_133C():
        OP_67(0, 5410, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_133C)

    def lambda_1354():
        OP_6B(3850, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1354)

    def lambda_1364():
        OP_6C(32000, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1364)

    def lambda_1374():
        OP_6E(243, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1374)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C2")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1429")

    label("loc_13C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1429")

    label("loc_13EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1412")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1429")

    label("loc_1412")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1429")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1456")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14BD")

    label("loc_1456")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14BD")

    label("loc_147E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A6")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14BD")

    label("loc_14A6")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_14BD")

    Sleep(1000)
    OP_1D(0x97)
    OP_8C(0x101, 0, 400)
    Sleep(300)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #22
        0x101,
        "#1020F#12PWha...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1521")

    ChrTalk(    #23
        0x103,
        "#1524F#12PHere comes company!\x02",
    )

    CloseMessageWindow()
    Jump("loc_168C")

    label("loc_1521")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1550")

    ChrTalk(    #24
        0x106,
        "#054F#12PHere they come!\x02",
    )

    CloseMessageWindow()
    Jump("loc_168C")

    label("loc_1550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1583")

    ChrTalk(    #25
        0x102,
        "#1506F#12PCareful, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_168C")

    label("loc_1583")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15BB")

    ChrTalk(    #26
        0x10E,
        "#177F#12POn your guard, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_168C")

    label("loc_15BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F3")

    ChrTalk(    #27
        0x10D,
        "#271F#12POn your guard, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_168C")

    label("loc_15F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1626")

    ChrTalk(    #28
        0x10A,
        "#815F#12PHere comes company!\x02",
    )

    CloseMessageWindow()
    Jump("loc_168C")

    label("loc_1626")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_165C")

    ChrTalk(    #29
        0x105,
        "#1166F#12PBe careful, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_168C")

    label("loc_165C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168C")

    ChrTalk(    #30
        0x10B,
        "#214F#12PHere comes trouble!\x02",
    )

    CloseMessageWindow()

    label("loc_168C")

    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 15)
    SetChrSubChip(0x10F, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 17)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 18)
    SetChrSubChip(0xF1, 0)
    OP_0D()

    def lambda_16E3():
        OP_6D(80, 0, 13000, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_16E3)

    def lambda_16FB():
        OP_6B(3480, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_16FB)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -480, -3000, 14530, 180)
    OP_22(0x85, 0x1, 0x64)
    OP_43(0x11, 0x0, 0x0, 0x8)
    WaitChrThread(0x11, 0x0)
    OP_23(0x85)
    WaitChrThread(0x10F, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(-100, 300, 8420, 0)
    OP_67(0, 4540, -10000, 0)
    OP_6B(8000, 0)
    OP_6C(0, 0)
    OP_6E(119, 0)
    SetChrPos(0x10F, -600, 0, 7870, 0)
    SetChrPos(0x101, 640, 0, 7780, 0)
    SetChrPos(0xF0, -930, 0, 5900, 0)
    SetChrPos(0xF1, 960, 0, 5870, 0)
    SetChrPos(0x11, 0, 0, 14530, 180)

    def lambda_17E4():
        OP_6B(8600, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_17E4)
    Sleep(500)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x12, 6120, 9000, 4440, 270)
    SetChrPos(0x13, 4080, 9000, 1620, 315)
    SetChrPos(0x14, -3400, 9000, 1610, 45)
    SetChrPos(0x15, -6270, 9000, 5380, 90)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1856():
        OP_96(0xFE, 0x17E8, 0x0, 0x1158, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1856)
    Sleep(50)
    OP_22(0x99, 0x0, 0x64)

    def lambda_187E():
        OP_96(0xFE, 0xFFFFEDCC, 0xFFFFFF38, 0x758, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_187E)
    Sleep(50)
    OP_22(0x99, 0x0, 0x64)

    def lambda_18A6():
        OP_96(0xFE, 0xFF0, 0x0, 0x654, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_18A6)
    Sleep(50)
    OP_22(0x99, 0x0, 0x64)

    def lambda_18CE():
        OP_96(0xFE, 0xFFFFE782, 0x0, 0x1504, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_18CE)
    Sleep(50)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    WaitChrThread(0x12, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_190F():

        label("loc_190F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_190F")

    QueueWorkItem2(0x12, 3, lambda_190F)
    WaitChrThread(0x14, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_192C():

        label("loc_192C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_192C")

    QueueWorkItem2(0x14, 3, lambda_192C)
    WaitChrThread(0x13, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1949():

        label("loc_1949")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1949")

    QueueWorkItem2(0x13, 3, lambda_1949)
    WaitChrThread(0x15, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1966():

        label("loc_1966")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1966")

    QueueWorkItem2(0x15, 3, lambda_1966)

    def lambda_1979():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1979)
    Sleep(100)

    def lambda_198C():
        OP_8C(0xFE, 135, 600)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_198C)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #31
        0x10F,
        (
            "#1446F#6PThese are dream spiders!\x02\x03",

            "#1441FThey're foul beasts that devour people's dreams\x01",
            "and replace them with nightmares!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1007F#6PWell, this plane's off to an AWESOME start...\x02\x03",

            "#1006FWell, whatever. Let's kick some devil butt!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1A98():
        OP_6D(0, 0, 8790, 300)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1A98)

    def lambda_1AB0():
        OP_67(0, 4810, -10000, 300)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1AB0)

    def lambda_1AC8():
        OP_6B(6430, 300)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1AC8)

    def lambda_1AD8():
        OP_6E(112, 300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1AD8)
    SetChrChipByIndex(0x11, 1)

    def lambda_1AED():
        OP_8F(0xFE, 0xFFFFFFEC, 0x0, 0x245E, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1AED)
    Sleep(20)
    SetChrChipByIndex(0x12, 3)

    def lambda_1B12():
        OP_8F(0xFE, 0x7F8, 0x0, 0x19AA, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1B12)
    Sleep(20)
    SetChrChipByIndex(0x14, 3)

    def lambda_1B37():
        OP_8F(0xFE, 0xFFFFFB28, 0x0, 0x1590, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1B37)
    Sleep(20)
    SetChrChipByIndex(0x13, 3)

    def lambda_1B5C():
        OP_8F(0xFE, 0x4CE, 0x0, 0x164E, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1B5C)
    Sleep(20)
    SetChrChipByIndex(0x15, 3)

    def lambda_1B81():
        OP_8F(0xFE, 0xFFFFF880, 0x0, 0x1734, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1B81)
    WaitChrThread(0x10F, 0x1)
    WaitChrThread(0x10F, 0x2)
    WaitChrThread(0x10F, 0x3)
    Battle(0x21C, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_1D(0xDF)
    EventBegin(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_E0(238, 0x4F, 0x2)
    OP_E0(239, 0x50, 0x2)
    OP_E0(240, 0x51, 0x2)
    OP_E0(241, 0x52, 0x2)
    SetChrPos(0x10F, -1190, 0, 7470, 0)
    SetChrPos(0x101, 440, 0, 7580, 0)
    SetChrPos(0xF0, -1430, 0, 5900, 225)
    SetChrPos(0xF1, 460, 0, 5870, 180)
    SetChrChipByIndex(0x10F, 15)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF0, 17)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 18)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Sleep(1000)
    OP_6D(800, 0, 8000, 0)
    OP_67(0, 5990, -10000, 0)
    OP_6B(4100, 0)
    OP_6C(45000, 0)
    OP_6E(235, 0)

    def lambda_1CC3():
        OP_6B(3600, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1CC3)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x2)
    Sleep(300)

    ChrTalk(    #33
        0x10F,
        "#1445F#6PI think that was the last of them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1007F#12PWhew... I'm bushed.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    def lambda_1D93():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D93)
    Sleep(100)

    def lambda_1DA6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1DA6)
    Sleep(100)
    OP_8C(0xF0, 0, 400)
    Sleep(300)

    ChrTalk(    #35
        0x101,
        (
            "#1002F#11PSo were those the kinda devils you were\x01",
            "talking about back in the garden?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #36
        0x10F,
        (
            "#1802F#6PMore specifically, it's a subspecies of devils\x01",
            "known as dream devils.\x02\x03",

            "They're said to specialize in attacking the mind,\x01",
            "and I think we've confirmed that to be perfectly\x01",
            "accurate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1015F#11PWe're gonna need to put in more than our backs\x01",
            "at this rate...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #38
        0x101,
        (
            "#1006F#11PHow about we double check our equipment one\x01",
            "last time before we head on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        (
            "#1447F#6PThat certainly sounds wise.\x02\x01",

            "#1448FThere's no such thing as being too cautious.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2A02)
    OP_28(0x35, 0x1, 0x4)
    OP_28(0x35, 0x1, 0x8)
    OP_28(0x35, 0x1, 0x10)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xDE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_C80 end

    def Function_8_2015(): pass

    label("Function_8_2015")

    PlayEffect(0x2, 0x4, 0xFF, -280, 100, 14530, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_2050():

        label("loc_2050")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2050")

    QueueWorkItem2(0xFE, 1, lambda_2050)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_2015 end

    def Function_9_207D(): pass

    label("Function_9_207D")

    OP_8E(0xFE, 0xFFFFFB5A, 0x0, 0x1D2E, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_207D end

    def Function_10_20B1(): pass

    label("Function_10_20B1")

    OP_8E(0xFE, 0x1B8, 0x0, 0x1D9C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_10_20B1 end

    def Function_11_20E5(): pass

    label("Function_11_20E5")

    OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x170C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_11_20E5 end

    def Function_12_2119(): pass

    label("Function_12_2119")

    OP_8E(0xFE, 0x1CC, 0x0, 0x16EE, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_12_2119 end

    def Function_13_214D(): pass

    label("Function_13_214D")

    EventBegin(0x0)
    Fade(500)
    OP_6D(1340, -9450, 94300, 0)
    OP_67(0, 5110, -10000, 0)
    OP_6B(4710, 0)
    OP_6C(45000, 0)
    OP_6E(170, 0)
    SetChrPos(0x10F, 90, -9450, 94130, 180)
    SetChrPos(0x101, -1030, -9450, 94640, 180)
    SetChrPos(0xF1, 2080, -9200, 95100, 225)
    SetChrPos(0xF0, 390, -9200, 95430, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    OP_8E(0x10F, 0xFFFFFFF6, 0xFFFFDB16, 0x16AE4, 0x3E8, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x10F, 14)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x10, 0x82, 0xFFFFDECC, 0x169D6, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x10, 0x80)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05Found \x1F\x5E\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35E, 1)
    OP_64(0x0, 0x1)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #41
        0x10F,
        "#1444F#5PAnother stone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1011F#5PWow... That thing sure is pretty.\x02\x03",

            "Is it some kind of septium?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2329():
        OP_6D(1200, -9450, 95200, 800)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2329)
    OP_8C(0x10F, 0, 400)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #43
        0x10F,
        (
            "#1446F#12PNo. It's what's known as a sealing stone.\x02\x03",

            "#1448FYou were inside one just like this when we\x01",
            "found you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x101,
        (
            "#1004F#5PI-I was?!\x02\x03",

            "#1006FAre we gonna find someone in this one, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10F,
        (
            "#1447F#12PWithout a doubt.\x02\x03",

            "#1448FYou wouldn't happen to have any inkling as to\x01",
            "who it could be, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1015F#5PLet me think...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253F")

    ChrTalk(    #47
        0x102,
        (
            "#1505F#5PIt'd be nice if it was Dad...\x02\x03",

            "#1514F...but I doubt we'd get that lucky.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #48
        0x101,
        "#1016F#6PAhaha... Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FD")

    label("loc_253F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2614")

    ChrTalk(    #49
        0x106,
        (
            "#551F#5PHey, Estelle...\x02\x03",

            "#555FYou don't think it could be your old man,\x01",
            "do you?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #50
        0x101,
        (
            "#1016F#6PHe'd be a real big help right about now...\x02\x03",

            "#1025FI don't think we're THAT lucky, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FD")

    label("loc_2614")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26EA")

    ChrTalk(    #51
        0x103,
        (
            "#1526F#5PSay, Estelle...\x02\x03",

            "#1527FYou don't think it could be your father, do you?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #52
        0x101,
        (
            "#1016F#6PHe'd be a real big help right about now...\x02\x03",

            "#1025FI don't think we're THAT lucky, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FD")

    label("loc_26EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_279A")

    ChrTalk(    #53
        0x108,
        (
            "#573F#5PIt'd be great if it were Master Cassius...\x02\x03",

            "#070F...but I'm guessing we're not going to get\x01",
            "quite that lucky.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #54
        0x101,
        "#1016F#6PAhaha... Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FD")

    label("loc_279A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_286F")

    ChrTalk(    #55
        0x10E,
        (
            "#179F#5PIt would be wonderful if it was Brigadier General\x01",
            "Bright, given his strength...\x02\x03",

            "#170F...but I suppose that may be a little too much to \x01",
            "hope for.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #56
        0x101,
        "#1016F#6PAhaha... Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FD")

    label("loc_286F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2941")

    ChrTalk(    #57
        0x104,
        (
            "#1545F#5PHmm...\x02\x03",

            "#1540FYou don't think it could be Cassius, do you,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1016F#6PHe'd be a real big help right about now...\x02\x03",

            "#1025FI don't think we're THAT lucky, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FD")

    label("loc_2941")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29FD")

    ChrTalk(    #59
        0x105,
        (
            "#1165F#5PIt would be wonderful if it were your dad with\x01",
            "how strong he is...\x02\x03",

            "#1382F...but that may be a little too much to hope for.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #60
        0x101,
        "#1016F#6PAhaha... Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_29FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B0D")

    ChrTalk(    #61
        0x107,
        "#064F#5PCould Grandpa be inside?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #62
        0x101,
        (
            "#1006F#6PWell, it's true that he's busted us out of a\x01",
            "jam plenty of times in the past...\x02\x03",

            "#1015FWasn't he out of the country on vacation,\x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x107,
        (
            "#560F#5POh, yeah. You're right.\x02\x03",

            "#561FMaybe not, then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BAC")
    OP_62(0x10A, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #64
        0x10A,
        "#1310F#5PMaybe it could be Kurt!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1006F#6PIt might just be! I don't see any reason why\x01",
            "it wouldn't.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C7E")

    ChrTalk(    #66
        0x10B,
        (
            "#216F#5PY-You don't think it could be my brothers,\x01",
            "do you?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #67
        0x101,
        (
            "#1004F#6PThat'd actually make sense, I guess.\x02\x03",

            "#1006FThey did help us out when we were on the \x01",
            "Liber Ark, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D59")

    label("loc_2C7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D59")

    ChrTalk(    #68
        0x10D,
        (
            "#272F#5PHmm...\x02\x03",

            "#277FPerhaps it could be the remaining members\x01",
            "of the sky bandits?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #69
        0x101,
        (
            "#1004F#6PThat'd make sense, I guess.\x02\x03",

            "#1006FThey did help us out when we were on the \x01",
            "Liber Ark and all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D59")


    ChrTalk(    #70
        0x10F,
        (
            "#1446F#12P...It sounds as though there are a number of \x01",
            "possibilities.\x02\x03",

            "#1448FAnd the fastest way to find out which one rings\x01",
            "true is to take this back to the garden.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(300)

    ChrTalk(    #71
        0x101,
        "#1006F#5PThen let's go!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2A03)
    OP_28(0x35, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_13_214D end

    def Function_14_2E3F(): pass

    label("Function_14_2E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0E")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(3840)
    Sleep(500)
    TalkBegin(0xFF)

    label("loc_2F0E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #72
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308D")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FA6"),
        (1, "loc_3021"),
        (2, "loc_304F"),
        (SWITCH_DEFAULT, "loc_307D"),
    )


    label("loc_2FA6")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_308A")

    label("loc_3021")

    OP_A9(0x22)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #73
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_308A")

    label("loc_304F")

    OP_A9(0x8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #74
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_308A")

    label("loc_307D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_308A")

    label("loc_308A")

    Jump("loc_2F4A")

    label("loc_308D")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BA")
    OP_A2(0x2592)
    EventEnd(0x1)
    Jump("loc_30BD")

    label("loc_30BA")

    TalkEnd(0xFF)

    label("loc_30BD")

    Return()

    # Function_14_2E3F end

    def Function_15_30BE(): pass

    label("Function_15_30BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30CF")
    Call(0, 7)
    Return()

    label("loc_30CF")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -150, -400, 800, 0)
    SetChrPos(0x1, 720, -400, 60, 0)
    SetChrPos(0x2, -1190, -400, -360, 0)
    SetChrPos(0x3, -170, -400, -1190, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -20, -400, -150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 25)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_15_30BE end

    def Function_16_31AD(): pass

    label("Function_16_31AD")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -16100, -4350, 23960, 270)
    SetChrPos(0x1, -16100, -4350, 23960, 270)
    SetChrPos(0x2, -16100, -4350, 23960, 270)
    SetChrPos(0x3, -16100, -4350, 23960, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -16100, -4350, 23960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 25)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_16_31AD end

    def Function_17_328B(): pass

    label("Function_17_328B")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -90, -9350, 181790, 180)
    SetChrPos(0x1, -90, -9350, 181790, 180)
    SetChrPos(0x2, -90, -9350, 181790, 180)
    SetChrPos(0x3, -90, -9350, 181790, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -90, -9350, 181790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 25)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_17_328B end

    def Function_18_3369(): pass

    label("Function_18_3369")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -50580, -9350, 141310, 135)
    SetChrPos(0x1, -50580, -9350, 141310, 135)
    SetChrPos(0x2, -50580, -9350, 141310, 135)
    SetChrPos(0x3, -50580, -9350, 141310, 135)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -50580, -9350, 141310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 25)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_18_3369 end

    def Function_19_3447(): pass

    label("Function_19_3447")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 50410, -9350, 141370, 225)
    SetChrPos(0x1, 50410, -9350, 141370, 225)
    SetChrPos(0x2, 50410, -9350, 141370, 225)
    SetChrPos(0x3, 50410, -9350, 141370, 225)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 50410, -9350, 141370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 25)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_19_3447 end

    def Function_20_3525(): pass

    label("Function_20_3525")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -150, -400, 800, 180)
    SetChrPos(0x2, 720, -400, 60, 180)
    SetChrPos(0x1, -1190, -400, -360, 180)
    SetChrPos(0x0, -170, -400, -1190, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -20, -400, -150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 26)
    NewScene("ED6_DT21/U5102   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_20_3525 end

    def Function_21_35E1(): pass

    label("Function_21_35E1")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -16100, -4350, 23960, 90)
    SetChrPos(0x2, -16100, -4350, 23960, 90)
    SetChrPos(0x1, -16100, -4350, 23960, 90)
    SetChrPos(0x0, -16100, -4350, 23960, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -16100, -4350, 23960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 26)
    NewScene("ED6_DT21/M7201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_35E1 end

    def Function_22_369D(): pass

    label("Function_22_369D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -90, -9350, 181790, 0)
    SetChrPos(0x2, -90, -9350, 181790, 0)
    SetChrPos(0x1, -90, -9350, 181790, 0)
    SetChrPos(0x0, -90, -9350, 181790, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -90, -9350, 181790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 26)
    NewScene("ED6_DT21/M7201   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_22_369D end

    def Function_23_3759(): pass

    label("Function_23_3759")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -50580, -9350, 141310, 315)
    SetChrPos(0x2, -50580, -9350, 141310, 315)
    SetChrPos(0x1, -50580, -9350, 141310, 315)
    SetChrPos(0x0, -50580, -9350, 141310, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -50580, -9350, 141310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 26)
    NewScene("ED6_DT21/M7201   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3759 end

    def Function_24_3815(): pass

    label("Function_24_3815")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 50410, -9350, 141370, 45)
    SetChrPos(0x2, 50410, -9350, 141370, 45)
    SetChrPos(0x1, 50410, -9350, 141370, 45)
    SetChrPos(0x0, 50410, -9350, 141370, 45)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 50410, -9350, 141370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 26)
    NewScene("ED6_DT21/M7201   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3815 end

    def Function_25_38D1(): pass

    label("Function_25_38D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38FA")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_38EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_38EE)

    label("loc_38FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3923")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3917():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3917)

    label("loc_3923")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_394C")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3940():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3940)

    label("loc_394C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3975")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3969():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3969)

    label("loc_3975")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39A1")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_39A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39B8")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_39B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39CF")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_39CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39E6")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_39E6")

    Return()

    # Function_25_38D1 end

    def Function_26_39E7(): pass

    label("Function_26_39E7")


    def lambda_39ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_39ED)

    def lambda_39FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_39FF)

    def lambda_3A11():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3A11)

    def lambda_3A23():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3A23)
    Sleep(1000)
    Return()

    # Function_26_39E7 end

    def Function_27_3A35(): pass

    label("Function_27_3A35")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #75
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_27_3A35 end

    def Function_28_3A8E(): pass

    label("Function_28_3A8E")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 16990, -4450, 25520, 0)
    SetChrPos(0x1, 14670, -4450, 25470, 0)
    SetChrPos(0x2, 16550, -4450, 23330, 0)
    SetChrPos(0x3, 14510, -4450, 23100, 0)
    OP_6D(15390, -4450, 25860, 0)
    OP_67(0, 6200, -10000, 0)
    OP_6B(5350, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B64")
    OP_28(0x15, 0x4, 0x2)
    OP_82(0x8B, 0x2)
    PlayEffect(0x8C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_3B64")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_3BEB")

    AnonymousTalk(    #76
        (
            "\x07\x05#40WThe path has already been opened...\x01",
            "#500W \x01",
            "#40WOpen the door, and step inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CAC")

    label("loc_3BEB")


    AnonymousTalk(    #77
        (
            "\x07\x05#40WAll may set foot within this door; to lay claim to its\x01",
            "rewards, however, you must first overcome a trial.\x01",
            "#500W \x01",
            "#40WShould this fail to deter you, open the door,\x01",
            "and step inside...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CAC")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Call(0, 27)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD5")
    Call(0, 29)

    label("loc_3CD5")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_28_3A8E end

    def Function_29_3CE1(): pass

    label("Function_29_3CE1")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0xA)
    Sleep(500)

    def lambda_3D4A():
        OP_6B(4360, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3D4A)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_23(0x85)
    OP_E3(0x0, 0x20, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3CE1 end

    def Function_30_3D9A(): pass

    label("Function_30_3D9A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 16990, -4450, 25520, 0)
    SetChrPos(0x1, 14670, -4450, 25470, 0)
    SetChrPos(0x2, 16550, -4450, 23330, 0)
    SetChrPos(0x3, 14510, -4450, 23100, 0)
    OP_6D(15390, -4450, 25860, 0)
    OP_67(0, 6200, -10000, 0)
    OP_6B(5350, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_30_3D9A end

    SaveToFile()

Try(main)
