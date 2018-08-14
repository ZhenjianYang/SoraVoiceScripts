from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4262   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4262.x',
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
        X                   = -72510,
        Z                   = 0,
        Y                   = 2230,
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
        X                   = -141100,
        Z                   = 0,
        Y                   = 1690,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86150,
        Z                   = 0,
        Y                   = 57780,
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
        X                   = -28000,
        Z                   = 0,
        Y                   = -57120,
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
        TriggerX            = -148010,
        TriggerZ            = 0,
        TriggerY            = -680,
        TriggerRange        = 1000,
        ActorX              = -148010,
        ActorZ              = 1000,
        ActorY              = -680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16E",          # 00, 0
        "Function_1_16F",          # 01, 1
        "Function_2_194",          # 02, 2
    )


    def Function_0_16E(): pass

    label("Function_0_16E")

    Return()

    # Function_0_16E end

    def Function_1_16F(): pass

    label("Function_1_16F")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C")
    OP_6F(0x21, 0)
    Jump("loc_193")

    label("loc_18C")

    OP_6F(0x21, 60)

    label("loc_193")

    Return()

    # Function_1_16F end

    def Function_2_194(): pass

    label("Function_2_194")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16A, 1)"), scpexpr(EXPR_END)), "loc_206")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x6A\x01\x07\x00。\x02",
    )

    Jump("loc_1EB")

    label("loc_1EB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27A5)
    Jump("loc_272")

    label("loc_206")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x6A\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x6A\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_253")

    label("loc_253")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_272")

    Jump("loc_2A6")

    label("loc_275")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2A6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_194 end

    SaveToFile()

Try(main)
