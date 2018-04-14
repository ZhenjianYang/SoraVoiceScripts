from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1500   ._SN',
        MapName             = 'Bose',
        Location            = 'C1500.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60022",
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
        '',                                     # 9
        '',                                     # 10
        '古罗尼山道·关所方向',                 # 11
        '西柏斯街道方向',                       # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT09/CH10880 ._CH',             # 00
        'ED6_DT09/CH10881 ._CH',             # 01
        'ED6_DT09/CH11160 ._CH',             # 02
        'ED6_DT09/CH11161 ._CH',             # 03
        'ED6_DT09/CH10200 ._CH',             # 04
        'ED6_DT09/CH10201 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT29/CH12440 ._CH',             # 08
        'ED6_DT29/CH12441 ._CH',             # 09
        'ED6_DT29/CH12500 ._CH',             # 0A
        'ED6_DT29/CH13030 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT09/CH10880P._CP',             # 00
        'ED6_DT09/CH10881P._CP',             # 01
        'ED6_DT09/CH11160P._CP',             # 02
        'ED6_DT09/CH11161P._CP',             # 03
        'ED6_DT09/CH10200P._CP',             # 04
        'ED6_DT09/CH10201P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT29/CH12440P._CP',             # 08
        'ED6_DT29/CH12441P._CP',             # 09
        'ED6_DT29/CH12500P._CP',             # 0A
        'ED6_DT29/CH13030P._CP',             # 0B
    )

    DeclNpc(
        X                   = -134573,
        Z                   = 3995,
        Y                   = 87240,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -148670,
        Z                   = 4059,
        Y                   = 108220,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -140810,
        Z                   = 6010,
        Y                   = -31010,
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
        X                   = -119390,
        Z                   = -60,
        Y                   = 180920,
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
        X                   = -146390,
        Z                   = 2009,
        Y                   = 152190,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -148000,
        Z                   = 2090,
        Y                   = 136280,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154200,
        Z                   = 1990,
        Y                   = 120790,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154710,
        Z                   = 4070,
        Y                   = 99880,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154180,
        Z                   = 4030,
        Y                   = 76310,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -162330,
        Z                   = 4019,
        Y                   = 46020,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -131150,
        Z                   = 2040,
        Y                   = 55190,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -151910,
        Z                   = 5910,
        Y                   = -11960,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -151260,
        Z                   = 4040,
        Y                   = 20370,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -134573,
        Y                   = 3500,
        Z                   = 87240,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -157500,
        Y                   = 3000,
        Z                   = 105200,
        Range               = -142800,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x1B134,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -158410,
        TriggerZ            = 1970,
        TriggerY            = 120220,
        TriggerRange        = 1000,
        ActorX              = -158970,
        ActorZ              = 1970,
        ActorY              = 120040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -124550,
        TriggerZ            = 4019,
        TriggerY            = 90450,
        TriggerRange        = 1000,
        ActorX              = -123890,
        ActorZ              = 4019,
        ActorY              = 90020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -156400,
        TriggerZ            = 3930,
        TriggerY            = 80510,
        TriggerRange        = 1000,
        ActorX              = -156750,
        ActorZ              = 3930,
        ActorY              = 81120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -170750,
        TriggerZ            = 5900,
        TriggerY            = 3230,
        TriggerRange        = 1000,
        ActorX              = -171430,
        ActorZ              = 5900,
        ActorY              = 3350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -130810,
        TriggerZ            = 4050,
        TriggerY            = 21300,
        TriggerRange        = 1000,
        ActorX              = -130139,
        ActorZ              = 4050,
        ActorY              = 21690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37A",          # 00, 0
        "Function_1_37B",          # 01, 1
        "Function_2_475",          # 02, 2
        "Function_3_48B",          # 03, 3
        "Function_4_5A2",          # 04, 4
        "Function_5_6B9",          # 05, 5
        "Function_6_7D0",          # 06, 6
        "Function_7_8E7",          # 07, 7
        "Function_8_98C",          # 08, 8
        "Function_9_CAC",          # 09, 9
        "Function_10_FB0",         # 0A, 10
        "Function_11_19F1",        # 0B, 11
    )


    def Function_0_37A(): pass

    label("Function_0_37A")

    Return()

    # Function_0_37A end

    def Function_1_37B(): pass

    label("Function_1_37B")

    OP_16(0x2, 0xFA0, 0xFFFBED08, 0xFFFF2540, 0x23003E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F")
    OP_6F(0x0, 0)
    Jump("loc_3A6")

    label("loc_39F")

    OP_6F(0x0, 60)

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8")
    OP_6F(0x1, 0)
    Jump("loc_3BF")

    label("loc_3B8")

    OP_6F(0x1, 60)

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1")
    OP_6F(0x2, 0)
    Jump("loc_3D8")

    label("loc_3D1")

    OP_6F(0x2, 60)

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EA")
    OP_6F(0x3, 0)
    Jump("loc_3F1")

    label("loc_3EA")

    OP_6F(0x3, 60)

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403")
    OP_6F(0x4, 0)
    Jump("loc_40A")

    label("loc_403")

    OP_6F(0x4, 60)

    label("loc_40A")

    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_46A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_455")
    OP_8C(0x9, 180, 0)

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467")
    ClearChrFlags(0x9, 0x80)
    OP_B2(0x1, 0x1, 0x80)

    label("loc_467")

    Jump("loc_474")

    label("loc_46A")

    SetChrFlags(0x9, 0x80)
    OP_B2(0x0, 0x1, 0x80)

    label("loc_474")

    Return()

    # Function_1_37B end

    def Function_2_475(): pass

    label("Function_2_475")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_475")

    label("loc_48A")

    Return()

    # Function_2_475 end

    def Function_3_48B(): pass

    label("Function_3_48B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_563")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_4FA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B70)
    Jump("loc_560")

    label("loc_4FA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_560")

    Jump("loc_594")

    label("loc_563")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_594")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_48B end

    def Function_4_5A2(): pass

    label("Function_4_5A2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_611")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B71)
    Jump("loc_677")

    label("loc_611")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_677")

    Jump("loc_6AB")

    label("loc_67A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6AB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5A2 end

    def Function_5_6B9(): pass

    label("Function_5_6B9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_791")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_728")
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
    OP_A2(0x1B72)
    Jump("loc_78E")

    label("loc_728")

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
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_78E")

    Jump("loc_7C2")

    label("loc_791")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6B9 end

    def Function_6_7D0(): pass

    label("Function_6_7D0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_83F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B73)
    Jump("loc_8A5")

    label("loc_83F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_8A5")

    Jump("loc_8D9")

    label("loc_8A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8D9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7D0 end

    def Function_7_8E7(): pass

    label("Function_7_8E7")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_960")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    AddSepith(0x0, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B74)
    Jump("loc_97A")

    label("loc_960")


    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_97A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_8E7 end

    def Function_8_98C(): pass

    label("Function_8_98C")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_99C"),
        (101, "loc_AEE"),
        (SWITCH_DEFAULT, "loc_C40"),
    )


    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 6)), scpexpr(EXPR_END)), "loc_9A4")
    Return()

    label("loc_9A4")

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

    AnonymousTalk(    #14
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
        (1, "loc_A89"),
        (SWITCH_DEFAULT, "loc_AAC"),
    )


    label("loc_A89")

    Fade(500)
    OP_89(0x0, -148540, 2360, 114080, 156)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_AAC")

    Battle(0xEED, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -148540, 2360, 114080, 156)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_AE5"),
        (1, "loc_AE8"),
        (SWITCH_DEFAULT, "loc_AEB"),
    )


    label("loc_AE5")

    EventEnd(0x0)
    Return()

    label("loc_AE8")

    OP_B4(0x0)
    Return()

    label("loc_AEB")

    Jump("loc_C40")

    label("loc_AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 6)), scpexpr(EXPR_END)), "loc_AF6")
    Return()

    label("loc_AF6")

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

    AnonymousTalk(    #15
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
        (1, "loc_BDB"),
        (SWITCH_DEFAULT, "loc_BFE"),
    )


    label("loc_BDB")

    Fade(500)
    OP_89(0x0, -148760, 3940, 101000, 18)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_BFE")

    Battle(0xEF7, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -148760, 3940, 101000, 18)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_C37"),
        (1, "loc_C3A"),
        (SWITCH_DEFAULT, "loc_C3D"),
    )


    label("loc_C37")

    EventEnd(0x0)
    Return()

    label("loc_C3A")

    OP_B4(0x0)
    Return()

    label("loc_C3D")

    Jump("loc_C40")

    label("loc_C40")

    EventBegin(0x1)
    SetChrFlags(0x9, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x20F6)
    OP_28(0xB5, 0x4, 0x10)
    OP_28(0xB5, 0x4, 0x2)
    OP_28(0xB5, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_8_98C end

    def Function_9_CAC(): pass

    label("Function_9_CAC")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #17
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
        (0, "loc_D15"),
        (1, "loc_F45"),
        (SWITCH_DEFAULT, "loc_FAD"),
    )


    label("loc_D15")

    Battle(0xD3, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D36"),
        (2, "loc_EC5"),
        (1, "loc_F3D"),
        (SWITCH_DEFAULT, "loc_F42"),
    )


    label("loc_D36")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD7")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【◇消灭了琥珀之塔和迷雾峡谷的通缉魔兽】\x01",      # 0
            "【◇什么也没有变更】\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DC2"),
        (SWITCH_DEFAULT, "loc_DD7"),
    )


    label("loc_DC2")

    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_28(0xB2, 0x1, 0x1)
    OP_28(0xB3, 0x1, 0x1)
    Jump("loc_DD7")

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE9")
    Call(0, 10)
    Jump("loc_EC2")

    label("loc_DE9")

    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -136150, 4030, 88170, 135)
    SetChrPos(0x1, -136150, 4030, 88170, 135)
    SetChrPos(0x2, -136150, 4030, 88170, 135)
    SetChrPos(0x3, -136150, 4030, 88170, 135)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05消灭了古罗尼山顶的通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1A0E)
    OP_28(0xB1, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x2)
    OP_28(0x93, 0x1, 0x4)
    OP_28(0x93, 0x1, 0x8)
    Sleep(400)

    label("loc_EC2")

    Jump("loc_F42")

    label("loc_EC5")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -138230, 4019, 89590, 135)
    SetChrPos(0x1, -138230, 4019, 89590, 135)
    SetChrPos(0x2, -138230, 4019, 89590, 135)
    SetChrPos(0x3, -138230, 4019, 89590, 135)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_F42")

    label("loc_F3D")

    OP_B4(0x0)
    Jump("loc_F42")

    label("loc_F42")

    Jump("loc_FAD")

    label("loc_F45")

    Fade(500)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -138230, 4019, 89590, 135)
    SetChrPos(0x1, -138230, 4019, 89590, 135)
    SetChrPos(0x2, -138230, 4019, 89590, 135)
    SetChrPos(0x3, -138230, 4019, 89590, 135)
    OP_69(0x0, 0x0)
    OP_0D()
    Jump("loc_FAD")

    label("loc_FAD")

    EventEnd(0x0)
    Return()

    # Function_9_CAC end

    def Function_10_FB0(): pass

    label("Function_10_FB0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC3")
    Call(0, 11)

    label("loc_FC3")

    OP_6D(-135710, 4050, 87980, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(260000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -136610, 4010, 88580, 135)
    SetChrPos(0x106, -136320, 4010, 87160, 45)
    SetChrPos(0xF8, -134790, 4030, 89020, 225)
    SetChrPos(0xF9, -134630, 4000, 87460, 315)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #19
        0x101,
        (
            "#1007F哈～总算是解决了啊。\x02\x03",

            "#1002F不过……\x01",
            "这些魔兽的样子似乎很奇怪啊？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x18\x07\x05是哪里和平时不同了呢？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【魔兽变强了】\x01",        # 0
            "【魔兽变胆怯了】\x01",      # 1
            "【魔兽非常兴奋】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1151"),
        (1, "loc_132A"),
        (2, "loc_14DD"),
        (SWITCH_DEFAULT, "loc_1690"),
    )


    label("loc_1151")

    OP_2B(0x93, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C6")

    ChrTalk(    #21
        0x108,
        (
            "#072F那也没错……\x01",
            "不过更明显的是它们的性情变了。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1321")

    label("loc_11C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_123C")

    ChrTalk(    #22
        0x103,
        (
            "#022F那也说的没错……\x01",
            "不过更明显的是它们的性情变了哦。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1321")

    label("loc_123C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B4")

    ChrTalk(    #23
        0x104,
        (
            "#032F嗯，那也说的不错，\x01",
            "不过更明显的是它们的性情变了哦。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1321")

    label("loc_12B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1321")

    ChrTalk(    #24
        0x105,
        (
            "#043F那样说也对，\x01",
            "不过更明显的是它们的性情变了。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1321")

    OP_28(0x93, 0x1, 0x400)
    Jump("loc_1690")

    label("loc_132A")

    OP_2B(0x93, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_139B")

    ChrTalk(    #25
        0x108,
        (
            "#072F啊啊～不管什么样的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D4")

    label("loc_139B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1405")

    ChrTalk(    #26
        0x103,
        (
            "#022F哎～不管什么样的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D4")

    label("loc_1405")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_146D")

    ChrTalk(    #27
        0x104,
        (
            "#032F嗯，哪个地方的魔兽\x01",
            "都好像很奇怪啊。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D4")

    label("loc_146D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D4")

    ChrTalk(    #28
        0x105,
        (
            "#042F是啊，不管什么样的魔兽\x01",
            "也都很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D4")

    OP_28(0x93, 0x1, 0x1000)
    Jump("loc_1690")

    label("loc_14DD")

    OP_2B(0x93, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154E")

    ChrTalk(    #29
        0x108,
        (
            "#072F啊啊～不管什么样的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1687")

    label("loc_154E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B8")

    ChrTalk(    #30
        0x103,
        (
            "#022F哎～不管什么样的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1687")

    label("loc_15B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1620")

    ChrTalk(    #31
        0x104,
        (
            "#032F嗯，哪个地方的魔兽\x01",
            "都好像很奇怪啊。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1687")

    label("loc_1620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1687")

    ChrTalk(    #32
        0x105,
        (
            "#042F是啊，不管什么样的魔兽\x01",
            "也都很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1687")

    OP_28(0x93, 0x1, 0x800)
    Jump("loc_1690")

    label("loc_1690")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D8")

    ChrTalk(    #33
        0x107,
        (
            "#065F我、我也\x01",
            "有那种感觉。\x02\x03",

            "#561F好、好可怕啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AD")

    label("loc_16D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_171F")

    ChrTalk(    #34
        0x105,
        (
            "#043F我也……\x01",
            "有那种感觉啊。\x02\x03",

            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AD")

    label("loc_171F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1766")

    ChrTalk(    #35
        0x104,
        (
            "#032F我也有\x01",
            "同样的感觉呢。\x02\x03",

            "嗯，到底是为什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AD")

    label("loc_1766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17AD")

    ChrTalk(    #36
        0x103,
        (
            "#026F我也有同感啊。\x02\x03",

            "#522F嗯……\x01",
            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AD")


    ChrTalk(    #37
        0x106,
        "#057F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1004F嗯？　怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x106,
        (
            "#555F啊，没什么……\x02\x03",

            "或许这是\x01",
            "某种前兆也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1020F前兆……\x01",
            "难道是『结社』！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x106,
        (
            "#552F那就不知道了……\x01",
            "不过以前也发生过类似的状况。\x02\x03",

            "魔兽突然就变得\x01",
            "仓惶不安…\x02\x03",

            "之后……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1004F？？？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F7")

    ChrTalk(    #43
        0x107,
        "#063F阿加特哥哥……？\x02",
    )

    CloseMessageWindow()

    label("loc_18F7")


    ChrTalk(    #44
        0x106,
        (
            "#053F算了，今天就这样吧。\x02\x03",

            "#057F不管怎么说，动物的直觉\x01",
            "有时候比人更敏锐的，\x02\x03",

            "我们也必须准备应付\x01",
            "随时可能出现的特殊情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1002F嗯……明白了。\x02\x03",

            "那么…\x01",
            "我们暂时先返回协会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x106,
        "#050F啊啊～就这样办吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A0E)
    OP_28(0xB1, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x2)
    OP_28(0x93, 0x1, 0x4)
    OP_28(0x93, 0x1, 0x8)
    OP_28(0x93, 0x1, 0x2000)
    EventEnd(0x0)
    Return()

    # Function_10_FB0 end

    def Function_11_19F1(): pass

    label("Function_11_19F1")

    FadeToDark(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_1AA8"),
        (1, "loc_1AAE"),
        (SWITCH_DEFAULT, "loc_1AB4"),
    )


    label("loc_1AA8")

    OP_A2(0x1200)
    Jump("loc_1AB4")

    label("loc_1AAE")

    OP_A2(0x1201)
    Jump("loc_1AB4")

    label("loc_1AB4")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_19F1 end

    SaveToFile()

Try(main)
