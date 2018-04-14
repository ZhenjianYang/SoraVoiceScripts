from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5302   ._SN',
        MapName             = 'Other',
        Location            = 'C5302.x',
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
        '升降梯',                               # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12340 ._CH',             # 0A
        'ED6_DT29/CH12341 ._CH',             # 0B
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
        'ED6_DT29/CH12340P._CP',             # 0A
        'ED6_DT29/CH12341P._CP',             # 0B
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


    DeclMonster(
        X                   = -91600,
        Z                   = 2160,
        Y                   = 96970,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x530,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -98800,
        Z                   = 140,
        Y                   = 15500,
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
        X                   = -99020,
        Z                   = 90,
        Y                   = 2280,
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
        X                   = -71000,
        Z                   = 4240,
        Y                   = -78680,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 120,
        Z                   = 2000,
        Y                   = -94140,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x530,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 84070,
        Z                   = 2170,
        Y                   = -85430,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 100070,
        Y                   = -2000,
        Z                   = 9050,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 10,
    )


    DeclActor(
        TriggerX            = -107040,
        TriggerZ            = 0,
        TriggerY            = 5010,
        TriggerRange        = 1000,
        ActorX              = -107640,
        ActorZ              = 0,
        ActorY              = 4980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107050,
        TriggerZ            = 0,
        TriggerY            = 7600,
        TriggerRange        = 1000,
        ActorX              = -107650,
        ActorZ              = 0,
        ActorY              = 7570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107050,
        TriggerZ            = 0,
        TriggerY            = 10290,
        TriggerRange        = 1000,
        ActorX              = -107690,
        ActorZ              = 0,
        ActorY              = 10200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107050,
        TriggerZ            = 0,
        TriggerY            = 12900,
        TriggerRange        = 1000,
        ActorX              = -107650,
        ActorZ              = 0,
        ActorY              = 12870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 13070,
        TriggerRange        = 1000,
        ActorX              = -90030,
        ActorZ              = 0,
        ActorY              = 13100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 10470,
        TriggerRange        = 1000,
        ActorX              = -90090,
        ActorZ              = 0,
        ActorY              = 10500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 7650,
        TriggerRange        = 1000,
        ActorX              = -90010,
        ActorZ              = 0,
        ActorY              = 7690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 5050,
        TriggerRange        = 1000,
        ActorX              = -90020,
        ActorZ              = 0,
        ActorY              = 4960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_312",          # 00, 0
        "Function_1_323",          # 01, 1
        "Function_2_420",          # 02, 2
        "Function_3_537",          # 03, 3
        "Function_4_68A",          # 04, 4
        "Function_5_7A1",          # 05, 5
        "Function_6_8B8",          # 06, 6
        "Function_7_9CF",          # 07, 7
        "Function_8_AE6",          # 08, 8
        "Function_9_BFD",          # 09, 9
        "Function_10_D14",         # 0A, 10
        "Function_11_F03",         # 0B, 11
    )


    def Function_0_312(): pass

    label("Function_0_312")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322")
    Event(0, 11)

    label("loc_322")

    Return()

    # Function_0_312 end

    def Function_1_323(): pass

    label("Function_1_323")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361")
    OP_6F(0x1, 0)
    Jump("loc_368")

    label("loc_361")

    OP_6F(0x1, 60)

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A")
    OP_6F(0x2, 0)
    Jump("loc_381")

    label("loc_37A")

    OP_6F(0x2, 60)

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393")
    OP_6F(0x3, 0)
    Jump("loc_39A")

    label("loc_393")

    OP_6F(0x3, 60)

    label("loc_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC")
    OP_6F(0x4, 0)
    Jump("loc_3B3")

    label("loc_3AC")

    OP_6F(0x4, 60)

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5")
    OP_6F(0x5, 0)
    Jump("loc_3CC")

    label("loc_3C5")

    OP_6F(0x5, 60)

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE")
    OP_6F(0x6, 0)
    Jump("loc_3E5")

    label("loc_3DE")

    OP_6F(0x6, 60)

    label("loc_3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7")
    OP_6F(0x7, 0)
    Jump("loc_3FE")

    label("loc_3F7")

    OP_6F(0x7, 60)

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410")
    OP_6F(0x8, 0)
    Jump("loc_417")

    label("loc_410")

    OP_6F(0x8, 60)

    label("loc_417")

    OP_10(0x0, 0x0)
    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_323 end

    def Function_2_420(): pass

    label("Function_2_420")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_48F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x236C)
    Jump("loc_4F5")

    label("loc_48F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x06\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4F5")

    Jump("loc_529")

    label("loc_4F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_529")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_420 end

    def Function_3_537(): pass

    label("Function_3_537")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x236D)
    Jump("loc_678")

    label("loc_65E")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_678")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_537 end

    def Function_4_68A(): pass

    label("Function_4_68A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_762")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x172, 1)"), scpexpr(EXPR_END)), "loc_6F9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x72\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x236F)
    Jump("loc_75F")

    label("loc_6F9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x72\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x72\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_75F")

    Jump("loc_793")

    label("loc_762")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_793")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_68A end

    def Function_5_7A1(): pass

    label("Function_5_7A1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_879")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_810")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2370)
    Jump("loc_876")

    label("loc_810")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_876")

    Jump("loc_8AA")

    label("loc_879")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7A1 end

    def Function_6_8B8(): pass

    label("Function_6_8B8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_990")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_927")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2371)
    Jump("loc_98D")

    label("loc_927")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x01\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_98D")

    Jump("loc_9C1")

    label("loc_990")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8B8 end

    def Function_7_9CF(): pass

    label("Function_7_9CF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15B, 1)"), scpexpr(EXPR_END)), "loc_A3E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\x5B\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2372)
    Jump("loc_AA4")

    label("loc_A3E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\x5B\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x5B\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_AA4")

    Jump("loc_AD8")

    label("loc_AA7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AD8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_9CF end

    def Function_8_AE6(): pass

    label("Function_8_AE6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_B55")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2374)
    Jump("loc_BBB")

    label("loc_B55")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_BBB")

    Jump("loc_BEF")

    label("loc_BBE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BEF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_AE6 end

    def Function_9_BFD(): pass

    label("Function_9_BFD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_C6C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2375)
    Jump("loc_CD2")

    label("loc_C6C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_CD2")

    Jump("loc_D06")

    label("loc_CD5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D06")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_BFD end

    def Function_10_D14(): pass

    label("Function_10_D14")

    EventBegin(0x0)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100070, -1750, 9050, 0)
    OP_48()
    Fade(1000)
    OP_6D(100070, 0, 9050, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 14000, 10000, 0)
    OP_89(0x1, 101000, 14000, 9000, 90)
    OP_89(0x2, 99000, 14000, 9000, 270)
    OP_89(0x3, 100000, 14000, 8000, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_DC4():
        OP_8F(0xFE, 0x18E5C, 0xEA60, 0x352, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DC4)
    Sleep(500)

    def lambda_DE4():
        OP_6D(100070, 35000, 9050, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE4)

    def lambda_DFC():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DFC)

    def lambda_E14():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E14)
    Sleep(500)

    def lambda_E29():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E29)
    Sleep(500)

    def lambda_E49():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E49)
    Sleep(400)

    def lambda_E69():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E69)
    Sleep(200)

    def lambda_E89():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E89)
    Sleep(100)

    def lambda_EA9():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EA9)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A2(0x228E)
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

    # Function_10_D14 end

    def Function_11_F03(): pass

    label("Function_11_F03")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100070, 66000, 9050, 0)
    OP_48()
    OP_6D(100070, 48000, 9050, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 67000, 10000, 0)
    OP_89(0x1, 101000, 67000, 9000, 90)
    OP_89(0x2, 99000, 67000, 9000, 270)
    OP_89(0x3, 100000, 67000, 8000, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_FB2():
        OP_6D(100070, 0, 9050, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB2)

    def lambda_FCA():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FCA)

    def lambda_FE2():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FE2)
    FadeToBright(1000, 0)
    SetPlaceName(0x11D)

    def lambda_FFE():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FFE)
    Sleep(7800)

    def lambda_101E():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_101E)
    Sleep(700)

    def lambda_103E():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_103E)
    Sleep(600)

    def lambda_105E():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_105E)
    Sleep(100)

    def lambda_107E():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_107E)
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
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 100420, 0, 4460, 180)
    SetChrPos(0x1, 100420, 0, 4460, 180)
    SetChrPos(0x2, 100420, 0, 4460, 180)
    SetChrPos(0x3, 100420, 0, 4460, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_11_F03 end

    SaveToFile()

Try(main)
