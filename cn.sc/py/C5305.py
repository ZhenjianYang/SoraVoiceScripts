from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5305   ._SN',
        MapName             = 'Other',
        Location            = 'C5305.x',
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
        'ED6_DT29/CH12290 ._CH',             # 0A
        'ED6_DT29/CH12291 ._CH',             # 0B
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
        'ED6_DT29/CH12290P._CP',             # 0A
        'ED6_DT29/CH12291P._CP',             # 0B
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
        X                   = 60,
        Z                   = 3500,
        Y                   = -94030,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -91910,
        Z                   = 2230,
        Y                   = 96640,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -98860,
        Z                   = 50,
        Y                   = 8530,
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
        X                   = -79920,
        Z                   = 2350,
        Y                   = -72810,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 83880,
        Z                   = 2180,
        Y                   = -85080,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 100050,
        Y                   = -2000,
        Z                   = 9110,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -107300,
        TriggerZ            = 0,
        TriggerY            = 4900,
        TriggerRange        = 1000,
        ActorX              = -107910,
        ActorZ              = 0,
        ActorY              = 4870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107300,
        TriggerZ            = 0,
        TriggerY            = 9030,
        TriggerRange        = 1000,
        ActorX              = -107910,
        ActorZ              = 0,
        ActorY              = 9000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107290,
        TriggerZ            = 0,
        TriggerY            = 13070,
        TriggerRange        = 1000,
        ActorX              = -107980,
        ActorZ              = 0,
        ActorY              = 12940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 13010,
        TriggerRange        = 1000,
        ActorX              = -90050,
        ActorZ              = 0,
        ActorY              = 13040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90710,
        TriggerZ            = 0,
        TriggerY            = 8940,
        TriggerRange        = 1000,
        ActorX              = -90060,
        ActorZ              = 0,
        ActorY              = 8980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90710,
        TriggerZ            = 0,
        TriggerY            = 5000,
        TriggerRange        = 1000,
        ActorX              = -90020,
        ActorZ              = 0,
        ActorY              = 5030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -540,
        TriggerZ            = 2000,
        TriggerY            = -94060,
        TriggerRange        = 1000,
        ActorX              = 60,
        ActorZ              = 2000,
        ActorY              = -94030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_352",          # 01, 1
        "Function_2_4A3",          # 02, 2
        "Function_3_4B9",          # 03, 3
        "Function_4_5D0",          # 04, 4
        "Function_5_6E7",          # 05, 5
        "Function_6_7FE",          # 06, 6
        "Function_7_915",          # 07, 7
        "Function_8_A2C",          # 08, 8
        "Function_9_B43",          # 09, 9
        "Function_10_D13",         # 0A, 10
        "Function_11_E3C",         # 0B, 11
        "Function_12_102B",        # 0C, 12
        "Function_13_1277",        # 0D, 13
        "Function_14_1373",        # 0E, 14
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E7")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_30A")

    label("loc_2E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA")
    Event(0, 12)
    Jump("loc_30A")

    label("loc_2FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A")
    Event(0, 14)

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_END)), "loc_351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351")
    OP_A2(0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_351")

    Return()

    # Function_0_2D6 end

    def Function_1_352(): pass

    label("Function_1_352")

    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385")
    OP_6F(0x3, 0)
    Jump("loc_38C")

    label("loc_385")

    OP_6F(0x3, 60)

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E")
    OP_6F(0x4, 0)
    Jump("loc_3A5")

    label("loc_39E")

    OP_6F(0x4, 60)

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7")
    OP_6F(0x5, 0)
    Jump("loc_3BE")

    label("loc_3B7")

    OP_6F(0x5, 60)

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0")
    OP_6F(0x6, 0)
    Jump("loc_3D7")

    label("loc_3D0")

    OP_6F(0x6, 60)

    label("loc_3D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9")
    OP_6F(0x7, 0)
    Jump("loc_3F0")

    label("loc_3E9")

    OP_6F(0x7, 60)

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402")
    OP_6F(0x8, 0)
    Jump("loc_409")

    label("loc_402")

    OP_6F(0x8, 60)

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B")
    OP_6F(0x9, 0)
    Jump("loc_422")

    label("loc_41B")

    OP_6F(0x9, 60)

    label("loc_422")

    OP_10(0xE, 0x0)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_10(0x10, 0x0)
    OP_82(0x83, 0x0)
    Jump("loc_49D")

    label("loc_44C")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 600)
    OP_10(0x10, 0x1)
    OP_82(0x83, 0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_1B(0x10, 0x0, 0xD)

    label("loc_49D")

    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_352 end

    def Function_2_4A3(): pass

    label("Function_2_4A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4A3")

    label("loc_4B8")

    Return()

    # Function_2_4A3 end

    def Function_3_4B9(): pass

    label("Function_3_4B9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_591")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_528")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2383)
    Jump("loc_58E")

    label("loc_528")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x01\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_58E")

    Jump("loc_5C2")

    label("loc_591")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4B9 end

    def Function_4_5D0(): pass

    label("Function_4_5D0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_63F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2384)
    Jump("loc_6A5")

    label("loc_63F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
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

    label("loc_6A5")

    Jump("loc_6D9")

    label("loc_6A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6D9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5D0 end

    def Function_5_6E7(): pass

    label("Function_5_6E7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_756")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2385)
    Jump("loc_7BC")

    label("loc_756")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_7BC")

    Jump("loc_7F0")

    label("loc_7BF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7F0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6E7 end

    def Function_6_7FE(): pass

    label("Function_6_7FE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_86D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2386)
    Jump("loc_8D3")

    label("loc_86D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_8D3")

    Jump("loc_907")

    label("loc_8D6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_907")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7FE end

    def Function_7_915(): pass

    label("Function_7_915")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9ED")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_984")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2387)
    Jump("loc_9EA")

    label("loc_984")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_9EA")

    Jump("loc_A1E")

    label("loc_9ED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A1E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_915 end

    def Function_8_A2C(): pass

    label("Function_8_A2C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B04")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_A9B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2388)
    Jump("loc_B01")

    label("loc_A9B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x01\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_B01")

    Jump("loc_B35")

    label("loc_B04")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B35")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A2C end

    def Function_9_B43(): pass

    label("Function_9_B43")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C22")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_91(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_B95():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B95)

    def lambda_BB0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_BB0)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(    #18
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x532, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_BFD"),
        (2, "loc_C0F"),
        (1, "loc_C1F"),
        (SWITCH_DEFAULT, "loc_C22"),
    )


    label("loc_BFD")

    OP_A2(0x238A)
    OP_6F(0x9, 60)
    Sleep(500)
    Jump("loc_C22")

    label("loc_C0F")

    OP_6F(0x9, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_C1F")

    OP_B4(0x0)
    Return()

    label("loc_C22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x108, 1)"), scpexpr(EXPR_END)), "loc_C71")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\x08\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2389)
    Jump("loc_CD3")

    label("loc_C71")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #20
        (
            "宝箱里装有\x1F\x08\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x08\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_CD3")

    Jump("loc_D05")

    label("loc_CD6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D05")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_B43 end

    def Function_10_D13(): pass

    label("Function_10_D13")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-28890, 80, 108700, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(301000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)
    Sleep(1500)
    OP_22(0xE1, 0x0, 0x64)
    Sleep(3000)
    OP_22(0x70, 0x0, 0x64)
    OP_73(0x0)

    def lambda_D9B():
        OP_6D(-890, 1090, 98940, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9B)

    def lambda_DB3():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB3)
    OP_6C(315000, 5000)
    OP_6B(3500, 0)
    OP_6E(262, 0)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_D13 end

    def Function_11_E3C(): pass

    label("Function_11_E3C")

    EventBegin(0x0)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 100050, -1750, 9110, 0)
    OP_48()
    Fade(1000)
    OP_6D(100050, 0, 9110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 0, 10000, 0)
    OP_89(0x1, 101000, 0, 9000, 90)
    OP_89(0x2, 99000, 0, 9000, 270)
    OP_89(0x3, 100000, 0, 8000, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_EEC():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EEC)
    Sleep(500)

    def lambda_F0C():
        OP_6D(100050, 35000, 9110, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F0C)

    def lambda_F24():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F24)

    def lambda_F3C():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F3C)
    Sleep(500)

    def lambda_F51():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F51)
    Sleep(500)

    def lambda_F71():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F71)
    Sleep(400)

    def lambda_F91():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F91)
    Sleep(200)

    def lambda_FB1():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FB1)
    Sleep(100)

    def lambda_FD1():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FD1)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A2(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_E3C end

    def Function_12_102B(): pass

    label("Function_12_102B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 100050, 66000, 9110, 0)
    OP_48()
    OP_6D(100050, 48000, 9110, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 67000, 10000, 0)
    OP_89(0x1, 101000, 67000, 9000, 90)
    OP_89(0x2, 99000, 67000, 9000, 270)
    OP_89(0x3, 100000, 67000, 8000, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_10DA():
        OP_6D(100050, 0, 9110, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10DA)

    def lambda_10F2():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10F2)

    def lambda_110A():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_110A)
    FadeToBright(1000, 0)
    SetPlaceName(0x11F)

    def lambda_1126():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1126)
    Sleep(7800)

    def lambda_1146():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1146)
    Sleep(700)

    def lambda_1166():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1166)
    Sleep(600)

    def lambda_1186():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1186)
    Sleep(100)

    def lambda_11A6():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11A6)
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
    SetChrPos(0x0, 99940, 0, 4350, 180)
    SetChrPos(0x1, 99940, 0, 4350, 180)
    SetChrPos(0x2, 99940, 0, 4350, 180)
    SetChrPos(0x3, 99940, 0, 4350, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_12_102B end

    def Function_13_1277(): pass

    label("Function_13_1277")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-1000, 1050, 99000, 0)
    SetChrPos(0x101, -500, 1050, 98500, 180)
    SetChrPos(0x102, -1500, 1050, 98500, 180)
    SetChrPos(0xF8, -500, 1050, 99500, 180)
    SetChrPos(0xF9, -1500, 1050, 99500, 180)
    OP_0D()
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1322():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1322)

    def lambda_1334():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1334)

    def lambda_1346():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1346)

    def lambda_1358():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1358)
    Sleep(2000)
    NewScene("ED6_DT21/C5300   ._SN", 122, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1277 end

    def Function_14_1373(): pass

    label("Function_14_1373")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-1000, 1050, 99000, 0)
    SetChrPos(0x101, -1500, 1050, 99500, 0)
    SetChrPos(0x102, -500, 1050, 99500, 0)
    SetChrPos(0xF8, -1500, 1050, 98500, 0)
    SetChrPos(0xF9, -500, 1050, 98500, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_144E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_144E)

    def lambda_1460():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1460)

    def lambda_1472():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1472)

    def lambda_1484():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1484)
    Sleep(2500)
    Fade(500)
    OP_6D(-1000, 0, 103000, 0)
    SetChrPos(0x0, -1000, 0, 103000, 0)
    SetChrPos(0x1, -1000, 0, 103000, 0)
    SetChrPos(0x2, -1000, 0, 103000, 0)
    SetChrPos(0x3, -1000, 0, 103000, 0)
    EventEnd(0x0)
    Return()

    # Function_14_1373 end

    SaveToFile()

Try(main)
