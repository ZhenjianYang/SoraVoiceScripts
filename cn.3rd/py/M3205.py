from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3205   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3205.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        'ED6_DT07/CH00330 ._CH',             # 00
        'ED6_DT07/CH00331 ._CH',             # 01
        'ED6_DT07/CH00430 ._CH',             # 02
        'ED6_DT07/CH00431 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00330P._CP',             # 00
        'ED6_DT07/CH00331P._CP',             # 01
        'ED6_DT07/CH00430P._CP',             # 02
        'ED6_DT07/CH00431P._CP',             # 03
    )

    DeclMonster(
        X                   = 870,
        Z                   = 0,
        Y                   = -23390,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 38850,
        Z                   = 0,
        Y                   = 3720,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 67250,
        Z                   = 0,
        Y                   = 14860,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15230,
        Z                   = 0,
        Y                   = 18680,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6640,
        Z                   = 0,
        Y                   = 82520,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1190,
        Z                   = 0,
        Y                   = 136940,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1030,
        Z                   = 0,
        Y                   = 153140,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -960,
        TriggerZ            = 0,
        TriggerY            = 171820,
        TriggerRange        = 1000,
        ActorX              = -960,
        ActorZ              = 800,
        ActorY              = 171820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1000,
        TriggerZ            = 0,
        TriggerY            = -17000,
        TriggerRange        = 1000,
        ActorX              = 1000,
        ActorZ              = 1000,
        ActorY              = -17000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -29000,
        TriggerZ            = 0,
        TriggerY            = 49500,
        TriggerRange        = 1000,
        ActorX              = -29000,
        ActorZ              = 1000,
        ActorY              = 49500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3000,
        TriggerZ            = 0,
        TriggerY            = -17000,
        TriggerRange        = 1000,
        ActorX              = 3000,
        ActorZ              = 1000,
        ActorY              = -17000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1000,
        TriggerZ            = 0,
        TriggerY            = -17000,
        TriggerRange        = 1000,
        ActorX              = -1000,
        ActorZ              = 1000,
        ActorY              = -17000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_243",          # 01, 1
        "Function_2_2BD",          # 02, 2
        "Function_3_3E3",          # 03, 3
        "Function_4_509",          # 04, 4
        "Function_5_660",          # 05, 5
        "Function_6_786",          # 06, 6
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Return()

    # Function_0_242 end

    def Function_1_243(): pass

    label("Function_1_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_254")
    OP_72(0x100A, 0x0)
    ExitThread()
    Jump("loc_258")

    label("loc_254")

    OP_64(0x0, 0x1)

    label("loc_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x566, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A")
    OP_6F(0x2E, 0)
    Jump("loc_271")

    label("loc_26A")

    OP_6F(0x2E, 60)

    label("loc_271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x566, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283")
    OP_6F(0x2F, 0)
    Jump("loc_28A")

    label("loc_283")

    OP_6F(0x2F, 60)

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x566, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C")
    OP_6F(0x30, 0)
    Jump("loc_2A3")

    label("loc_29C")

    OP_6F(0x30, 60)

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x566, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5")
    OP_6F(0x31, 0)
    Jump("loc_2BC")

    label("loc_2B5")

    OP_6F(0x31, 60)

    label("loc_2BC")

    Return()

    # Function_1_243 end

    def Function_2_2BD(): pass

    label("Function_2_2BD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x566, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x175, 1)"), scpexpr(EXPR_END)), "loc_331")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x75\x01\x07\x00。\x02",
    )

    Jump("loc_316")

    label("loc_316")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B34)
    Jump("loc_39F")

    label("loc_331")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x75\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x75\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_380")

    label("loc_380")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_39F")

    Jump("loc_3D5")

    label("loc_3A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3D5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2BD end

    def Function_3_3E3(): pass

    label("Function_3_3E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x566, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_457")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    Jump("loc_43C")

    label("loc_43C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B35)
    Jump("loc_4C5")

    label("loc_457")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x06\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4A6")

    label("loc_4A6")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2F, 60)
    OP_70(0x2F, 0x0)

    label("loc_4C5")

    Jump("loc_4FB")

    label("loc_4C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3E3 end

    def Function_4_509(): pass

    label("Function_4_509")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x566, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_632")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x30, 0x1E)
    OP_73(0x30)
    OP_6F(0x30, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #6
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x02#62I时之耀晶片×２００\x01",
            "\x07\x02#60I空之耀晶片×２００\x01",
            "\x07\x02#61I幻之耀晶片×２００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2B36)
    Jump("loc_64E")

    label("loc_632")


    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_64E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_509 end

    def Function_5_660(): pass

    label("Function_5_660")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x566, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_745")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x31, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_6D4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_6B9")

    label("loc_6B9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B37)
    Jump("loc_742")

    label("loc_6D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_723")

    label("loc_723")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x31, 60)
    OP_70(0x31, 0x0)

    label("loc_742")

    Jump("loc_778")

    label("loc_745")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_778")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_660 end

    def Function_6_786(): pass

    label("Function_6_786")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #11
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 0)), scpexpr(EXPR_END)), "loc_88E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88E")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "使用Ｃ－０２钥匙\x01",      # 0
            "不使用\x01",                # 1
        )
    )

    Jump("loc_834")

    label("loc_834")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_85A"),
        (SWITCH_DEFAULT, "loc_87E"),
    )


    label("loc_85A")

    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x2B82)
    OP_71(0x100A, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88B")

    label("loc_87E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88B")

    label("loc_88B")

    Jump("loc_7FD")

    label("loc_88E")

    TalkEnd(0xFF)
    Return()

    # Function_6_786 end

    SaveToFile()

Try(main)
