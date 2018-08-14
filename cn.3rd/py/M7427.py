from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7427   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7427.x',
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
        'ED6_DT29/CH14840 ._CH',             # 0C
        'ED6_DT29/CH14840 ._CH',             # 0D
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
        'ED6_DT29/CH14840P._CP',             # 0C
        'ED6_DT29/CH14840P._CP',             # 0D
    )

    DeclMonster(
        X                   = -250,
        Z                   = -3000,
        Y                   = 8710,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x323,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40,
        Z                   = -3000,
        Y                   = 30,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x323,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -490,
        Z                   = -3000,
        Y                   = -8400,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x323,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 113180,
        Z                   = 0,
        Y                   = 0,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 117030,
        Z                   = 0,
        Y                   = 3800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 120750,
        Z                   = 0,
        Y                   = 0,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 116990,
        Z                   = 0,
        Y                   = -3800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -103220,
        Z                   = 0,
        Y                   = 0,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -106960,
        Z                   = 0,
        Y                   = -3800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -110800,
        Z                   = 0,
        Y                   = 0,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -106970,
        Z                   = 0,
        Y                   = 3800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -3000,
        TriggerY            = 5030,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -2000,
        ActorY              = 5030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10,
        TriggerZ            = -3000,
        TriggerY            = -4820,
        TriggerRange        = 1000,
        ActorX              = 10,
        ActorZ              = -2000,
        ActorY              = -4820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 116990,
        TriggerZ            = 0,
        TriggerY            = -20,
        TriggerRange        = 1000,
        ActorX              = 116990,
        ActorZ              = 1000,
        ActorY              = -20,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -106970,
        TriggerZ            = 0,
        TriggerY            = -10,
        TriggerRange        = 1000,
        ActorX              = -106970,
        ActorZ              = 1000,
        ActorY              = -10,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2DE",          # 00, 0
        "Function_1_2DF",          # 01, 1
        "Function_2_39C",          # 02, 2
        "Function_3_419",          # 03, 3
        "Function_4_496",          # 04, 4
        "Function_5_5B6",          # 05, 5
    )


    def Function_0_2DE(): pass

    label("Function_0_2DE")

    Return()

    # Function_0_2DE end

    def Function_1_2DF(): pass

    label("Function_1_2DF")

    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349")
    OP_6F(0x0, 0)
    Jump("loc_350")

    label("loc_349")

    OP_6F(0x0, 60)

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362")
    OP_6F(0x1, 0)
    Jump("loc_369")

    label("loc_362")

    OP_6F(0x1, 60)

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B")
    OP_6F(0x2, 0)
    Jump("loc_382")

    label("loc_37B")

    OP_6F(0x2, 60)

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394")
    OP_6F(0x3, 0)
    Jump("loc_39B")

    label("loc_394")

    OP_6F(0x3, 60)

    label("loc_39B")

    Return()

    # Function_1_2DF end

    def Function_2_39C(): pass

    label("Function_2_39C")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED")
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
    OP_A2(0x2CD4)
    Jump("loc_407")

    label("loc_3ED")


    AnonymousTalk(    #0
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_407")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_39C end

    def Function_3_419(): pass

    label("Function_3_419")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CD5)
    Jump("loc_484")

    label("loc_46A")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_484")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_419 end

    def Function_4_496(): pass

    label("Function_4_496")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_577")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_508")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_4ED")

    label("loc_4ED")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CD6)
    Jump("loc_574")

    label("loc_508")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_555")

    label("loc_555")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_574")

    Jump("loc_5A8")

    label("loc_577")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5A8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_496 end

    def Function_5_5B6(): pass

    label("Function_5_5B6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x181, 1)"), scpexpr(EXPR_END)), "loc_628")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x81\x01\x07\x00。\x02",
    )

    Jump("loc_60D")

    label("loc_60D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CD7)
    Jump("loc_694")

    label("loc_628")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x81\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x81\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_675")

    label("loc_675")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_694")

    Jump("loc_6C8")

    label("loc_697")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5B6 end

    SaveToFile()

Try(main)
