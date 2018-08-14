from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7412   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7412.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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
            'ED6_DT21/SUB000  ._SN',
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
        'ED6_DT29/CH14040 ._CH',             # 00
        'ED6_DT29/CH14040 ._CH',             # 01
        'ED6_DT29/CH14880 ._CH',             # 02
        'ED6_DT29/CH14880 ._CH',             # 03
        'ED6_DT29/CH14890 ._CH',             # 04
        'ED6_DT29/CH14890 ._CH',             # 05
        'ED6_DT29/CH14870 ._CH',             # 06
        'ED6_DT29/CH14870 ._CH',             # 07
        'ED6_DT29/CH14820 ._CH',             # 08
        'ED6_DT29/CH14820 ._CH',             # 09
        'ED6_DT29/CH14610 ._CH',             # 0A
        'ED6_DT29/CH14610 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14040P._CP',             # 00
        'ED6_DT29/CH14040P._CP',             # 01
        'ED6_DT29/CH14880P._CP',             # 02
        'ED6_DT29/CH14880P._CP',             # 03
        'ED6_DT29/CH14890P._CP',             # 04
        'ED6_DT29/CH14890P._CP',             # 05
        'ED6_DT29/CH14870P._CP',             # 06
        'ED6_DT29/CH14870P._CP',             # 07
        'ED6_DT29/CH14820P._CP',             # 08
        'ED6_DT29/CH14820P._CP',             # 09
        'ED6_DT29/CH14610P._CP',             # 0A
        'ED6_DT29/CH14610P._CP',             # 0B
    )

    DeclMonster(
        X                   = 10110,
        Z                   = 0,
        Y                   = 22070,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x320,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 137140,
        Z                   = -6000,
        Y                   = 11380,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x321,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32640,
        Z                   = -6000,
        Y                   = 8050,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x325,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19470,
        Z                   = -6000,
        Y                   = 13930,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x322,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19690,
        Z                   = -6000,
        Y                   = 1510,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x321,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 22170,
        TriggerZ            = -6000,
        TriggerY            = 8000,
        TriggerRange        = 1000,
        ActorX              = 22170,
        ActorZ              = -5000,
        ActorY              = 8000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25920,
        TriggerZ            = -6000,
        TriggerY            = 4280,
        TriggerRange        = 1000,
        ActorX              = 25920,
        ActorZ              = -5000,
        ActorY              = 4280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26010,
        TriggerZ            = -6000,
        TriggerY            = 11800,
        TriggerRange        = 1000,
        ActorX              = 26010,
        ActorZ              = -5000,
        ActorY              = 11800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_203",          # 01, 1
        "Function_2_30F",          # 02, 2
        "Function_3_38C",          # 03, 3
        "Function_4_4AC",          # 04, 4
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Return()

    # Function_0_202 end

    def Function_1_203(): pass

    label("Function_1_203")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_235")
    OP_E5(0x0, 0xFF, 0x1D, 1)
    OP_E5(0x0, 0xFF, 0x1, 1)
    OP_E5(0x1, 0xFF, 0x1E, 1)
    OP_E5(0x1, 0xFF, 0x2, 1)
    Jump("loc_255")

    label("loc_235")

    OP_E5(0x1, 0xFF, 0x1D, 1)
    OP_E5(0x1, 0xFF, 0x1, 1)
    OP_E5(0x0, 0xFF, 0x1E, 1)
    OP_E5(0x0, 0xFF, 0x2, 1)

    label("loc_255")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x592, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D5")
    OP_6F(0x0, 0)
    Jump("loc_2DC")

    label("loc_2D5")

    OP_6F(0x0, 60)

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x592, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE")
    OP_6F(0x1, 0)
    Jump("loc_2F5")

    label("loc_2EE")

    OP_6F(0x1, 60)

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x592, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307")
    OP_6F(0x2, 0)
    Jump("loc_30E")

    label("loc_307")

    OP_6F(0x2, 60)

    label("loc_30E")

    Return()

    # Function_1_203 end

    def Function_2_30F(): pass

    label("Function_2_30F")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x592, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_360")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 28)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C90)
    Jump("loc_37A")

    label("loc_360")


    AnonymousTalk(    #0
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_37A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_30F end

    def Function_3_38C(): pass

    label("Function_3_38C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x592, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_3FE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_3E3")

    label("loc_3E3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C91)
    Jump("loc_46A")

    label("loc_3FE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_44B")

    label("loc_44B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_46A")

    Jump("loc_49E")

    label("loc_46D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_49E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_38C end

    def Function_4_4AC(): pass

    label("Function_4_4AC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x592, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_51E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    Jump("loc_503")

    label("loc_503")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C92)
    Jump("loc_58A")

    label("loc_51E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x05\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_56B")

    label("loc_56B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_58A")

    Jump("loc_5BE")

    label("loc_58D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5BE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4AC end

    SaveToFile()

Try(main)
