from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5505   ._SN',
        MapName             = 'Other',
        Location            = 'C5505.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12180 ._CH',             # 00
        'ED6_DT29/CH12181 ._CH',             # 01
        'ED6_DT29/CH12230 ._CH',             # 02
        'ED6_DT29/CH12231 ._CH',             # 03
        'ED6_DT29/CH12270 ._CH',             # 04
        'ED6_DT29/CH12271 ._CH',             # 05
        'ED6_DT29/CH12360 ._CH',             # 06
        'ED6_DT29/CH12361 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12180P._CP',             # 00
        'ED6_DT29/CH12181P._CP',             # 01
        'ED6_DT29/CH12230P._CP',             # 02
        'ED6_DT29/CH12231P._CP',             # 03
        'ED6_DT29/CH12270P._CP',             # 04
        'ED6_DT29/CH12271P._CP',             # 05
        'ED6_DT29/CH12360P._CP',             # 06
        'ED6_DT29/CH12361P._CP',             # 07
    )

    DeclNpc(
        X                   = -26690,
        Z                   = 1000,
        Y                   = 13420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -26150,
        Z                   = 0,
        Y                   = -18160,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9050,
        Z                   = 0,
        Y                   = -1650,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 350,
        Z                   = 0,
        Y                   = -14310,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37130,
        Z                   = 0,
        Y                   = -6030,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16500,
        Z                   = 0,
        Y                   = 22960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24260,
        Z                   = 0,
        Y                   = 2230,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32920,
        Z                   = 0,
        Y                   = 21400,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 40970,
        TriggerZ            = 0,
        TriggerY            = -12100,
        TriggerRange        = 1000,
        ActorX              = 41400,
        ActorZ              = 0,
        ActorY              = -12530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26690,
        TriggerZ            = 0,
        TriggerY            = 14080,
        TriggerRange        = 1000,
        ActorX              = -26690,
        ActorZ              = 0,
        ActorY              = 13420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_216",          # 00, 0
        "Function_1_217",          # 01, 1
        "Function_2_254",          # 02, 2
        "Function_3_26A",          # 03, 3
        "Function_4_385",          # 04, 4
        "Function_5_4A0",          # 05, 5
    )


    def Function_0_216(): pass

    label("Function_0_216")

    Return()

    # Function_0_216 end

    def Function_1_217(): pass

    label("Function_1_217")

    OP_22(0x1CD, 0x0, 0x64)
    OP_22(0x1CE, 0x1, 0x50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233")
    OP_6F(0x0, 0)
    Jump("loc_23A")

    label("loc_233")

    OP_6F(0x0, 60)

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C")
    OP_6F(0x1, 0)
    Jump("loc_253")

    label("loc_24C")

    OP_6F(0x1, 60)

    label("loc_253")

    Return()

    # Function_1_217 end

    def Function_2_254(): pass

    label("Function_2_254")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_269")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_254")

    label("loc_269")

    Return()

    # Function_2_254 end

    def Function_3_26A(): pass

    label("Function_3_26A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_342")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x125, 1)"), scpexpr(EXPR_END)), "loc_2D9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x25\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1121)
    Jump("loc_33F")

    label("loc_2D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x25\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x25\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_33F")

    Jump("loc_373")

    label("loc_342")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_373")

    Sleep(30)
    Call(0, 5)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_26A end

    def Function_4_385(): pass

    label("Function_4_385")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x104, 1)"), scpexpr(EXPR_END)), "loc_3F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x04\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1122)
    Jump("loc_45A")

    label("loc_3F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x04\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x04\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_45A")

    Jump("loc_48E")

    label("loc_45D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_48E")

    Sleep(30)
    Call(0, 5)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_385 end

    def Function_5_4A0(): pass

    label("Function_5_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_562")

    ChrTalk(    #6
        0x101,
        (
            "#1004F啊……！\x02\x03",

            "难不成，这个\x01",
            "就是我们的装备？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#811F嗯，似乎是呢⊙\x02\x03",

            "#1310F说不定其它装备\x01",
            "也被藏在什么地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006F嗯～\x01",
            "虽然想避开和魔兽的战斗，\x01",
            "但似乎值得探索一下呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x100F)

    label("loc_562")

    Return()

    # Function_5_4A0 end

    SaveToFile()

Try(main)
