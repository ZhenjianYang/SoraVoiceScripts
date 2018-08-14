from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4260   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4260.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        'ED6_DT29/CH14510 ._CH',             # 00
        'ED6_DT29/CH14511 ._CH',             # 01
        'ED6_DT29/CH14790 ._CH',             # 02
        'ED6_DT29/CH14790 ._CH',             # 03
        'ED6_DT29/CH14450 ._CH',             # 04
        'ED6_DT29/CH14451 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14510P._CP',             # 00
        'ED6_DT29/CH14511P._CP',             # 01
        'ED6_DT29/CH14790P._CP',             # 02
        'ED6_DT29/CH14790P._CP',             # 03
        'ED6_DT29/CH14450P._CP',             # 04
        'ED6_DT29/CH14451P._CP',             # 05
    )

    DeclMonster(
        X                   = -240,
        Z                   = 500,
        Y                   = 151710,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7290,
        Z                   = 0,
        Y                   = 142410,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7970,
        Z                   = 0,
        Y                   = 139890,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 2260,
        TriggerZ            = 500,
        TriggerY            = 156570,
        TriggerRange        = 1000,
        ActorX              = 2260,
        ActorZ              = 1500,
        ActorY              = 156570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_153",          # 01, 1
        "Function_2_178",          # 02, 2
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Return()

    # Function_0_152 end

    def Function_1_153(): pass

    label("Function_1_153")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170")
    OP_6F(0x16, 0)
    Jump("loc_177")

    label("loc_170")

    OP_6F(0x16, 60)

    label("loc_177")

    Return()

    # Function_1_153 end

    def Function_2_178(): pass

    label("Function_2_178")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x167, 1)"), scpexpr(EXPR_END)), "loc_1EA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x67\x01\x07\x00。\x02",
    )

    Jump("loc_1CF")

    label("loc_1CF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27A3)
    Jump("loc_256")

    label("loc_1EA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x67\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x67\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_237")

    label("loc_237")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x16, 60)
    OP_70(0x16, 0x0)

    label("loc_256")

    Jump("loc_28A")

    label("loc_259")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_28A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_178 end

    SaveToFile()

Try(main)
