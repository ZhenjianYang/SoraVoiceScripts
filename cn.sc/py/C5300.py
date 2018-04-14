from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5300   ._SN',
        MapName             = 'Other',
        Location            = 'C5300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        '怀斯曼教授',                           # 9
        '小丑肯帕雷拉',                         # 10
        '凯文神父',                             # 11
        '升降梯',                               # 12
        '怀斯曼之杖',                           # 13
        '地震控制用假人',                       # 14
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
        'ED6_DT29/CH12010 ._CH',             # 00
        'ED6_DT29/CH12010 ._CH',             # 01
        'ED6_DT29/CH12080 ._CH',             # 02
        'ED6_DT29/CH12081 ._CH',             # 03
        'ED6_DT29/CH12050 ._CH',             # 04
        'ED6_DT29/CH12051 ._CH',             # 05
        'ED6_DT29/CH12140 ._CH',             # 06
        'ED6_DT29/CH12141 ._CH',             # 07
        'ED6_DT29/CH12420 ._CH',             # 08
        'ED6_DT29/CH12421 ._CH',             # 09
        'ED6_DT29/CH12280 ._CH',             # 0A
        'ED6_DT29/CH12281 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12010P._CP',             # 00
        'ED6_DT29/CH12010P._CP',             # 01
        'ED6_DT29/CH12080P._CP',             # 02
        'ED6_DT29/CH12081P._CP',             # 03
        'ED6_DT29/CH12050P._CP',             # 04
        'ED6_DT29/CH12051P._CP',             # 05
        'ED6_DT29/CH12140P._CP',             # 06
        'ED6_DT29/CH12141P._CP',             # 07
        'ED6_DT29/CH12420P._CP',             # 08
        'ED6_DT29/CH12421P._CP',             # 09
        'ED6_DT29/CH12280P._CP',             # 0A
        'ED6_DT29/CH12281P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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


    DeclMonster(
        X                   = -76830,
        Z                   = 0,
        Y                   = -90660,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94910,
        Z                   = 0,
        Y                   = -72500,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x529,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -100110,
        Z                   = 0,
        Y                   = 15090,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -87500,
        Z                   = 0,
        Y                   = 96820,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x528,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 81290,
        Z                   = 0,
        Y                   = 102460,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 99160,
        Z                   = 0,
        Y                   = 84400,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 102030,
        Y                   = -2000,
        Z                   = 1000,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = 20,
        TriggerZ            = 0,
        TriggerY            = -83640,
        TriggerRange        = 1000,
        ActorX              = 50,
        ActorZ              = 0,
        ActorY              = -82980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2550,
        TriggerZ            = 0,
        TriggerY            = -83650,
        TriggerRange        = 1000,
        ActorX              = -2520,
        ActorZ              = 0,
        ActorY              = -83030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2450,
        TriggerZ            = 0,
        TriggerY            = -83650,
        TriggerRange        = 1000,
        ActorX              = 2480,
        ActorZ              = 0,
        ActorY              = -82990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10350,
        TriggerZ            = 0,
        TriggerY            = -94070,
        TriggerRange        = 1000,
        ActorX              = 11050,
        ActorZ              = 0,
        ActorY              = -94030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10350,
        TriggerZ            = 0,
        TriggerY            = -96660,
        TriggerRange        = 1000,
        ActorX              = 10970,
        ActorZ              = 0,
        ActorY              = -96630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10350,
        TriggerZ            = 0,
        TriggerY            = -91550,
        TriggerRange        = 1000,
        ActorX              = 11060,
        ActorZ              = 0,
        ActorY              = -91560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_36A",          # 00, 0
        "Function_1_3C8",          # 01, 1
        "Function_2_4B7",          # 02, 2
        "Function_3_5CE",          # 03, 3
        "Function_4_6E5",          # 04, 4
        "Function_5_7FC",          # 05, 5
        "Function_6_913",          # 06, 6
        "Function_7_A2A",          # 07, 7
        "Function_8_B41",          # 08, 8
        "Function_9_10E4",         # 09, 9
        "Function_10_24C5",        # 0A, 10
        "Function_11_24FE",        # 0B, 11
        "Function_12_2546",        # 0C, 12
        "Function_13_2595",        # 0D, 13
        "Function_14_2784",        # 0E, 14
        "Function_15_29D5",        # 0F, 15
        "Function_16_2B54",        # 10, 16
        "Function_17_2E69",        # 11, 17
        "Function_18_2EF0",        # 12, 18
    )


    def Function_0_36A(): pass

    label("Function_0_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_384")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 9)
    Jump("loc_3C7")

    label("loc_384")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397")
    Event(0, 14)
    Jump("loc_3C7")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B4")
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_3C7")

    label("loc_3B4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (122, "loc_3C0"),
        (SWITCH_DEFAULT, "loc_3C7"),
    )


    label("loc_3C0")

    Event(0, 15)
    Jump("loc_3C7")

    label("loc_3C7")

    Return()

    # Function_0_36A end

    def Function_1_3C8(): pass

    label("Function_1_3C8")

    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406")
    OP_6F(0x1, 0)
    Jump("loc_40D")

    label("loc_406")

    OP_6F(0x1, 60)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F")
    OP_6F(0x2, 0)
    Jump("loc_426")

    label("loc_41F")

    OP_6F(0x2, 60)

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438")
    OP_6F(0x3, 0)
    Jump("loc_43F")

    label("loc_438")

    OP_6F(0x3, 60)

    label("loc_43F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_451")
    OP_6F(0x4, 0)
    Jump("loc_458")

    label("loc_451")

    OP_6F(0x4, 60)

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A")
    OP_6F(0x5, 0)
    Jump("loc_471")

    label("loc_46A")

    OP_6F(0x5, 60)

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483")
    OP_6F(0x6, 0)
    Jump("loc_48A")

    label("loc_483")

    OP_6F(0x6, 60)

    label("loc_48A")

    OP_10(0x13, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AB")
    OP_10(0x16, 0x1)
    OP_1B(0x16, 0x0, 0x10)
    Jump("loc_4B1")

    label("loc_4AB")

    OP_10(0x16, 0x0)
    OP_82(0x83, 0x0)

    label("loc_4B1")

    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_3C8 end

    def Function_2_4B7(): pass

    label("Function_2_4B7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x154, 1)"), scpexpr(EXPR_END)), "loc_526")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x54\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2364)
    Jump("loc_58C")

    label("loc_526")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x54\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x54\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_58C")

    Jump("loc_5C0")

    label("loc_58F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5C0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_4B7 end

    def Function_3_5CE(): pass

    label("Function_3_5CE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_63D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2366)
    Jump("loc_6A3")

    label("loc_63D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_6A3")

    Jump("loc_6D7")

    label("loc_6A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6D7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5CE end

    def Function_4_6E5(): pass

    label("Function_4_6E5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_754")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2367)
    Jump("loc_7BA")

    label("loc_754")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_7BA")

    Jump("loc_7EE")

    label("loc_7BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7EE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6E5 end

    def Function_5_7FC(): pass

    label("Function_5_7FC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_86B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x04\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2368)
    Jump("loc_8D1")

    label("loc_86B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x04\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x04\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_8D1")

    Jump("loc_905")

    label("loc_8D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_905")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7FC end

    def Function_6_913(): pass

    label("Function_6_913")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_982")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2369)
    Jump("loc_9E8")

    label("loc_982")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_9E8")

    Jump("loc_A1C")

    label("loc_9EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A1C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_913 end

    def Function_7_A2A(): pass

    label("Function_7_A2A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B02")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x140, 1)"), scpexpr(EXPR_END)), "loc_A99")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\x40\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x236A)
    Jump("loc_AFF")

    label("loc_A99")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\x40\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x40\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_AFF")

    Jump("loc_B33")

    label("loc_B02")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B33")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A2A end

    def Function_8_B41(): pass

    label("Function_8_B41")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B58")
    Call(0, 17)
    Call(0, 18)

    label("loc_B58")

    OP_6D(-1440, 0, -89110, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(171000, 0)
    OP_6E(500, 0)
    SetChrPos(0x101, 450, 0, -129370, 0)
    SetChrPos(0x102, -740, 0, -129490, 0)
    SetChrPos(0xF8, 450, 0, -130590, 0)
    SetChrPos(0xF9, -760, 0, -130850, 0)
    FadeToBright(1000, 0)

    def lambda_BE8():
        OP_6D(80, 0, -129160, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE8)

    def lambda_C00():
        OP_67(0, 6290, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C00)

    def lambda_C18():
        OP_6C(159000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C18)

    def lambda_C28():
        OP_6B(1980, 7000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C28)
    OP_C8(0x80, 0x46, "C_PLAC27._CH", 0x1, 0x3E8)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8E")

    ChrTalk(    #18
        0x10B,
        "#212F#5P这、这就是『中枢塔』的内部……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF5")

    label("loc_C8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC9")

    ChrTalk(    #19
        0x108,
        "#072F#5P这就是『中枢塔』的内部吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF5")

    label("loc_CC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D04")

    ChrTalk(    #20
        0x106,
        "#057F#5P这就是『中枢塔』的内部啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF5")

    label("loc_D04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D42")

    ChrTalk(    #21
        0x104,
        (
            "#032F#5P喔……\x01",
            "这就是『中枢塔』内部吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF5")

    label("loc_D42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D85")

    ChrTalk(    #22
        0x109,
        (
            "#1063F#5P啊～……\x01",
            "这就是『中枢塔』的内部吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF5")

    label("loc_D85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBE")

    ChrTalk(    #23
        0x103,
        "#022F#5P这就是『中枢塔』的内部……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF5")

    label("loc_DBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF5")

    ChrTalk(    #24
        0x105,
        "#1163F#5P这就是『中枢塔』的内部……\x02",
    )

    CloseMessageWindow()

    label("loc_DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E37")

    ChrTalk(    #25
        0x107,
        (
            "#065F#5P简、简直是在巨大装置\x01",
            "的内部一样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_E37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E78")

    ChrTalk(    #26
        0x105,
        (
            "#1163F#5P简直是在巨大装置\x01",
            "的内部一样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_E78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB8")

    ChrTalk(    #27
        0x103,
        (
            "#022F#5P简直是在巨大装置\x01",
            "的内部一样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_EB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF9")

    ChrTalk(    #28
        0x109,
        (
            "#1063F#5P简直是在巨大装置\x01",
            "的内部一样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_EF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F39")

    ChrTalk(    #29
        0x104,
        (
            "#034F#5P简直是在巨大装置\x01",
            "的内部一样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_F39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F79")

    ChrTalk(    #30
        0x106,
        (
            "#555F#5P简直是在巨大装置\x01",
            "的内部一样啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB6")

    label("loc_F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(    #31
        0x108,
        (
            "#072F#5P简直是在巨大装置\x01",
            "的内部一样啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB6")


    ChrTalk(    #32
        0x101,
        (
            "#1002F#5P还有，那发光的液体\x01",
            "到底是什么呢……\x02\x03",

            "感觉正体不明的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#1035F#5P……或许是充满\x01",
            "高压导力的液体……\x02\x03",

            "#1042F看来最好不要\x01",
            "用手直接触碰。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(10, 0, -131270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 10, 0, -131270, 0)
    SetChrPos(0x1, 10, 0, -131270, 0)
    SetChrPos(0x2, 10, 0, -131270, 0)
    SetChrPos(0x3, 10, 0, -131270, 0)
    OP_A2(0x223C)
    EventEnd(0x0)
    Return()

    # Function_8_B41 end

    def Function_9_10E4(): pass

    label("Function_9_10E4")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_D2(0x2601EF, 0x2601F4, 0xC)
    OP_D2(0x27028E, 0x270298, 0xD)
    OP_D2(0x270296, 0x2702A0, 0xE)
    OP_D2(0x2601F0, 0x2601F5, 0xF)
    OP_D2(0x2601F6, 0x2601FB, 0x10)
    OP_D2(0x270080, 0x270084, 0x11)
    OP_D2(0x270176, 0x270183, 0x12)
    OP_D2(0x270178, 0x270185, 0x13)
    OP_D2(0x2701DA, 0x2701DF, 0x14)
    OP_D2(0x2600C1, 0x2600C6, 0x15)
    OP_D2(0x260157, 0x26015C, 0x16)
    OP_D2(0x2701D0, 0x2701D5, 0x17)
    OP_6D(-101510, 30, -14160, 0)
    OP_67(0, 9190, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(315000, 0)
    OP_6E(336, 0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 12)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0x9, 20)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -99780, 110, -11120, 0)
    OP_43(0xD, 0x3, 0x0, 0xC)
    OP_22(0x85, 0x1, 0x46)
    FadeToBright(1500, 0)

    def lambda_11F4():
        OP_6D(-100630, 0, -4610, 6800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11F4)

    def lambda_120C():
        OP_6B(2080, 6800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_120C)

    def lambda_121C():

        label("loc_121C")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x1F4)
        OP_48()
        Jump("loc_121C")

    QueueWorkItem2(0x8, 3, lambda_121C)
    OP_8E(0x8, 0xFFFE799C, 0x0, 0xFFFFEBD8, 0x3E8, 0x0)
    OP_44(0x8, 0x3)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #34
        0x8,
        (
            "#1157F#6P……不可能……这不可能……\x02\x03",

            "如此事态……\x01",
            "『盟主』的预言里并没有……\x02\x03",

            "#1156F……等……等一下……\x02\x03",

            "难、难道说…\x01",
            "我也只是一枚试验用的棋子吗……\x02\x03",

            "#1157F哼……\x01",
            "回去之后一定要问明白才行……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, -99790, 0, 7790, 180)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #35
        0xA,
        "青年的声音",
        "#3P很抱歉，你已经没机会那么做了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1380():
        OP_6D(-100880, 0, -790, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1380)

    def lambda_1398():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1398)

    def lambda_13B0():
        OP_6B(1660, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13B0)

    def lambda_13C0():
        OP_6E(534, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13C0)
    OP_8E(0xA, 0xFFFE79EC, 0x0, 0x96A, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #36
        0x8,
        (
            "#1157F#6P凯文·格拉汉姆……\x01",
            "你是什么时候来到这种地方的……\x02\x03",

            "滚开……我可没时间\x01",
            "理会你这种杂鱼……\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    Sleep(200)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 14)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x8, 14)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    OP_22(0xD8, 0x0, 0x64)
    OP_99(0x8, 0x4, 0x9, 0x5DC)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0xA, 22)
    SetChrSubChip(0xA, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xA, 1)
    Sleep(1000)
    LoadEffect(0x1, "monster\\msc0647a.eff")
    LoadEffect(0x2, "monster\\msc0647b.eff")
    LoadEffect(0x3, "scraft\\sc008_02.eff")
    LoadEffect(0x3, "scraft\\sc008_02.eff")
    LoadEffect(0x4, "monster\\ms31004a.eff")
    PlayEffect(0x1, 0x1, 0xA, 0, 2800, 3000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0x0, 0x2)
    PlayEffect(0x3, 0x2, 0xA, 300, 1000, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    PlayEffect(0x2, 0x3, 0xA, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x390, 0x0, 0x64)
    PlayEffect(0x4, 0x4, 0xA, 0, 0, 0, 0, 0, 0, 2000, 4000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_82(0x3, 0x2)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 13)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x8,
        (
            "#1156F……你……\x01",
            "『魔眼』竟然对你无效！？\x02\x03",

            "就算是星杯骑士，\x01",
            "也不是你这种新手可以抵挡的啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x4, 0x2)
    Sleep(1000)
    Sleep(100)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xA, 17)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #38
        0xA,
        (
            "#1066F#2P啊～抱歉。\x01",
            "之前说了个小小的谎。\x02\x03",

            "#1060F我在骑士团排名第五位。\x01",
            "所以像这类的场面早已见怪不怪了。\x02\x03",

            "#1075F不过，就算如此，\x01",
            "也很难赢得了正常状态下的你……\x02\x03",

            "#1073F不过，出现『可乘之机』的话就另当别论了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        "#1153F什么……\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x3, "map\\mp104_00.eff")
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 18)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0xA, 19)
    OP_99(0xA, 0x0, 0x7, 0xBB8)

    def lambda_185B():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_185B)
    Sleep(300)
    PlayEffect(0x3, 0x3, 0xA, 0, 1050, 1550, 0, 0, 0, 500, 500, 500, 0x8, 0, 500, 0, 0)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(200)
    OP_22(0x151, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 15)
    OP_99(0x8, 0x0, 0x4, 0x5DC)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)
    OP_83(0x3, 0x2)
    OP_82(0x3, 0x0)
    Sleep(500)

    ChrTalk(    #40
        0x8,
        "#1157F唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "#1075F#2P……我真正的任务\x01",
            "并不是调查什么『辉之环』。\x02\x03",

            "#1072F最恶的破戒僧，\x01",
            "盖鲁格·怀斯曼——\x02\x03",

            "我是前来了结你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#1151F呼呼……原来如此……\x02\x03",

            "不过，如果你以为这种程度的攻击，\x01",
            "就能消灭我『白面』的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_9E(0x8, 0x28, 0x0, 0x12C, 0x1388)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 15)
    Sleep(500)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_1A23():
        OP_99(0xFE, 0x5, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1A23)
    Sleep(150)
    OP_43(0xC, 0x0, 0x0, 0xA)
    WaitChrThread(0x8, 0x0)
    Sleep(1000)
    OP_99(0x8, 0x8, 0xA, 0x320)
    Sleep(500)

    ChrTalk(    #43
        0x8,
        "#1153F#5P什……什么……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x152, 0x1, 0x5A)
    OP_99(0x8, 0xB, 0xF, 0x1F4)
    OP_62(0x8, 0xC8, 1800, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x8,
        (
            "#1156F#5P『盐、盐之桩』……\x02\x03",

            "曾经将诺桑普里亚北部地区\x01",
            "化为盐之海的禁断咒具……\x02\x03",

            "#1157F为了杀死我一个人，\x01",
            "竟然会动用到这种东西……！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #45
        0xA,
        (
            "#1072F你的做法太过分了，\x02\x03",

            "即使是中立的教会\x01",
            "也已无法再继续坐视下去了。\x02\x03",

            "老老实实地消失吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BAC():
        OP_99(0xFE, 0x10, 0x18, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1BAC)
    Sleep(1000)

    ChrTalk(    #46 op#A op#5
        0x8,
        "#1158F#5P#3S#60A你……你这条可恨的走狗！！！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    WaitChrThread(0x8, 0x2)
    OP_23(0x152)
    Sleep(1900)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1900)
    OP_63(0xA)
    Sleep(900)

    ChrTalk(    #47
        0xA,
        (
            "#1072F#2P走狗吗……\x01",
            "嗯，这话倒也说得没错。\x02\x03",

            "#1076F…………………………………\x02\x03",

            "#1065F#2P约修亚，真羡慕你的运气。\x02\x03",

            "和我这种人不同，\x01",
            "至少…你还有回头的机会。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    LoadEffect(0x1, "map\\\\mp055_00.eff")
    LoadEffect(0x2, "map\\mp105_00.eff")
    SetChrPos(0x9, -102410, 0, -5240, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetMessageWindowPos(70, 100, -1, -1)
    SetChrName("少年的声音")

    AnonymousTalk(    #48
        (
            "\x07\x05#5P呼呼呼……\x01",
            "这算是嫉妒吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1D72():
        OP_6D(-102500, 0, -550, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D72)

    def lambda_1D8A():
        OP_67(0, 5200, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D8A)

    def lambda_1DA2():
        OP_6B(1740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DA2)

    def lambda_1DB2():
        OP_6E(542, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1DB2)
    PlayEffect(0x1, 0x0, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(500)

    def lambda_1E01():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E01)
    WaitChrThread(0x9, 0x1)
    OP_82(0x0, 0x2)
    OP_43(0x9, 0x3, 0x0, 0xB)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #49
        0x9,
        (
            "#853F#5P星杯骑士第五位──\x01",
            "『异端制裁者』凯文·格拉汉姆。\x02\x03",

            "#854F呵呵呵……\x01",
            "果然如传闻中一般冷酷无情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "#1074F#2P你是……\x01",
            "小丑吧。\x02\x03",

            "#1072F不好意思……\x01",
            "你来晚一步，他已经没救了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "#854F#5P呵呵……\x01",
            "或许你已经听说了，\x01",
            "我的任务仅仅是『观察』而已。\x02\x03",

            "掌握计划的全过程，\x01",
            "滴水不漏地向『盟主』报告。\x02\x03",

            "#853F教授的自毁灭亡也只是单纯的结果，\x01",
            "并非能够防范的事态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        (
            "#1075F#2P原来如此……\x02\x03",

            "#1073F『噬身之蛇』……\x01",
            "看来这组织里还充满许多的谜团啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#854F#5P呵呵……\x01",
            "你们骑士团不也是一样吗。\x02\x03",

            "#853F好了……\x01",
            "这下我的任务也结束了。\x02\x03",

            "失物也已经回收完毕，\x01",
            "差不多是该回去的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        "#1074F#2P什么……！？\x02",
    )

    CloseMessageWindow()

    def lambda_208C():
        OP_6D(-101170, 0, -3010, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_208C)

    def lambda_20A4():
        OP_67(0, 4800, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20A4)
    OP_8C(0x9, 90, 400)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 21)
    SetChrSubChip(0x9, 0)
    OP_0D()
    WaitChrThread(0x9, 0x1)
    Sleep(500)
    Fade(500)

    def lambda_20E2():
        OP_6B(1540, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20E2)
    OP_99(0x9, 0x1, 0x2, 0x3E8)
    OP_22(0xBC, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_22(0x153, 0x0, 0x64)
    SetChrSubChip(0x8, 25)
    Sleep(500)
    PlayEffect(0x2, 0x2, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)

    def lambda_2155():

        label("loc_2155")

        OP_99(0xFE, 0x8, 0xF, 0x5DC)
        OP_48()
        Jump("loc_2155")

    QueueWorkItem2(0xC, 1, lambda_2155)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2189():
        OP_6B(1640, 5000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2189)
    PlayEffect(0x1, 0x0, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(200)
    PlayEffect(0x1, 0x1, 0xC, 0, 0, 0, 0, 0, 0, 1300, 1000, 1300, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 20)
    SetChrSubChip(0x9, 0)
    Sleep(500)
    OP_8C(0x9, 0, 300)
    Sleep(500)

    ChrTalk(    #55
        0x9,
        (
            "#851F啊哈哈！\x01",
            "那么祝一切顺利！\x02\x03",

            "希望以后\x01",
            "有机会再见！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2268():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2268)
    Sleep(200)

    def lambda_227F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_227F)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xC, 0x1)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_43(0x9, 0x3, 0x0, 0xB)
    SetChrFlags(0x9, 0x80)
    Sleep(1500)

    def lambda_22B2():
        OP_67(0, 5300, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22B2)
    OP_8E(0xA, 0xFFFE79F6, 0x0, 0xFFFFF22C, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #56
        0xA,
        (
            "#1074F#5P失物……难道是……\x02\x03",

            "#1072F…………………………………\x02\x03",

            "#1065F算了……\x01",
            "这已经超出我的任务权限了。\x02\x03",

            "#1067F得赶快和艾丝蒂尔\x01",
            "他们会合才行啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    FadeToDark(1500, 0, -1)
    OP_24(0x85, 0x3C)
    Sleep(200)
    OP_24(0x85, 0x32)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    OP_0D()
    OP_21()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #57
        (
            "\x07\x05……就这样，艾丝蒂尔等人\x01",
            "在断断续续发生的摇晃中逃出了『中枢塔』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "\x07\x05或许是因为导力急剧下降的缘故，\x01",
            "『光环轨道』变得完全无法使用……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #59
        (
            "\x07\x05艾丝蒂尔等人便通过地下道\x01",
            "前往停泊在公园区域的埃尔赛尤号。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5208   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_9_10E4 end

    def Function_10_24C5(): pass

    label("Function_10_24C5")

    SetChrPos(0xFE, -99300, 0, -4800, 0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x800)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xC, 16)
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x5, 0x3E8)
    Return()

    # Function_10_24C5 end

    def Function_11_24FE(): pass

    label("Function_11_24FE")

    Sleep(250)
    OP_24(0x10A, 0x5A)
    Sleep(250)
    OP_24(0x10A, 0x50)
    Sleep(250)
    OP_24(0x10A, 0x46)
    Sleep(250)
    OP_24(0x10A, 0x3C)
    Sleep(250)
    OP_24(0x10A, 0x32)
    Sleep(250)
    OP_24(0x10A, 0x28)
    Sleep(250)
    OP_24(0x10A, 0x1E)
    Sleep(250)
    OP_23(0x10A)
    Return()

    # Function_11_24FE end

    def Function_12_2546(): pass

    label("Function_12_2546")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2594")
    OP_7C(0x28, 0x28, 0x3E8, 0x320)
    Sleep(1800)
    OP_7C(0x14, 0x14, 0x3E8, 0x514)
    Sleep(1600)
    OP_7C(0x1E, 0x1E, 0x3E8, 0x5DC)
    Sleep(2000)
    Jump("Function_12_2546")

    label("loc_2594")

    Return()

    # Function_12_2546 end

    def Function_13_2595(): pass

    label("Function_13_2595")

    EventBegin(0x0)
    OP_A1(0xB, 0x0)
    SetChrPos(0xB, 101980, -1750, 850, 0)
    OP_48()
    Fade(1000)
    OP_6D(101980, 0, 850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 102000, 0, 2000, 0)
    OP_89(0x1, 103000, 0, 1000, 90)
    OP_89(0x2, 101000, 0, 1000, 270)
    OP_89(0x3, 102000, 0, 0, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_2645():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2645)
    Sleep(500)

    def lambda_2665():
        OP_6D(101980, 35000, 850, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2665)

    def lambda_267D():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_267D)

    def lambda_2695():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2695)
    Sleep(500)

    def lambda_26AA():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26AA)
    Sleep(500)

    def lambda_26CA():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26CA)
    Sleep(400)

    def lambda_26EA():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26EA)
    Sleep(200)

    def lambda_270A():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_270A)
    Sleep(100)

    def lambda_272A():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_272A)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2595 end

    def Function_14_2784(): pass

    label("Function_14_2784")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0xB, 0x0)
    SetChrPos(0xB, 101980, 66000, 850, 0)
    OP_48()
    OP_6D(101980, 48000, 850, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 102000, 67000, 2000, 0)
    OP_89(0x1, 103000, 67000, 1000, 90)
    OP_89(0x2, 101000, 67000, 1000, 270)
    OP_89(0x3, 102000, 67000, 0, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_2833():
        OP_6D(101980, 0, 850, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2833)

    def lambda_284B():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_284B)

    def lambda_2863():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2863)
    FadeToBright(1000, 0)
    SetPlaceName(0x11C)

    def lambda_287F():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_287F)
    Sleep(3800)
    Sleep(4000)

    def lambda_28A4():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_28A4)
    Sleep(700)

    def lambda_28C4():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_28C4)
    Sleep(600)

    def lambda_28E4():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_28E4)
    Sleep(100)

    def lambda_2904():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2904)
    Sleep(500)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xB, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 102080, 0, 5330, 0)
    SetChrPos(0x1, 102080, 0, 5330, 0)
    SetChrPos(0x2, 102080, 0, 5330, 0)
    SetChrPos(0x3, 102080, 0, 5330, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_14_2784 end

    def Function_15_29D5(): pass

    label("Function_15_29D5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 1100, -94000, 0)
    SetChrPos(0x101, 500, 1100, -94500, 180)
    SetChrPos(0x102, -500, 1100, -94500, 180)
    SetChrPos(0xF8, 500, 1100, -93500, 180)
    SetChrPos(0xF9, -500, 1100, -93500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_2AB0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2AB0)

    def lambda_2AC2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2AC2)

    def lambda_2AD4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2AD4)

    def lambda_2AE6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2AE6)
    Sleep(2500)
    Fade(500)
    OP_6D(0, 0, -97620, 0)
    SetChrPos(0x0, 0, 0, -97620, 180)
    SetChrPos(0x1, 0, 0, -97620, 180)
    SetChrPos(0x2, 0, 0, -97620, 180)
    SetChrPos(0x3, 0, 0, -97620, 180)
    EventEnd(0x0)
    Return()

    # Function_15_29D5 end

    def Function_16_2B54(): pass

    label("Function_16_2B54")

    EventBegin(0x1)
    Fade(500)
    OP_6D(0, 1100, -94000, 0)
    SetChrPos(0x101, -500, 1100, -93500, 0)
    SetChrPos(0x102, 500, 1100, -93500, 0)
    SetChrPos(0xF8, -500, 1100, -94500, 0)
    SetChrPos(0xF9, 500, 1100, -94500, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_END)), "loc_2BF6")
    OP_CC(0x1, 0x0, "【第５层】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_END)), "loc_2C15")
    OP_CC(0x1, 0x0, "【第４层】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 6)), scpexpr(EXPR_END)), "loc_2C34")
    OP_CC(0x1, 0x0, "【第３层】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 3)), scpexpr(EXPR_END)), "loc_2C53")
    OP_CC(0x1, 0x0, "【第２层】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2C53")

    OP_CC(0x1, 0x0, "【放弃】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C9E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D20")

    label("loc_2C9E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D20")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC2")
    Jump("loc_2D20")

    label("loc_2CC2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D13")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2CFC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CF9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CF9")

    Jump("loc_2D13")

    label("loc_2CFC")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2CC2")

    label("loc_2D13")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2CA8")

    label("loc_2D20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC3")
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_2D7C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2D7C)

    def lambda_2D8E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2D8E)

    def lambda_2DA0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2DA0)

    def lambda_2DB2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2DB2)
    Sleep(2000)

    label("loc_2DC3")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2DDC"),
        (1, "loc_2DE8"),
        (2, "loc_2DF4"),
        (3, "loc_2E00"),
        (SWITCH_DEFAULT, "loc_2E0C"),
    )


    label("loc_2DDC")

    NewScene("ED6_DT21/C5306   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_2E0C")

    label("loc_2DE8")

    NewScene("ED6_DT21/C5305   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_2E0C")

    label("loc_2DF4")

    NewScene("ED6_DT21/C5303   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_2E0C")

    label("loc_2E00")

    NewScene("ED6_DT21/C5301   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_2E0C")

    label("loc_2E0C")

    Fade(500)
    OP_6D(0, 0, -97620, 0)
    SetChrPos(0x0, 0, 0, -97620, 180)
    SetChrPos(0x1, 0, 0, -97620, 180)
    SetChrPos(0x2, 0, 0, -97620, 180)
    SetChrPos(0x3, 0, 0, -97620, 180)
    EventEnd(0x0)
    Return()

    # Function_16_2B54 end

    def Function_17_2E69(): pass

    label("Function_17_2E69")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EE3"),
        (1, "loc_2EE9"),
        (SWITCH_DEFAULT, "loc_2EEF"),
    )


    label("loc_2EE3")

    OP_A2(0x1200)
    Jump("loc_2EEF")

    label("loc_2EE9")

    OP_A2(0x1201)
    Jump("loc_2EEF")

    label("loc_2EEF")

    Return()

    # Function_17_2E69 end

    def Function_18_2EF0(): pass

    label("Function_18_2EF0")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_18_2EF0 end

    SaveToFile()

Try(main)
