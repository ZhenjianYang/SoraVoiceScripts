from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7303   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
        'ED6_DT29/CH14720 ._CH',             # 00
        'ED6_DT29/CH14721 ._CH',             # 01
        'ED6_DT29/CH14550 ._CH',             # 02
        'ED6_DT29/CH14551 ._CH',             # 03
        'ED6_DT29/CH14440 ._CH',             # 04
        'ED6_DT29/CH14440 ._CH',             # 05
        'ED6_DT29/CH14760 ._CH',             # 06
        'ED6_DT29/CH14761 ._CH',             # 07
        'ED6_DT29/CH14770 ._CH',             # 08
        'ED6_DT29/CH14771 ._CH',             # 09
        'ED6_DT29/CH14340 ._CH',             # 0A
        'ED6_DT29/CH14340 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14720P._CP',             # 00
        'ED6_DT29/CH14721P._CP',             # 01
        'ED6_DT29/CH14550P._CP',             # 02
        'ED6_DT29/CH14551P._CP',             # 03
        'ED6_DT29/CH14440P._CP',             # 04
        'ED6_DT29/CH14440P._CP',             # 05
        'ED6_DT29/CH14760P._CP',             # 06
        'ED6_DT29/CH14761P._CP',             # 07
        'ED6_DT29/CH14770P._CP',             # 08
        'ED6_DT29/CH14771P._CP',             # 09
        'ED6_DT29/CH14340P._CP',             # 0A
        'ED6_DT29/CH14340P._CP',             # 0B
    )

    DeclMonster(
        X                   = 4210,
        Z                   = 6370,
        Y                   = 20460,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17400,
        Z                   = 18420,
        Y                   = 67270,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17440,
        Z                   = 29070,
        Y                   = 96760,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 42270,
        Z                   = 33920,
        Y                   = 102780,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -3870,
        TriggerZ            = 7750,
        TriggerY            = 26660,
        TriggerRange        = 1000,
        ActorX              = -3870,
        ActorZ              = 8750,
        ActorY              = 26660,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -17060,
        TriggerZ            = 20800,
        TriggerY            = 97960,
        TriggerRange        = 1000,
        ActorX              = -17060,
        ActorZ              = 21800,
        ActorY              = 97960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21880,
        TriggerZ            = 29050,
        TriggerY            = 88850,
        TriggerRange        = 1000,
        ActorX              = 21880,
        ActorZ              = 30050,
        ActorY              = 88850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_1E7",          # 01, 1
        "Function_2_265",          # 02, 2
        "Function_3_385",          # 03, 3
        "Function_4_4A5",          # 04, 4
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Return()

    # Function_0_1E6 end

    def Function_1_1E7(): pass

    label("Function_1_1E7")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF30F8, 0x230096)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B")
    OP_6F(0x0, 0)
    Jump("loc_232")

    label("loc_22B")

    OP_6F(0x0, 60)

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244")
    OP_6F(0x1, 0)
    Jump("loc_24B")

    label("loc_244")

    OP_6F(0x1, 60)

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D")
    OP_6F(0x2, 0)
    Jump("loc_264")

    label("loc_25D")

    OP_6F(0x2, 60)

    label("loc_264")

    Return()

    # Function_1_1E7 end

    def Function_2_265(): pass

    label("Function_2_265")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1C8, 1)"), scpexpr(EXPR_END)), "loc_2D7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xC8\x01\x07\x00。\x02",
    )

    Jump("loc_2BC")

    label("loc_2BC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C66)
    Jump("loc_343")

    label("loc_2D7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xC8\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xC8\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_324")

    label("loc_324")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_343")

    Jump("loc_377")

    label("loc_346")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_377")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_265 end

    def Function_3_385(): pass

    label("Function_3_385")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1C9, 1)"), scpexpr(EXPR_END)), "loc_3F7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xC9\x01\x07\x00。\x02",
    )

    Jump("loc_3DC")

    label("loc_3DC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C67)
    Jump("loc_463")

    label("loc_3F7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xC9\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xC9\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_444")

    label("loc_444")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_463")

    Jump("loc_497")

    label("loc_466")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_497")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_385 end

    def Function_4_4A5(): pass

    label("Function_4_4A5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_586")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x180, 1)"), scpexpr(EXPR_END)), "loc_517")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x80\x01\x07\x00。\x02",
    )

    Jump("loc_4FC")

    label("loc_4FC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C6F)
    Jump("loc_583")

    label("loc_517")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x80\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x80\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_564")

    label("loc_564")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_583")

    Jump("loc_5B7")

    label("loc_586")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5B7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4A5 end

    SaveToFile()

Try(main)
