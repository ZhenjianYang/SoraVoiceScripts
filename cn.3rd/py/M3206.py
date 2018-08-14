from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3206   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3206.x',
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
        X                   = -53080,
        Z                   = 0,
        Y                   = -93410,
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
        X                   = 7910,
        Z                   = 0,
        Y                   = -105070,
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
        X                   = 12690,
        Z                   = 0,
        Y                   = -17420,
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
        X                   = 1140,
        Z                   = 0,
        Y                   = 18960,
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
        X                   = 96950,
        Z                   = 0,
        Y                   = 52790,
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
        X                   = -33000,
        Z                   = 0,
        Y                   = 2009,
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
        X                   = 29780,
        Z                   = 0,
        Y                   = 92670,
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
        X                   = 16890,
        Z                   = 0,
        Y                   = 147050,
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
        X                   = -1050,
        Z                   = 0,
        Y                   = 216930,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -970,
        TriggerZ            = 0,
        TriggerY            = 243890,
        TriggerRange        = 1000,
        ActorX              = -970,
        ActorZ              = 800,
        ActorY              = 243890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5860,
        TriggerZ            = 0,
        TriggerY            = -17010,
        TriggerRange        = 1000,
        ActorX              = 5860,
        ActorZ              = 1000,
        ActorY              = -17010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3000,
        TriggerZ            = 0,
        TriggerY            = -61000,
        TriggerRange        = 1000,
        ActorX              = 3000,
        ActorZ              = 1000,
        ActorY              = -61000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 99080,
        TriggerZ            = 0,
        TriggerY            = 52790,
        TriggerRange        = 1000,
        ActorX              = 99080,
        ActorZ              = 1000,
        ActorY              = 52790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96260,
        TriggerZ            = 0,
        TriggerY            = 19230,
        TriggerRange        = 1000,
        ActorX              = 96260,
        ActorZ              = 1000,
        ActorY              = 19230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 81040,
        TriggerZ            = 0,
        TriggerY            = 118550,
        TriggerRange        = 1000,
        ActorX              = 81040,
        ActorZ              = 1000,
        ActorY              = 118550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_29E",          # 00, 0
        "Function_1_29F",          # 01, 1
        "Function_2_332",          # 02, 2
        "Function_3_458",          # 03, 3
        "Function_4_5AF",          # 04, 4
        "Function_5_6D5",          # 05, 5
        "Function_6_7FB",          # 06, 6
        "Function_7_921",          # 07, 7
    )


    def Function_0_29E(): pass

    label("Function_0_29E")

    Return()

    # Function_0_29E end

    def Function_1_29F(): pass

    label("Function_1_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B0")
    OP_72(0x1000, 0x0)
    ExitThread()
    Jump("loc_2B4")

    label("loc_2B0")

    OP_64(0x0, 0x1)

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6")
    OP_6F(0x36, 0)
    Jump("loc_2CD")

    label("loc_2C6")

    OP_6F(0x36, 60)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF")
    OP_6F(0x37, 0)
    Jump("loc_2E6")

    label("loc_2DF")

    OP_6F(0x37, 60)

    label("loc_2E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F8")
    OP_6F(0x38, 0)
    Jump("loc_2FF")

    label("loc_2F8")

    OP_6F(0x38, 60)

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311")
    OP_6F(0x39, 0)
    Jump("loc_318")

    label("loc_311")

    OP_6F(0x39, 60)

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A")
    OP_6F(0x3A, 0)
    Jump("loc_331")

    label("loc_32A")

    OP_6F(0x3A, 60)

    label("loc_331")

    Return()

    # Function_1_29F end

    def Function_2_332(): pass

    label("Function_2_332")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x36, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x33C, 1)"), scpexpr(EXPR_END)), "loc_3A6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x3C\x03\x07\x00。\x02",
    )

    Jump("loc_38B")

    label("loc_38B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BFB)
    Jump("loc_414")

    label("loc_3A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x3C\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x3C\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3F5")

    label("loc_3F5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x36, 60)
    OP_70(0x36, 0x0)

    label("loc_414")

    Jump("loc_44A")

    label("loc_417")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_44A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_332 end

    def Function_3_458(): pass

    label("Function_3_458")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_581")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x37, 0x1E)
    OP_73(0x37)
    OP_6F(0x37, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #3
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
    OP_A2(0x2B38)
    Jump("loc_59D")

    label("loc_581")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_59D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_458 end

    def Function_4_5AF(): pass

    label("Function_4_5AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x38, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D7, 1)"), scpexpr(EXPR_END)), "loc_623")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xD7\x02\x07\x00。\x02",
    )

    Jump("loc_608")

    label("loc_608")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B39)
    Jump("loc_691")

    label("loc_623")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xD7\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xD7\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_672")

    label("loc_672")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x38, 60)
    OP_70(0x38, 0x0)

    label("loc_691")

    Jump("loc_6C7")

    label("loc_694")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6C7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5AF end

    def Function_5_6D5(): pass

    label("Function_5_6D5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x39, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_749")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_72E")

    label("loc_72E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B3A)
    Jump("loc_7B7")

    label("loc_749")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_798")

    label("loc_798")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x39, 60)
    OP_70(0x39, 0x0)

    label("loc_7B7")

    Jump("loc_7ED")

    label("loc_7BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7ED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6D5 end

    def Function_6_7FB(): pass

    label("Function_6_7FB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_86F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_854")

    label("loc_854")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B3B)
    Jump("loc_8DD")

    label("loc_86F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_8BE")

    label("loc_8BE")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3A, 60)
    OP_70(0x3A, 0x0)

    label("loc_8DD")

    Jump("loc_913")

    label("loc_8E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_913")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7FB end

    def Function_7_921(): pass

    label("Function_7_921")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #14
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 3)), scpexpr(EXPR_END)), "loc_A29")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_998")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A29")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "使用Ｃ－０３钥匙\x01",      # 0
            "不使用\x01",                # 1
        )
    )

    Jump("loc_9CF")

    label("loc_9CF")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9F5"),
        (SWITCH_DEFAULT, "loc_A19"),
    )


    label("loc_9F5")

    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x2B7C)
    OP_71(0x1000, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A26")

    label("loc_A19")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A26")

    label("loc_A26")

    Jump("loc_998")

    label("loc_A29")

    TalkEnd(0xFF)
    Return()

    # Function_7_921 end

    SaveToFile()

Try(main)
