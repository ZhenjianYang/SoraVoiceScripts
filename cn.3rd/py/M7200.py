from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '封印石? ',                             # 9
        '梦魔·贪婪',                           # 10
        '贪婪毒蜘蛛',                           # 11
        '贪婪毒蜘蛛',                           # 12
        '贪婪毒蜘蛛',                           # 13
        '贪婪毒蜘蛛',                           # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
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
        "Function_3_702",          # 03, 3
        "Function_4_828",          # 04, 4
        "Function_5_94E",          # 05, 5
        "Function_6_A74",          # 06, 6
        "Function_7_B9A",          # 07, 7
        "Function_8_1E44",         # 08, 8
        "Function_9_1EAC",         # 09, 9
        "Function_10_1EE0",        # 0A, 10
        "Function_11_1F14",        # 0B, 11
        "Function_12_1F48",        # 0C, 12
        "Function_13_1F7C",        # 0D, 13
        "Function_14_2BD7",        # 0E, 14
        "Function_15_2E6C",        # 0F, 15
        "Function_16_2F5B",        # 10, 16
        "Function_17_3039",        # 11, 17
        "Function_18_3117",        # 12, 18
        "Function_19_31F5",        # 13, 19
        "Function_20_32D3",        # 14, 20
        "Function_21_338F",        # 15, 21
        "Function_22_344B",        # 16, 22
        "Function_23_3507",        # 17, 23
        "Function_24_35C3",        # 18, 24
        "Function_25_367F",        # 19, 25
        "Function_26_3795",        # 1A, 26
        "Function_27_37E3",        # 1B, 27
        "Function_28_3857",        # 1C, 28
        "Function_29_3A5C",        # 1D, 29
        "Function_30_3B15",        # 1E, 30
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_650")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    Jump("loc_635")

    label("loc_635")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A81)
    Jump("loc_6BE")

    label("loc_650")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFF\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_69F")

    label("loc_69F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_6BE")

    Jump("loc_6F4")

    label("loc_6C1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6F4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_5DC end

    def Function_3_702(): pass

    label("Function_3_702")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x160, 1)"), scpexpr(EXPR_END)), "loc_776")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x60\x01\x07\x00。\x02",
    )

    Jump("loc_75B")

    label("loc_75B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A82)
    Jump("loc_7E4")

    label("loc_776")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x60\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x60\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_7C5")

    label("loc_7C5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_7E4")

    Jump("loc_81A")

    label("loc_7E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_81A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_702 end

    def Function_4_828(): pass

    label("Function_4_828")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x14E, 1)"), scpexpr(EXPR_END)), "loc_89C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x4E\x01\x07\x00。\x02",
    )

    Jump("loc_881")

    label("loc_881")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A83)
    Jump("loc_90A")

    label("loc_89C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x4E\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x4E\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_8EB")

    label("loc_8EB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_90A")

    Jump("loc_940")

    label("loc_90D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_940")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_828 end

    def Function_5_94E(): pass

    label("Function_5_94E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A33")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x162, 1)"), scpexpr(EXPR_END)), "loc_9C2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x62\x01\x07\x00。\x02",
    )

    Jump("loc_9A7")

    label("loc_9A7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A84)
    Jump("loc_A30")

    label("loc_9C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x62\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x62\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_A11")

    label("loc_A11")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_A30")

    Jump("loc_A66")

    label("loc_A33")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A66")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_94E end

    def Function_6_A74(): pass

    label("Function_6_A74")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x550, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B59")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16F, 1)"), scpexpr(EXPR_END)), "loc_AE8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\x6F\x01\x07\x00。\x02",
    )

    Jump("loc_ACD")

    label("loc_ACD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A85)
    Jump("loc_B56")

    label("loc_AE8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\x6F\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x6F\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_B37")

    label("loc_B37")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_B56")

    Jump("loc_B8C")

    label("loc_B59")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B8C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A74 end

    def Function_7_B9A(): pass

    label("Function_7_B9A")

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

    def lambda_CB4():
        OP_6D(370, -400, 390, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_CB4)

    def lambda_CCC():
        OP_67(0, 9180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_CCC)

    def lambda_CE4():
        OP_6B(3610, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_CE4)

    def lambda_CF4():
        OP_6E(250, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CF4)
    OP_0D()
    PlayEffect(0x0, 0xFF, 0xFF, -20, -400, -150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(300)

    def lambda_D49():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D49)

    def lambda_D5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D5B)

    def lambda_D6D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D6D)

    def lambda_D7F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_D7F)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    def lambda_D9B():
        OP_6D(530, 0, 7780, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_D9B)

    def lambda_DB3():
        OP_67(0, 6180, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_DB3)

    def lambda_DCB():
        OP_6B(3600, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_DCB)

    def lambda_DDB():
        OP_6E(255, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DDB)
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
        "#1004F#6P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        (
            "#1443F#5P果然……\x01",
            "是异空间没错啊。\x02",
        )
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

    def lambda_EBB():
        OP_6D(-500, -1250, 12020, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_EBB)

    def lambda_ED3():
        OP_6B(8380, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_ED3)

    def lambda_EE3():
        OP_6E(480, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_EE3)
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

    def lambda_F7E():
        OP_6D(0, -1850, 107440, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_F7E)

    def lambda_F96():
        OP_67(0, 7830, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_F96)

    def lambda_FAE():
        OP_6B(13020, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_FAE)

    def lambda_FBE():
        OP_6E(539, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_FBE)
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
            "#1446F#6P用大理石砌成的\x01",
            "处于次元狭缝中的迷宫……\x02\x03",

            "#1443F是这样一种场景吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1007F#12P嗯……\x01",
            "看上去构造也好像相当复杂啊。\x02\x03",

            "#1002F看来我们要\x01",
            "鼓足干劲挑战才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        "#1446F#6P没错……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x10F,
        "#1441F#6P……这种气息是……！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #21
        0x101,
        "#1004F#11P哎……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xFF, -280, 100, 14530, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_0D()

    def lambda_1216():
        OP_6D(80, 0, 11280, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1216)

    def lambda_122E():
        OP_67(0, 5410, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_122E)

    def lambda_1246():
        OP_6B(3850, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1246)

    def lambda_1256():
        OP_6C(32000, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1256)

    def lambda_1266():
        OP_6E(243, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1266)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B4")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_131B")

    label("loc_12B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DC")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_131B")

    label("loc_12DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1304")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_131B")

    label("loc_1304")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_131B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1348")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13AF")

    label("loc_1348")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1370")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13AF")

    label("loc_1370")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1398")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13AF")

    label("loc_1398")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_13AF")

    Sleep(1000)
    OP_1D(0x97)
    OP_8C(0x101, 0, 400)
    Sleep(300)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #22
        0x101,
        "#1020F#12P什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_141E")

    ChrTalk(    #23
        0x103,
        "#1524F#12P来了吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_141E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144F")

    ChrTalk(    #24
        0x106,
        "#054F#12P来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_144F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1485")

    ChrTalk(    #25
        0x102,
        "#1506F#12P……来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_1485")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B6")

    ChrTalk(    #26
        0x10E,
        "#177F#12P来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_14B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E7")

    ChrTalk(    #27
        0x10D,
        "#271F#12P来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_14E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1520")

    ChrTalk(    #28
        0x10A,
        "#815F#12P这么快就来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_1520")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1552")

    ChrTalk(    #29
        0x105,
        "#1166F#12P来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_1552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1580")

    ChrTalk(    #30
        0x10B,
        "#214F#12P来了……！\x02",
    )

    CloseMessageWindow()

    label("loc_1580")

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

    def lambda_15D7():
        OP_6D(80, 0, 13000, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_15D7)

    def lambda_15EF():
        OP_6B(3480, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_15EF)
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

    def lambda_16D8():
        OP_6B(8600, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_16D8)
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

    def lambda_174A():
        OP_96(0xFE, 0x17E8, 0x0, 0x1158, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_174A)
    Sleep(50)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1772():
        OP_96(0xFE, 0xFFFFEDCC, 0xFFFFFF38, 0x758, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1772)
    Sleep(50)
    OP_22(0x99, 0x0, 0x64)

    def lambda_179A():
        OP_96(0xFE, 0xFF0, 0x0, 0x654, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_179A)
    Sleep(50)
    OP_22(0x99, 0x0, 0x64)

    def lambda_17C2():
        OP_96(0xFE, 0xFFFFE782, 0x0, 0x1504, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_17C2)
    Sleep(50)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    WaitChrThread(0x12, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1803():

        label("loc_1803")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1803")

    QueueWorkItem2(0x12, 3, lambda_1803)
    WaitChrThread(0x14, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1820():

        label("loc_1820")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1820")

    QueueWorkItem2(0x14, 3, lambda_1820)
    WaitChrThread(0x13, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_183D():

        label("loc_183D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_183D")

    QueueWorkItem2(0x13, 3, lambda_183D)
    WaitChrThread(0x15, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_185A():

        label("loc_185A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_185A")

    QueueWorkItem2(0x15, 3, lambda_185A)

    def lambda_186D():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_186D)
    Sleep(100)

    def lambda_1880():
        OP_8C(0xFE, 135, 600)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1880)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #31
        0x10F,
        (
            "#1446F#6P梦魔和梦蜘蛛……\x02\x03",

            "#1441F吞噬人类的梦，\x01",
            "并为人类带来梦魇的怪物……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1007F#6P一上来就出现\x01",
            "这么难缠的对手……\x02\x03",

            "#1006F算了，我不会手下留情的。\x01",
            "看我把你们全部打飞！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_196E():
        OP_6D(0, 0, 8790, 300)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_196E)

    def lambda_1986():
        OP_67(0, 4810, -10000, 300)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1986)

    def lambda_199E():
        OP_6B(6430, 300)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_199E)

    def lambda_19AE():
        OP_6E(112, 300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_19AE)
    SetChrChipByIndex(0x11, 1)

    def lambda_19C3():
        OP_8F(0xFE, 0xFFFFFFEC, 0x0, 0x245E, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_19C3)
    Sleep(20)
    SetChrChipByIndex(0x12, 3)

    def lambda_19E8():
        OP_8F(0xFE, 0x7F8, 0x0, 0x19AA, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_19E8)
    Sleep(20)
    SetChrChipByIndex(0x14, 3)

    def lambda_1A0D():
        OP_8F(0xFE, 0xFFFFFB28, 0x0, 0x1590, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1A0D)
    Sleep(20)
    SetChrChipByIndex(0x13, 3)

    def lambda_1A32():
        OP_8F(0xFE, 0x4CE, 0x0, 0x164E, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1A32)
    Sleep(20)
    SetChrChipByIndex(0x15, 3)

    def lambda_1A57():
        OP_8F(0xFE, 0xFFFFF880, 0x0, 0x1734, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1A57)
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

    def lambda_1B99():
        OP_6B(3600, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1B99)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x2)
    Sleep(300)

    ChrTalk(    #33
        0x10F,
        "#1445F#6P……总算击败它们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007F#12P唉……\x01",
            "果然还是要谨慎前进才行呢。\x02",
        )
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

    def lambda_1C75():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C75)
    Sleep(100)

    def lambda_1C88():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1C88)
    Sleep(100)
    OP_8C(0xF0, 0, 400)
    Sleep(300)

    ChrTalk(    #35
        0x101,
        (
            "#1002F#11P刚才那些怪物……\x01",
            "就是你之前所说的『恶魔』吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #36
        0x10F,
        (
            "#1802F#6P嗯嗯，\x01",
            "它们是叫做『梦魔』的恶魔亚种。\x02\x03",

            "和圣典记载的一样，\x01",
            "那些怪物最擅长精神攻击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1015F#11P很棘手的家伙啊……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #38
        0x101,
        (
            "#1006F#11P也就是说，\x01",
            "我们要做好应对措施才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        (
            "#1447F#6P没错……\x02\x01",

            "#1448F确认好装备之后，\x01",
            "我们再继续小心前进吧。\x02",
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

    # Function_7_B9A end

    def Function_8_1E44(): pass

    label("Function_8_1E44")

    PlayEffect(0x2, 0x4, 0xFF, -280, 100, 14530, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_1E7F():

        label("loc_1E7F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1E7F")

    QueueWorkItem2(0xFE, 1, lambda_1E7F)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_1E44 end

    def Function_9_1EAC(): pass

    label("Function_9_1EAC")

    OP_8E(0xFE, 0xFFFFFB5A, 0x0, 0x1D2E, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_1EAC end

    def Function_10_1EE0(): pass

    label("Function_10_1EE0")

    OP_8E(0xFE, 0x1B8, 0x0, 0x1D9C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_10_1EE0 end

    def Function_11_1F14(): pass

    label("Function_11_1F14")

    OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x170C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_11_1F14 end

    def Function_12_1F48(): pass

    label("Function_12_1F48")

    OP_8E(0xFE, 0x1CC, 0x0, 0x16EE, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_12_1F48 end

    def Function_13_1F7C(): pass

    label("Function_13_1F7C")

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
        "\x07\x00得到了\x1F\x5E\x03\x07\x00。\x02",
    )

    Jump("loc_20BB")

    label("loc_20BB")

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
        "#1444F#5P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1011F#5P哇……\x01",
            "真是块美丽的宝石呢。\x02\x03",

            "是七耀石之类的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2162():
        OP_6D(1200, -9450, 95200, 800)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2162)
    OP_8C(0x10F, 0, 400)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #43
        0x10F,
        (
            "#1446F#12P不是……\x01",
            "这就是『封印石』。\x02\x03",

            "#1448F先前，\x01",
            "你也是被封印在这里面的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x101,
        (
            "#1004F#5P有、有这种事吗？\x02\x03",

            "#1006F……这么说，\x01",
            "这里面也封印着什么人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10F,
        (
            "#1447F#12P嗯，不会错的。\x02\x03",

            "#1448F你认为会是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1015F#5P嗯，这个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2365")

    ChrTalk(    #47
        0x102,
        (
            "#1505F#5P如果是父亲的话，\x01",
            "那可就让人放心了……\x02\x03",

            "#1514F不过这种情况\x01",
            "实在是让人不敢奢求啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #48
        0x101,
        "#1016F#6P啊哈哈……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EB")

    label("loc_2365")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2432")

    ChrTalk(    #49
        0x106,
        (
            "#551F#5P喂喂，艾丝蒂尔……\x02\x03",

            "#555F这不会是\x01",
            "你家的大叔吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #50
        0x101,
        (
            "#1016F#6P唔，这个……\x01",
            "要真的是他，我们就得救了。\x02\x03",

            "#1025F可是……\x01",
            "应该不会这么巧合吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EB")

    label("loc_2432")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2503")

    ChrTalk(    #51
        0x103,
        (
            "#1526F#5P对了，艾丝蒂尔……\x02\x03",

            "#1527F这里面……\x01",
            "不会是老师吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #52
        0x101,
        (
            "#1016F#6P唔，这个……\x01",
            "要真的是他，我们就得救了。\x02\x03",

            "#1025F可是……\x01",
            "应该不会这么巧合吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EB")

    label("loc_2503")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A8")

    ChrTalk(    #53
        0x108,
        (
            "#573F#5P如果是卡西乌斯大人，\x01",
            "那我们就得救了……\x02\x03",

            "#070F不过实在是\x01",
            "不可能这么巧合啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #54
        0x101,
        "#1016F#6P啊哈哈……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EB")

    label("loc_25A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2663")

    ChrTalk(    #55
        0x10E,
        (
            "#179F#5P如果是卡西乌斯准将的话，\x01",
            "那我们就可以如虎添翼了……\x02\x03",

            "#170F不过说到底也不可能\x01",
            "让我们这么占便宜啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #56
        0x101,
        "#1016F#6P啊哈哈……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EB")

    label("loc_2663")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2741")

    ChrTalk(    #57
        0x104,
        (
            "#1545F#5P唔，艾丝蒂尔君。\x02\x03",

            "#1540F难道说……\x01",
            "这里面不会是\x01",
            "卡西乌斯先生吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1016F#6P唔，这个……\x01",
            "要真的是他，我们就得救了。\x02\x03",

            "#1025F可是……\x01",
            "应该不会这么巧合吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EB")

    label("loc_2741")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27EB")

    ChrTalk(    #59
        0x105,
        (
            "#1165F#5P如果卡西乌斯先生，\x01",
            "那我们就可以放心了……\x02\x03",

            "#1382F不过看起来，\x01",
            "应该不会这么巧合吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #60
        0x101,
        "#1016F#6P啊哈哈……确实。\x02",
    )

    CloseMessageWindow()

    label("loc_27EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28F0")

    ChrTalk(    #61
        0x107,
        (
            "#064F#5P难、难道说……\x01",
            "里面的人是爷爷……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #62
        0x101,
        (
            "#1006F#6P是啊，\x01",
            "他的确和我们一起去过浮游都市呢。\x02\x03",

            "#1015F啊……\x01",
            "不过拉赛尔博士不是去旅游了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x107,
        (
            "#560F#5P啊，嗯，没错呢。\x02\x03",

            "#561F所以应该就不是了……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_298D")
    OP_62(0x10A, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #64
        0x10A,
        (
            "#1310F#5P仔细想一想，\x01",
            "会不会是克鲁茨前辈！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1006F#6P啊……\x01",
            "那也是有可能的事情啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A58")

    ChrTalk(    #66
        0x10B,
        (
            "#216F#5P难、难道说……\x01",
            "里面的人是大哥他们！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #67
        0x101,
        (
            "#1004F#6P是吗……\x01",
            "这种可能性也是挺高的啊。\x02\x03",

            "#1006F之前在浮游都市的时候，\x01",
            "我们曾得到他们的鼎力相助啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B38")

    label("loc_2A58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B38")

    ChrTalk(    #68
        0x10D,
        (
            "#272F#5P唔……\x02\x03",

            "#277F说不定，\x01",
            "里面的人是那群空贼呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #69
        0x101,
        (
            "#1004F#6P啊，原来如此……\x01",
            "是乔丝特的哥哥们吧。\x02\x03",

            "#1006F的确，之前在浮游都市的时候，\x01",
            "我们曾得到他们的鼎力相助啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B38")


    ChrTalk(    #70
        0x10F,
        (
            "#1446F#12P……原来如此。\x02\x03",

            "#1448F不管怎么说……\x01",
            "我们还是暂且\x01",
            "回一下『据点』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(300)

    ChrTalk(    #71
        0x101,
        "#1006F#5P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2A03)
    OP_28(0x35, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_13_1F7C end

    def Function_14_2BD7(): pass

    label("Function_14_2BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA6")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    label("loc_2CA6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #72
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_2CD0")

    label("loc_2CD0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E3B")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_2D35")

    label("loc_2D35")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D52"),
        (1, "loc_2DCD"),
        (2, "loc_2DFC"),
        (SWITCH_DEFAULT, "loc_2E2B"),
    )


    label("loc_2D52")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jump("loc_2E38")

    label("loc_2DCD")

    OP_A9(0x22)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #73
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_2DF9")

    label("loc_2DF9")

    Jump("loc_2E38")

    label("loc_2DFC")

    OP_A9(0x8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #74
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_2E28")

    label("loc_2E28")

    Jump("loc_2E38")

    label("loc_2E2B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E38")

    label("loc_2E38")

    Jump("loc_2CE3")

    label("loc_2E3B")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E68")
    OP_A2(0x2592)
    EventEnd(0x1)
    Jump("loc_2E6B")

    label("loc_2E68")

    TalkEnd(0xFF)

    label("loc_2E6B")

    Return()

    # Function_14_2BD7 end

    def Function_15_2E6C(): pass

    label("Function_15_2E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E7D")
    Call(0, 7)
    Return()

    label("loc_2E7D")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_15_2E6C end

    def Function_16_2F5B(): pass

    label("Function_16_2F5B")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_16_2F5B end

    def Function_17_3039(): pass

    label("Function_17_3039")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_17_3039 end

    def Function_18_3117(): pass

    label("Function_18_3117")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_18_3117 end

    def Function_19_31F5(): pass

    label("Function_19_31F5")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_19_31F5 end

    def Function_20_32D3(): pass

    label("Function_20_32D3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_20_32D3 end

    def Function_21_338F(): pass

    label("Function_21_338F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_21_338F end

    def Function_22_344B(): pass

    label("Function_22_344B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_22_344B end

    def Function_23_3507(): pass

    label("Function_23_3507")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_23_3507 end

    def Function_24_35C3(): pass

    label("Function_24_35C3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_24_35C3 end

    def Function_25_367F(): pass

    label("Function_25_367F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36A8")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_369C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_369C)

    label("loc_36A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D1")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_36C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_36C5)

    label("loc_36D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36FA")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_36EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_36EE)

    label("loc_36FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3723")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3717():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3717)

    label("loc_3723")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_374F")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_374F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3766")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3766")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_377D")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_377D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3794")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3794")

    Return()

    # Function_25_367F end

    def Function_26_3795(): pass

    label("Function_26_3795")


    def lambda_379B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_379B)

    def lambda_37AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_37AD)

    def lambda_37BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_37BF)

    def lambda_37D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_37D1)
    Sleep(1000)
    Return()

    # Function_26_3795 end

    def Function_27_37E3(): pass

    label("Function_27_37E3")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #75
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_3840")

    label("loc_3840")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_27_37E3 end

    def Function_28_3857(): pass

    label("Function_28_3857")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392D")
    OP_28(0x15, 0x4, 0x2)
    OP_82(0x8B, 0x2)
    PlayEffect(0x8C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_392D")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_39A4")

    AnonymousTalk(    #76
        (
            "\x07\x05#40W      道路既已打开……\x01",
            "#500W\x01",
            "#40W      穿越此『门』吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A27")

    label("loc_39A4")


    AnonymousTalk(    #77
        (
            "\x07\x05#40W   吾之『门』为万人敞开……\x01",
            "    然则前方将有试炼降临。\x01",
            "#500W\x01",
            "#40W　   如若汝有此等勇气，\x01",
            "     便可穿越此『门』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A27")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Call(0, 27)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A50")
    Call(0, 29)

    label("loc_3A50")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_28_3857 end

    def Function_29_3A5C(): pass

    label("Function_29_3A5C")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0xA)
    Sleep(500)

    def lambda_3AC5():
        OP_6B(4360, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3AC5)
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

    # Function_29_3A5C end

    def Function_30_3B15(): pass

    label("Function_30_3B15")

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

    # Function_30_3B15 end

    SaveToFile()

Try(main)
