from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7411   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7411.x',
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
        '斯莱普尼尔',                           # 9
        '圣剑天使',                             # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH14610 ._CH',             # 00
        'ED6_DT29/CH14611 ._CH',             # 01
        'ED6_DT29/CH14040 ._CH',             # 02
        'ED6_DT29/CH14041 ._CH',             # 03
        'ED6_DT29/CH14880 ._CH',             # 04
        'ED6_DT29/CH14880 ._CH',             # 05
        'ED6_DT29/CH14890 ._CH',             # 06
        'ED6_DT29/CH14890 ._CH',             # 07
        'ED6_DT29/CH14870 ._CH',             # 08
        'ED6_DT29/CH14870 ._CH',             # 09
        'ED6_DT29/CH14820 ._CH',             # 0A
        'ED6_DT29/CH14820 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14610P._CP',             # 00
        'ED6_DT29/CH14611P._CP',             # 01
        'ED6_DT29/CH14040P._CP',             # 02
        'ED6_DT29/CH14041P._CP',             # 03
        'ED6_DT29/CH14880P._CP',             # 04
        'ED6_DT29/CH14880P._CP',             # 05
        'ED6_DT29/CH14890P._CP',             # 06
        'ED6_DT29/CH14890P._CP',             # 07
        'ED6_DT29/CH14870P._CP',             # 08
        'ED6_DT29/CH14870P._CP',             # 09
        'ED6_DT29/CH14820P._CP',             # 0A
        'ED6_DT29/CH14820P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 13990,
        Z                   = -10000,
        Y                   = -65940,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x321,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 23210,
        Z                   = -6000,
        Y                   = -88210,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x322,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10950,
        Z                   = -14000,
        Y                   = -165050,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 32710,
        Y                   = -1000,
        Z                   = 99830,
        Range               = 41470,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x191FE,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 65000,
        TriggerZ            = 0,
        TriggerY            = 99000,
        TriggerRange        = 1000,
        ActorX              = 65000,
        ActorZ              = 1000,
        ActorY              = 99000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 0,
        TriggerY            = 37000,
        TriggerRange        = 1000,
        ActorX              = 40000,
        ActorZ              = 1000,
        ActorY              = 37000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34000,
        TriggerZ            = 0,
        TriggerY            = 37000,
        TriggerRange        = 1000,
        ActorX              = 34000,
        ActorZ              = 1000,
        ActorY              = 37000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11000,
        TriggerZ            = -14000,
        TriggerY            = -168800,
        TriggerRange        = 1000,
        ActorX              = 11000,
        ActorZ              = -13000,
        ActorY              = -168800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14780,
        TriggerZ            = -14000,
        TriggerY            = -165010,
        TriggerRange        = 1000,
        ActorX              = 14780,
        ActorZ              = -13000,
        ActorY              = -165010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7180,
        TriggerZ            = -14000,
        TriggerY            = -165080,
        TriggerRange        = 1000,
        ActorX              = 7180,
        ActorZ              = -13000,
        ActorY              = -165080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23240,
        TriggerZ            = 0,
        TriggerY            = 22810,
        TriggerRange        = 1000,
        ActorX              = 23240,
        ActorZ              = 2000,
        ActorY              = 22810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BA",          # 00, 0
        "Function_1_319",          # 01, 1
        "Function_2_3FD",          # 02, 2
        "Function_3_47C",          # 03, 3
        "Function_4_5A2",          # 04, 4
        "Function_5_6C8",          # 05, 5
        "Function_6_747",          # 06, 6
        "Function_7_7C6",          # 07, 7
        "Function_8_845",          # 08, 8
        "Function_9_9FE",          # 09, 9
        "Function_10_1048",        # 0A, 10
        "Function_11_1085",        # 0B, 11
    )


    def Function_0_2BA(): pass

    label("Function_0_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_318")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 36950, 500, 112440, 180)

    def lambda_2E2():

        label("loc_2E2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2E2")

    QueueWorkItem2(0x10, 3, lambda_2E2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 38340, 2500, 112370, 180)

    def lambda_30B():

        label("loc_30B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_30B")

    QueueWorkItem2(0x11, 3, lambda_30B)

    label("loc_318")

    Return()

    # Function_0_2BA end

    def Function_1_319(): pass

    label("Function_1_319")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378")
    OP_6F(0x0, 0)
    Jump("loc_37F")

    label("loc_378")

    OP_6F(0x0, 60)

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391")
    OP_6F(0x1, 0)
    Jump("loc_398")

    label("loc_391")

    OP_6F(0x1, 60)

    label("loc_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA")
    OP_6F(0x2, 0)
    Jump("loc_3B1")

    label("loc_3AA")

    OP_6F(0x2, 60)

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3")
    OP_6F(0x3, 0)
    Jump("loc_3CA")

    label("loc_3C3")

    OP_6F(0x3, 60)

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC")
    OP_6F(0x4, 0)
    Jump("loc_3E3")

    label("loc_3DC")

    OP_6F(0x4, 60)

    label("loc_3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5")
    OP_6F(0x5, 0)
    Jump("loc_3FC")

    label("loc_3F5")

    OP_6F(0x5, 60)

    label("loc_3FC")

    Return()

    # Function_1_319 end

    def Function_2_3FD(): pass

    label("Function_2_3FD")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E")
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
    OP_A2(0x2C88)
    Jump("loc_46A")

    label("loc_44E")


    AnonymousTalk(    #0
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_46A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3FD end

    def Function_3_47C(): pass

    label("Function_3_47C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_4F0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_4D5")

    label("loc_4D5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C89)
    Jump("loc_55E")

    label("loc_4F0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_53F")

    label("loc_53F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_55E")

    Jump("loc_594")

    label("loc_561")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
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

    # Function_3_47C end

    def Function_4_5A2(): pass

    label("Function_4_5A2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_687")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_616")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_5FB")

    label("loc_5FB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C8A)
    Jump("loc_684")

    label("loc_616")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_665")

    label("loc_665")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_684")

    Jump("loc_6BA")

    label("loc_687")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5A2 end

    def Function_5_6C8(): pass

    label("Function_5_6C8")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_719")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x1E)
    OP_73(0x3)
    OP_6F(0x3, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C8B)
    Jump("loc_735")

    label("loc_719")


    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_735")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6C8 end

    def Function_6_747(): pass

    label("Function_6_747")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_798")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 28)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C8C)
    Jump("loc_7B4")

    label("loc_798")


    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_7B4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_747 end

    def Function_7_7C6(): pass

    label("Function_7_7C6")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x591, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_817")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C8D)
    Jump("loc_833")

    label("loc_817")


    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_833")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_7C6 end

    def Function_8_845(): pass

    label("Function_8_845")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #10
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_872")

    label("loc_872")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_885")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DD")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_8D7")

    label("loc_8D7")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8F4"),
        (1, "loc_96F"),
        (2, "loc_99E"),
        (SWITCH_DEFAULT, "loc_9CD"),
    )


    label("loc_8F4")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DA")

    label("loc_96F")

    OP_A9(0x32)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #11
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_99B")

    label("loc_99B")

    Jump("loc_9DA")

    label("loc_99E")

    OP_A9(0xE)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_9CA")

    label("loc_9CA")

    Jump("loc_9DA")

    label("loc_9CD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9DA")

    label("loc_9DA")

    Jump("loc_885")

    label("loc_9DD")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_8_845 end

    def Function_9_9FE(): pass

    label("Function_9_9FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 5)), scpexpr(EXPR_END)), "loc_A06")
    Return()

    label("loc_A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 6)), scpexpr(EXPR_END)), "loc_B08")
    EventBegin(0x0)
    Fade(500)
    OP_E0(0, 0x4C, 0x2)
    OP_E0(1, 0x4D, 0x2)
    OP_E0(2, 0x4E, 0x2)
    OP_E0(3, 0x4F, 0x2)
    SetChrPos(0x0, 36630, 0, 100330, 0)
    SetChrPos(0x1, 37870, 0, 100060, 0)
    SetChrPos(0x2, 36060, 0, 98580, 0)
    SetChrPos(0x3, 37750, 0, 98370, 0)
    OP_6D(38700, 0, 105540, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(45000, 0)
    OP_6E(431, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 12)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 13)
    SetChrSubChip(0x1, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 14)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 15)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)
    Jump("loc_D48")

    label("loc_B08")

    EventBegin(0x0)
    OP_E0(0, 0x4C, 0x2)
    OP_E0(1, 0x4D, 0x2)
    OP_E0(2, 0x4E, 0x2)
    OP_E0(3, 0x4F, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 36950, 2500, 112440, 180)

    def lambda_B3A():

        label("loc_B3A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B3A")

    QueueWorkItem2(0x10, 3, lambda_B3A)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 38340, 5500, 112370, 180)

    def lambda_B6E():

        label("loc_B6E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B6E")

    QueueWorkItem2(0x11, 3, lambda_B6E)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_BA8():
        OP_6D(38880, 750, 112980, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_BA8)

    def lambda_BC0():
        OP_67(0, 4850, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BC0)

    def lambda_BD8():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BD8)

    def lambda_BE8():
        OP_6E(431, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_BE8)

    def lambda_BF8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BF8)
    Sleep(100)

    def lambda_C0B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C0B)
    Sleep(100)

    def lambda_C1E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C1E)
    Sleep(100)
    OP_8C(0x3, 0, 400)
    WaitChrThread(0x0, 0x0)
    SetChrPos(0x0, 36630, 0, 100330, 0)
    SetChrPos(0x1, 37870, 0, 100060, 0)
    SetChrPos(0x2, 36060, 0, 98580, 0)
    SetChrPos(0x3, 37750, 0, 98370, 0)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x11, 0x0, 0x0, 0xB)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)

    def lambda_C9E():
        OP_6D(38700, 0, 105540, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C9E)

    def lambda_CB6():
        OP_67(0, 5390, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_CB6)

    def lambda_CCE():
        OP_6B(2640, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_CCE)

    def lambda_CDE():
        OP_6E(431, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_CDE)
    WaitChrThread(0x0, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 12)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 13)
    SetChrSubChip(0x1, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 14)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 15)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)

    label("loc_D48")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D57():
        OP_6D(38510, 0, 102760, 450)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D57)

    def lambda_D6F():
        OP_67(0, 5760, -10000, 450)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_D6F)

    def lambda_D87():
        OP_6B(1920, 450)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_D87)

    def lambda_D97():
        OP_6E(370, 450)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_D97)
    SetChrChipByIndex(0x11, 3)

    def lambda_DAC():
        OP_8F(0xFE, 0x91C8, 0x3E8, 0x189CA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_DAC)

    def lambda_DC7():

        label("loc_DC7")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_DC7")

    QueueWorkItem2(0x11, 3, lambda_DC7)
    Sleep(50)
    SetChrChipByIndex(0x10, 1)

    def lambda_DE4():
        OP_8F(0xFE, 0x91C8, 0x1F4, 0x189CA, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DE4)

    def lambda_DFF():

        label("loc_DFF")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_DFF")

    QueueWorkItem2(0x10, 3, lambda_DFF)
    WaitChrThread(0x0, 0x3)
    Battle(0x330, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E3E"),
        (2, "loc_F0F"),
        (1, "loc_1032"),
        (SWITCH_DEFAULT, "loc_1037"),
    )


    label("loc_E3E")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(36970, 0, 102660, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, 36970, 0, 102660, 0)
    SetChrPos(0x1, 36970, 0, 102660, 0)
    SetChrPos(0x2, 36970, 0, 102660, 0)
    SetChrPos(0x3, 36970, 0, 102660, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C2D)
    Jump("loc_1037")

    label("loc_F0F")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 36950, 500, 112440, 180)

    def lambda_F46():

        label("loc_F46")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F46")

    QueueWorkItem2(0x10, 3, lambda_F46)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 38340, 2500, 112370, 180)

    def lambda_F6F():

        label("loc_F6F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F6F")

    QueueWorkItem2(0x11, 3, lambda_F6F)
    OP_6D(37150, 0, 97400, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, 37150, 0, 97400, 0)
    SetChrPos(0x1, 37150, 0, 97400, 0)
    SetChrPos(0x2, 37150, 0, 97400, 0)
    SetChrPos(0x3, 37150, 0, 97400, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C2E)
    Jump("loc_1037")

    label("loc_1032")

    OP_B4(0x0)
    Jump("loc_1037")

    label("loc_1037")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_9FE end

    def Function_10_1048(): pass

    label("Function_10_1048")


    def lambda_104E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_104E)

    def lambda_1060():
        OP_8F(0xFE, 0x9056, 0x1F4, 0x1B738, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1060)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_10_1048 end

    def Function_11_1085(): pass

    label("Function_11_1085")


    def lambda_108B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_108B)

    def lambda_109D():
        OP_8F(0xFE, 0x95C4, 0x9C4, 0x1B6F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_109D)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_11_1085 end

    SaveToFile()

Try(main)
