from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U2511   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U2511.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        'ED6_DT29/CH15140 ._CH',             # 00
        'ED6_DT29/CH15141 ._CH',             # 01
        'ED6_DT29/CH14650 ._CH',             # 02
        'ED6_DT29/CH14651 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT29/CH15140P._CP',             # 00
        'ED6_DT29/CH15141P._CP',             # 01
        'ED6_DT29/CH14650P._CP',             # 02
        'ED6_DT29/CH14651P._CP',             # 03
    )

    DeclMonster(
        X                   = 0,
        Z                   = 0,
        Y                   = -3110,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 11080,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31070,
        Z                   = 0,
        Y                   = 25910,
        Unknown_0C          = 90,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x272,
        Unknown_18          = 11081,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -100,
        Z                   = 0,
        Y                   = 40660,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x270,
        Unknown_18          = 11082,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 0,
        Z                   = 0,
        Y                   = -3110,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x270,
        Unknown_18          = 11080,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31070,
        Z                   = 0,
        Y                   = 25910,
        Unknown_0C          = 90,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x270,
        Unknown_18          = 11081,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -100,
        Z                   = 0,
        Y                   = 40660,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x270,
        Unknown_18          = 11082,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x20,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 30590,
        TriggerZ            = 0,
        TriggerY            = 52600,
        TriggerRange        = 1000,
        ActorX              = 30590,
        ActorZ              = 1000,
        ActorY              = 52600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5080,
        TriggerZ            = 0,
        TriggerY            = 6520,
        TriggerRange        = 1000,
        ActorX              = -5080,
        ActorZ              = 1000,
        ActorY              = 6520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_25C",          # 01, 1
        "Function_2_328",          # 02, 2
        "Function_3_44A",          # 03, 3
        "Function_4_4E8",          # 04, 4
        "Function_5_537",          # 05, 5
        "Function_6_590",          # 06, 6
        "Function_7_5E9",          # 07, 7
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1EF")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 7)

    label("loc_1EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_END)), "loc_208")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_23B")

    label("loc_208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_23B")

    label("loc_222")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x12, 0x80)

    label("loc_23B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 0)), scpexpr(EXPR_END)), "loc_24F")
    SetChrFlags(0x10, 0x80)

    label("loc_24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 1)), scpexpr(EXPR_END)), "loc_25B")
    SetChrFlags(0x11, 0x80)

    label("loc_25B")

    Return()

    # Function_0_1DA end

    def Function_1_25C(): pass

    label("Function_1_25C")

    OP_B1("U2511_n")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x271), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_282")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_282")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x272), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_297")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_297")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x270), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3")
    Event(0, 5)

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 2)), scpexpr(EXPR_END)), "loc_2F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_END)), "loc_2D8")
    Event(0, 6)
    Jump("loc_2F5")

    label("loc_2D8")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_A3(0x2B48)
    OP_A3(0x2B49)
    OP_A3(0x2B4A)

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307")
    OP_6F(0x4, 0)
    Jump("loc_30E")

    label("loc_307")

    OP_6F(0x4, 60)

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320")
    OP_6F(0x5, 0)
    Jump("loc_327")

    label("loc_320")

    OP_6F(0x5, 60)

    label("loc_327")

    Return()

    # Function_1_25C end

    def Function_2_328(): pass

    label("Function_2_328")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x617, 1)"), scpexpr(EXPR_END)), "loc_39C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x17\x06\x07\x00。\x02",
    )

    Jump("loc_381")

    label("loc_381")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BA2)
    Jump("loc_408")

    label("loc_39C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x17\x06\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x17\x06\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3E9")

    label("loc_3E9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_408")

    Jump("loc_43C")

    label("loc_40B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_43C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_328 end

    def Function_3_44A(): pass

    label("Function_3_44A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x574, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    AnonymousTalk(    #3
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_4AA")

    label("loc_4AA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BA3)
    Jump("loc_4D6")

    label("loc_4BC")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4D6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_44A end

    def Function_4_4E8(): pass

    label("Function_4_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_END)), "loc_514")
    OP_C0(0x1F, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_536")

    label("loc_514")

    OP_C0(0x1F, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_536")

    Return()

    # Function_4_4E8 end

    def Function_5_537(): pass

    label("Function_5_537")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B48)
    OP_A3(0x2B49)
    OP_A3(0x2B4A)
    OP_A2(0x2B4B)
    OP_28(0x37, 0x1, 0x20)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2511   ._SN", 100, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_537 end

    def Function_6_590(): pass

    label("Function_6_590")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B48)
    OP_A3(0x2B49)
    OP_A3(0x2B4A)
    OP_A3(0x2B4B)
    OP_28(0x37, 0x1, 0x40)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2511   ._SN", 100, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_590 end

    def Function_7_5E9(): pass

    label("Function_7_5E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    label("loc_62E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B4")
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 0, 0, -3110, 180)
    SetChrPos(0x1, 0, 0, -3110, 180)
    SetChrPos(0x2, 0, 0, -3110, 180)
    SetChrPos(0x3, 0, 0, -3110, 180)
    OP_69(0x0, 0x0)
    Jump("loc_7BD")

    label("loc_6B4")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73A")
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 28940, 0, 25990, 270)
    SetChrPos(0x1, 28940, 0, 25990, 270)
    SetChrPos(0x2, 28940, 0, 25990, 270)
    SetChrPos(0x3, 28940, 0, 25990, 270)
    OP_69(0x0, 0x0)
    Jump("loc_7BD")

    label("loc_73A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BD")
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -100, 0, 40660, 0)
    SetChrPos(0x1, -100, 0, 40660, 0)
    SetChrPos(0x2, -100, 0, 40660, 0)
    SetChrPos(0x3, -100, 0, 40660, 0)
    OP_69(0x0, 0x0)

    label("loc_7BD")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_5E9 end

    SaveToFile()

Try(main)
