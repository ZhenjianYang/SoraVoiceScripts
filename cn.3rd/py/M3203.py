from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3203   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3203.x',
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
        '摩尔根将军',                           # 9
        '王国军将校',                           # 10
        '王国军将校',                           # 11
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
        'ED6_DT07/CH02080 ._CH',             # 00
        'ED6_DT27/CH04430 ._CH',             # 01
        'ED6_DT27/CH04431 ._CH',             # 02
        'ED6_DT27/CH04434 ._CH',             # 03
        'ED6_DT27/CH04435 ._CH',             # 04
        'ED6_DT07/CH00330 ._CH',             # 05
        'ED6_DT07/CH00331 ._CH',             # 06
        'ED6_DT07/CH00430 ._CH',             # 07
        'ED6_DT07/CH00431 ._CH',             # 08
        'ED6_DT09/CH10060 ._CH',             # 09
        'ED6_DT09/CH10061 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02080P._CP',             # 00
        'ED6_DT27/CH04430P._CP',             # 01
        'ED6_DT27/CH04431P._CP',             # 02
        'ED6_DT27/CH04434P._CP',             # 03
        'ED6_DT27/CH04435P._CP',             # 04
        'ED6_DT07/CH00330P._CP',             # 05
        'ED6_DT07/CH00331P._CP',             # 06
        'ED6_DT07/CH00430P._CP',             # 07
        'ED6_DT07/CH00431P._CP',             # 08
        'ED6_DT09/CH10060P._CP',             # 09
        'ED6_DT09/CH10061P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -40800,
        Z                   = 0,
        Y                   = 21190,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -67070,
        Z                   = 0,
        Y                   = 2120,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1110,
        Z                   = 0,
        Y                   = -48520,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 1060,
        TriggerZ            = 0,
        TriggerY            = 5760,
        TriggerRange        = 1000,
        ActorX              = 1060,
        ActorZ              = 800,
        ActorY              = 5760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30940,
        TriggerZ            = 0,
        TriggerY            = -48030,
        TriggerRange        = 1000,
        ActorX              = 30940,
        ActorZ              = 1000,
        ActorY              = -48030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39470,
        TriggerZ            = 120,
        TriggerY            = 43240,
        TriggerRange        = 1000,
        ActorX              = -39470,
        ActorZ              = 1120,
        ActorY              = 43240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 39920,
        TriggerZ            = 120,
        TriggerY            = 1330,
        TriggerRange        = 1000,
        ActorX              = 39920,
        ActorZ              = 1120,
        ActorY              = 1330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 39930,
        TriggerZ            = 120,
        TriggerY            = -1080,
        TriggerRange        = 1000,
        ActorX              = 39930,
        ActorZ              = 1120,
        ActorY              = -1080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4130,
        TriggerZ            = 0,
        TriggerY            = 34910,
        TriggerRange        = 1000,
        ActorX              = 4130,
        ActorZ              = 2000,
        ActorY              = 34910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28E",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_32E",          # 02, 2
        "Function_3_454",          # 03, 3
        "Function_4_57A",          # 04, 4
        "Function_5_6D1",          # 05, 5
        "Function_6_7F7",          # 06, 6
        "Function_7_903",          # 07, 7
        "Function_8_90C",          # 08, 8
        "Function_9_25CD",         # 09, 9
        "Function_10_2622",        # 0A, 10
        "Function_11_2677",        # 0B, 11
        "Function_12_3B81",        # 0C, 12
        "Function_13_3C40",        # 0D, 13
    )


    def Function_0_28E(): pass

    label("Function_0_28E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B3")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_2B3")

    Return()

    # Function_0_28E end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB")
    OP_6F(0x38, 0)
    Jump("loc_2E2")

    label("loc_2DB")

    OP_6F(0x38, 60)

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4")
    OP_6F(0x39, 0)
    Jump("loc_2FB")

    label("loc_2F4")

    OP_6F(0x39, 60)

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D")
    OP_6F(0x3A, 0)
    Jump("loc_314")

    label("loc_30D")

    OP_6F(0x3A, 60)

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326")
    OP_6F(0x3B, 0)
    Jump("loc_32D")

    label("loc_326")

    OP_6F(0x3B, 60)

    label("loc_32D")

    Return()

    # Function_1_2B4 end

    def Function_2_32E(): pass

    label("Function_2_32E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_413")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x38, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x336, 1)"), scpexpr(EXPR_END)), "loc_3A2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x36\x03\x07\x00。\x02",
    )

    Jump("loc_387")

    label("loc_387")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B90)
    Jump("loc_410")

    label("loc_3A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x36\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x36\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3F1")

    label("loc_3F1")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x38, 60)
    OP_70(0x38, 0x0)

    label("loc_410")

    Jump("loc_446")

    label("loc_413")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_446")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_32E end

    def Function_3_454(): pass

    label("Function_3_454")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x39, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_4C8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    Jump("loc_4AD")

    label("loc_4AD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B91)
    Jump("loc_536")

    label("loc_4C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x01\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_517")

    label("loc_517")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x39, 60)
    OP_70(0x39, 0x0)

    label("loc_536")

    Jump("loc_56C")

    label("loc_539")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_56C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_454 end

    def Function_4_57A(): pass

    label("Function_4_57A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3A, 0x1E)
    OP_73(0x3A)
    OP_6F(0x3A, 30)
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
    OP_A2(0x2B92)
    Jump("loc_6BF")

    label("loc_6A3")


    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6BF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_57A end

    def Function_5_6D1(): pass

    label("Function_5_6D1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_745")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_72A")

    label("loc_72A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B93)
    Jump("loc_7B3")

    label("loc_745")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_794")

    label("loc_794")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3B, 60)
    OP_70(0x3B, 0x0)

    label("loc_7B3")

    Jump("loc_7E9")

    label("loc_7B6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7E9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6D1 end

    def Function_6_7F7(): pass

    label("Function_6_7F7")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x571, 0)), scpexpr(EXPR_END)), "loc_8FF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FF")

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

    Jump("loc_8A5")

    label("loc_8A5")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8CB"),
        (SWITCH_DEFAULT, "loc_8EF"),
    )


    label("loc_8CB")

    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x2B82)
    OP_71(0x1004, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FC")

    label("loc_8EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FC")

    label("loc_8FC")

    Jump("loc_86E")

    label("loc_8FF")

    TalkEnd(0xFF)
    Return()

    # Function_6_7F7 end

    def Function_7_903(): pass

    label("Function_7_903")

    Call(0, 8)
    Call(0, 11)
    Return()

    # Function_7_903 end

    def Function_8_90C(): pass

    label("Function_8_90C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x4B, 0x2)
    OP_E0(238, 0x4C, 0x3)
    OP_E0(239, 0x4D, 0x2)
    OP_E0(239, 0x4E, 0x3)
    OP_E0(240, 0x4F, 0x2)
    OP_E0(240, 0x50, 0x3)
    OP_E0(241, 0x51, 0x2)
    OP_E0(241, 0x52, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 610, 0, 78790, 180)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -170, 0, 65019, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EC")
    SetChrPos(0xEF, 1490, 0, 65030, 0)
    SetChrPos(0xF0, -640, 0, 63180, 0)
    SetChrPos(0xF1, 1650, 0, 63540, 0)
    Jump("loc_A71")

    label("loc_9EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30")
    SetChrPos(0xF0, 1490, 0, 65030, 0)
    SetChrPos(0xEF, -640, 0, 63180, 0)
    SetChrPos(0xF1, 1650, 0, 63540, 0)
    Jump("loc_A71")

    label("loc_A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A71")
    SetChrPos(0xF1, 1490, 0, 65030, 0)
    SetChrPos(0xEF, -640, 0, 63180, 0)
    SetChrPos(0xF0, 1650, 0, 63540, 0)

    label("loc_A71")

    OP_6D(1590, 0, 65300, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(45000, 0)
    OP_6E(290, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #12
        0x10,
        "老人的声音",
        (
            "#4S#4P太慢了！\x01",
            "你们在干什么！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B42")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BA9")

    label("loc_B42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BA9")

    label("loc_B6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B92")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BA9")

    label("loc_B92")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BA9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD6")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C3D")

    label("loc_BD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C3D")

    label("loc_BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C26")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C3D")

    label("loc_C26")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C3D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CD1")

    label("loc_C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C92")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CD1")

    label("loc_C92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CD1")

    label("loc_CBA")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CD1")

    Sleep(1000)

    ChrTalk(    #13
        0x109,
        "#1064F#6P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10C,
        "#112F#12P你是……！\x02",
    )

    CloseMessageWindow()

    def lambda_D1C():
        OP_8F(0xFE, 0xFFFFFDF8, 0x0, 0x11A8A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D1C)
    Sleep(100)

    def lambda_D3C():
        OP_6D(1530, 0, 75920, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_D3C)

    def lambda_D54():
        OP_67(0, 5080, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_D54)

    def lambda_D6C():
        OP_6B(2480, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_D6C)

    def lambda_D7C():
        OP_6E(341, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_D7C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF2")

    def lambda_D9A():
        OP_8F(0xFE, 0x442, 0x0, 0x11A3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_D9A)
    Sleep(100)

    def lambda_DBA():
        OP_8F(0xFE, 0xFFFFFC2C, 0x0, 0x11350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_DBA)
    Sleep(100)

    def lambda_DDA():
        OP_8F(0xFE, 0x514, 0x0, 0x1135A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_DDA)
    Jump("loc_EC7")

    label("loc_DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5E")

    def lambda_E06():
        OP_8F(0xFE, 0x442, 0x0, 0x11A3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_E06)
    Sleep(100)

    def lambda_E26():
        OP_8F(0xFE, 0xFFFFFC2C, 0x0, 0x11350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_E26)
    Sleep(100)

    def lambda_E46():
        OP_8F(0xFE, 0x514, 0x0, 0x1135A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_E46)
    Jump("loc_EC7")

    label("loc_E5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC7")

    def lambda_E72():
        OP_8F(0xFE, 0x442, 0x0, 0x11A3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_E72)
    Sleep(100)

    def lambda_E92():
        OP_8F(0xFE, 0xFFFFFC2C, 0x0, 0x11350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_E92)
    Sleep(100)

    def lambda_EB2():
        OP_8F(0xFE, 0x514, 0x0, 0x1135A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_EB2)

    label("loc_EC7")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #15
        0x10,
        (
            "#163F#5P真是的……\x01",
            "这到底是怎么回事！\x02\x03",

            "#166F那家伙是叫『影之王』吗……\x01",
            "把我带到这样的地方来，\x01",
            "真是莫大的耻辱……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #16
        0x10,
        (
            "#162F#5P#3S哼！\x01",
            "真是气死了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD0")
    OP_62(0xEE, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1037")

    label("loc_FD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF8")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1037")

    label("loc_FF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1020")
    OP_62(0xEE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1037")

    label("loc_1020")

    OP_62(0xEE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1037")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105F")
    OP_62(0xEF, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10C6")

    label("loc_105F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1087")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10C6")

    label("loc_1087")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AF")
    OP_62(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10C6")

    label("loc_10AF")

    OP_62(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_10C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EE")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1155")

    label("loc_10EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1116")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1155")

    label("loc_1116")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113E")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1155")

    label("loc_113E")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1155")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117D")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_11E4")

    label("loc_117D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A5")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_11E4")

    label("loc_11A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CD")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_11E4")

    label("loc_11CD")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_11E4")

    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121F")

    ChrTalk(    #17
        0x105,
        "#1163F#12P摩尔根将军……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12AE")

    label("loc_121F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1254")

    ChrTalk(    #18
        0x10E,
        "#178F#12P摩尔根将军……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12AE")

    label("loc_1254")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128A")

    ChrTalk(    #19
        0x102,
        "#1502F#12P摩尔根将军……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12AE")

    label("loc_128A")


    ChrTalk(    #20
        0x10C,
        "#112F#12P摩尔根将军……\x02",
    )

    CloseMessageWindow()

    label("loc_12AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E8")

    ChrTalk(    #21
        0x101,
        "#1007F#12P啊，一点也没变啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_138E")

    label("loc_12E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1323")

    ChrTalk(    #22
        0x106,
        "#556F#12P哈哈，一点也没有变。\x02",
    )

    CloseMessageWindow()
    Jump("loc_138E")

    label("loc_1323")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_135F")

    ChrTalk(    #23
        0x103,
        "#1534F#12P呵呵，一点也没有变。\x02",
    )

    CloseMessageWindow()
    Jump("loc_138E")

    label("loc_135F")


    ChrTalk(    #24
        0x109,
        (
            "#1066F#6P哈哈……\x01",
            "还和以前一样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CF")

    ChrTalk(    #25
        0x104,
        (
            "#1545F#12P呼……\x01",
            "好厉害的一声吼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140A")

    label("loc_13CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140A")

    ChrTalk(    #26
        0x108,
        (
            "#573F#12P哈哈……\x01",
            "好大的声音啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144B")

    ChrTalk(    #27
        0x110,
        (
            "#264F#12P哇，真是个\x01",
            "大嗓门的老爷爷啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_148A")

    ChrTalk(    #28
        0x10B,
        (
            "#216F#12P真、真是个\x01",
            "烦躁的老头子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14BC")

    ChrTalk(    #29
        0x107,
        "#067F#12P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_14BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1501")

    ChrTalk(    #30
        0x10A,
        (
            "#819F#12P不、不愧是\x01",
            "哈肯大门的魔鬼将军……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1501")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1538")

    ChrTalk(    #31
        0x10F,
        "#1803F#12P（好大的声音……）\x02",
    )

    CloseMessageWindow()

    label("loc_1538")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1586")

    ChrTalk(    #32
        0x10D,
        (
            "#270F#4P（摩尔根将军……\x01",
            "  是利贝尔头等的宿将吗。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1586")


    ChrTalk(    #33
        0x10,
        (
            "#163F#5P算啦……\x01",
            "即便是怒吼也不该这样吧。\x02\x03",

            "#160F……说起来，\x01",
            "你们也真是不走运啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B8")
    Sleep(500)

    ChrTalk(    #34
        0x10,
        (
            "#163F#5P阿加特·科洛斯纳……\x01",
            "还有拉赛尔博士的孙女。\x02\x03",

            "#165F没想到会在这种地方\x01",
            "和你们见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        (
            "#560F#12P那个那个……\x01",
            "好、好久不见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171F")

    label("loc_16B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_171F")
    Sleep(500)

    ChrTalk(    #36
        0x10,
        (
            "#163F#5P阿加特·科洛斯纳……\x02\x03",

            "#165F没想到会在这种地方\x01",
            "和你见面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171F")


    ChrTalk(    #37
        0x106,
        (
            "#051F#12P哼……\x01",
            "我也听说过你的英勇事迹。\x02\x03",

            "『利贝尔的武神』……\x01",
            "你曾经被这样称呼对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "#165F#5P呼……都是过去的事了。\x02",
    )

    CloseMessageWindow()

    label("loc_17B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AF0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18B8")
    Sleep(500)

    ChrTalk(    #39
        0x10,
        (
            "#163F#5P艾丝蒂尔·布莱特……\x01",
            "还有约修亚·布莱特。\x02\x03",

            "#165F听说你们去修行了，\x01",
            "身体还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1016F#12P哈哈……\x01",
            "嗯，托您的福。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#1514F#12P将军阁下，\x01",
            "您也是老样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_18B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1982")
    Sleep(500)

    ChrTalk(    #42
        0x10,
        (
            "#163F#5P艾丝蒂尔·布莱特……\x02\x03",

            "#165F听说你们去修行了，\x01",
            "身体还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1016F#12P哈哈……\x01",
            "嗯，托您的福。\x02\x03",

            "#1006F将军您才是，\x01",
            "健康比什么都重要啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_1982")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A38")
    Sleep(500)

    ChrTalk(    #44
        0x10,
        (
            "#163F#5P约修亚·布莱特……\x02\x03",

            "#165F听说你们去修行了，\x01",
            "身体还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1513F#12P是，托您的福。\x02\x03",

            "#1500F将军阁下，\x01",
            "您也是老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A38")


    ChrTalk(    #46
        0x10,
        (
            "#163F#5P唉，我已经老了。\x02\x03",

            "#165F还是想尽早把工作\x01",
            "都留给你们父亲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ABD")

    ChrTalk(    #47
        0x101,
        "#1008F#12P啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_1ABD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF0")

    ChrTalk(    #48
        0x102,
        "#1513F#12P……您辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_1AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DC2")
    Sleep(500)

    ChrTalk(    #49
        0x10,
        (
            "#163F#5P可是，真没想到连公主殿下\x01",
            "也卷入了这件事……\x02\x03",

            "#166F唉，真是可恨啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C4D")

    ChrTalk(    #50
        0x10E,
        (
            "#179F#12P将军阁下……\x01",
            "请您不必担心。\x02\x03",

            "#170F我尤莉亚就算牺牲掉生命\x01",
            "也会保卫殿下的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x105,
        "#1382F#12P……尤莉亚小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#165F#5P是吗……\x01",
            "这样的话我就可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC2")

    label("loc_1C4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFA")

    ChrTalk(    #53
        0x10E,
        (
            "#179F#12P将军阁下……\x01",
            "请您不必担心。\x02\x03",

            "#170F我尤莉亚就算牺牲掉生命\x01",
            "也会保卫殿下的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#165F#5P是吗……\x01",
            "这样的话我就可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC2")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC2")

    ChrTalk(    #55
        0x105,
        (
            "#1383F#12P摩尔根将军……\x01",
            "请您不必担心。\x02\x03",

            "#1382F还有尤莉亚在。\x01",
            "我们一定能够平安回去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        (
            "#161F#5P公主殿下……\x02\x03",

            "#165F明白了。\x01",
            "我相信女神会保佑你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC2")

    Sleep(500)

    ChrTalk(    #57
        0x10,
        (
            "#163F#5P……理查德。\x02\x03",

            "我也有很多话\x01",
            "想对你说……\x02\x03",

            "#165F不过反正\x01",
            "另一个人也会替我说的，\x01",
            "这次就算了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10C,
        "#115F#12P……不敢当。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#163F#5P好了……时间宝贵。\x02\x03",

            "#160F聊天就暂且告一段落，\x01",
            "我们赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_1ED2():
        OP_6D(1800, 0, 76920, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1ED2)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3D")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FA4")

    label("loc_1F3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F65")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FA4")

    label("loc_1F65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FA4")

    label("loc_1F8D")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1FA4")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD1")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2038")

    label("loc_1FD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2038")

    label("loc_1FF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2021")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2038")

    label("loc_2021")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2038")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2065")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20CC")

    label("loc_2065")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_208D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20CC")

    label("loc_208D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B5")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20CC")

    label("loc_20B5")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_20CC")

    Sleep(1000)

    ChrTalk(    #60
        0x109,
        (
            "#1063F#6P战、战戟！？\x01",
            "这可真是有年头的武器了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10C,
        (
            "#114F#12P别小看它！\x01",
            "那正是『武神』最擅长的家伙……\x02\x03",

            "是军队没有机械化以前，\x01",
            "粉碎了众多敌兵的大斧枪！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10, 4)

    def lambda_219A():

        label("loc_219A")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_219A")

    QueueWorkItem2(0x10, 3, lambda_219A)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -1790, 100, 79330, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 2990, 100, 79080, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_2256():
        OP_6D(1610, 0, 76300, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2256)

    def lambda_226E():
        OP_67(0, 5960, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_226E)

    def lambda_2286():
        OP_6B(2360, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2286)

    def lambda_2296():
        OP_6E(373, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2296)

    def lambda_22A6():
        OP_6C(32000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_22A6)
    Sleep(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -1790, -3000, 79330, 180)
    SetChrPos(0x12, 2990, -3000, 79080, 180)
    OP_22(0x85, 0x1, 0x64)

    def lambda_22EC():

        label("loc_22EC")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_22EC")

    QueueWorkItem2(0x109, 3, lambda_22EC)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x12, 0x0, 0x0, 0xA)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 11)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 13)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 15)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 17)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_23(0x85)
    OP_82(0x0, 0x2)
    OP_44(0x10, 0x3)
    OP_44(0x109, 0x3)
    OP_1D(0xC4)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #62
        0x10,
        (
            "#165F#5P呵呵，上次拿起这东西\x01",
            "还是在前年的武术大会上……\x02\x03",

            "#163F对付我这样的老兵\x01",
            "如果还嫌吃力的话，\x01",
            "那前面的道路就可想而知了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #63
        0x10,
        "#162F#5P#4S你们就做好受死的准备放马过来吧！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_248B():
        OP_6D(1130, 0, 75700, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_248B)

    def lambda_24A3():
        OP_67(0, 6370, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_24A3)

    def lambda_24BB():
        OP_6B(2050, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_24BB)

    def lambda_24CB():
        OP_6E(300, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_24CB)
    SetChrChipByIndex(0x10, 2)

    def lambda_24E0():
        OP_8F(0xFE, 0x258, 0x0, 0x11DA0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_24E0)
    Sleep(10)
    SetChrChipByIndex(0x11, 6)

    def lambda_2505():
        OP_8F(0xFE, 0xFFFFFD9E, 0x0, 0x12066, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2505)
    Sleep(10)
    SetChrChipByIndex(0x12, 8)

    def lambda_252A():
        OP_8F(0xFE, 0x67C, 0x0, 0x120AC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_252A)

    def lambda_2545():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2545)

    def lambda_2560():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2560)

    def lambda_257B():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_257B)

    def lambda_2596():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2596)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A9, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_8_90C end

    def Function_9_25CD(): pass

    label("Function_9_25CD")

    PlayEffect(0x1, 0x3, 0xFF, -1790, 100, 79330, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x3, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_25CD end

    def Function_10_2622(): pass

    label("Function_10_2622")

    PlayEffect(0x1, 0x4, 0xFF, 2990, 100, 79080, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_2622 end

    def Function_11_2677(): pass

    label("Function_11_2677")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 610, 0, 78790, 180)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0xC)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 50, 500, 100, 0, 0, 0, 2300, 2500, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -150, 0, 74920, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2793")
    SetChrPos(0xEF, 1300, 0, 74940, 0)
    SetChrPos(0xF0, -600, 0, 73160, 0)
    SetChrPos(0xF1, 1010, 0, 73260, 0)
    Jump("loc_2818")

    label("loc_2793")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D7")
    SetChrPos(0xF0, 1300, 0, 74940, 0)
    SetChrPos(0xEF, -600, 0, 73160, 0)
    SetChrPos(0xF1, 1010, 0, 73260, 0)
    Jump("loc_2818")

    label("loc_27D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2818")
    SetChrPos(0xF1, 1300, 0, 74940, 0)
    SetChrPos(0xEF, -600, 0, 73160, 0)
    SetChrPos(0xF0, 1010, 0, 73260, 0)

    label("loc_2818")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(2100, 0, 77960, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #64
        0x10,
        (
            "#163F#5P呵呵……\x01",
            "我稍微有些放心了……\x02\x03",

            "#165F这样的话，\x01",
            "或许会有万分之一的可能……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10C,
        (
            "#112F#12P也就是说……\x01",
            "在最后等着的果然是……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#163F#5P嗯……\x01",
            "就是你们想象中的人物。\x02\x03",

            "#160F但是，那家伙也是人。\x01",
            "你们一定能看到光明的……\x02\x03",

            "以乾坤一掷的觉悟挑战就好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10C,
        "#119F#12P……知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        (
            "#163F#5P呵呵，真遗憾啊……\x02\x03",

            "如果有能打败那家伙的人，\x01",
            "我还真想亲眼看看呢……\x02\x03",

            "#165F如果有机会再见面的话，\x01",
            "一定要告诉我结果……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -850, 0, 0, 0, 0, 1900, 1900, 1900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_2AD3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2AD3)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    Sleep(1000)

    ChrTalk(    #69
        0x10C,
        "#116F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1067F#6P怎么办……\x01",
            "遇到天大的麻烦事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10C,
        (
            "#115F#11P是啊……\x02\x03",

            "#110F不过这个……\x01",
            "从某种意义上来说也是必然了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2BBA():
        OP_6D(2240, 0, 76000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2BBA)

    def lambda_2BD2():
        OP_67(0, 5160, -10000, 1200)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_2BD2)

    def lambda_2BEA():
        OP_6B(2440, 1200)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_2BEA)

    def lambda_2BFA():
        OP_6E(322, 1200)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_2BFA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C42")

    def lambda_2C18():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2C18)
    Sleep(100)

    def lambda_2C2B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C2B)
    Sleep(100)
    OP_8C(0xF0, 45, 400)
    Jump("loc_2CBB")

    label("loc_2C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C80")

    def lambda_2C56():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2C56)
    Sleep(100)

    def lambda_2C69():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C69)
    Sleep(100)
    OP_8C(0xEF, 45, 400)
    Jump("loc_2CBB")

    label("loc_2C80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CBB")

    def lambda_2C94():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2C94)
    Sleep(100)

    def lambda_2CA7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2CA7)
    Sleep(100)
    OP_8C(0xEF, 45, 400)

    label("loc_2CBB")

    WaitChrThread(0xEE, 0x3)
    Sleep(400)

    ChrTalk(    #72
        0x10C,
        (
            "#115F#5P虽然这么说可能有些自私，\x01",
            "不过请你们务必要协助我。\x02\x03",

            "#112F为了真正意义上的前进……\x01",
            "要亲手切断对过往的留恋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x109,
        "#1840F#6P理查德先生……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DE4")

    ChrTalk(    #74
        0x101,
        (
            "#1012F#6P嗯……当然！\x02\x03",

            "#1006F我也是，\x01",
            "想试试看现在的自己\x01",
            "对那个人究竟有多少胜算！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_2DE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E5C")

    ChrTalk(    #75
        0x102,
        (
            "#1513F#6P……我知道了。\x02\x03",

            "#1501F被照顾了六年……\x01",
            "我也想让他看看\x01",
            "我到底成长了多少呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_2E5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EF2")

    ChrTalk(    #76
        0x103,
        (
            "#1521F#6P呵呵，知道了。\x02\x03",

            "#1536F虽然有些害怕和老师交手……\x01",
            "但是我作为他的游击士大弟子，\x01",
            "也想展示一下自己的进步呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_2EF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F68")

    ChrTalk(    #77
        0x106,
        (
            "#053F#6P哼……正合我意。\x02\x03",

            "#051F我也想试试\x01",
            "现在的自己能够在\x01",
            "那个大叔面前如何表现。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_2F68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FDA")

    ChrTalk(    #78
        0x108,
        (
            "#573F#6P啊，正合我意。\x02\x03",

            "#070F我也想试试\x01",
            "泰斗流拳法对那位大人\x01",
            "能起到多大效果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_2FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3064")

    ChrTalk(    #79
        0x10E,
        (
            "#179F#6P……正合我意。\x02\x03",

            "#170F在士官学校里学到的基础……\x01",
            "现在能够施展到何种地步，\x01",
            "正想让他见识一下呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_3064")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30EB")

    ChrTalk(    #80
        0x10A,
        (
            "#1316F#6P老、老实说，\x01",
            "我没有多少自信……\x02\x03",

            "#816F但作为同一流派的成员，\x01",
            "我也想展示一下我最强的力量！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_30EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3162")

    ChrTalk(    #81
        0x10D,
        (
            "#278F#6P……正合我意。\x02\x03",

            "#275F如雷贯耳的传说中的剑士。\x01",
            "无论如何请让我和他比试一次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_3162")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31DF")

    ChrTalk(    #82
        0x110,
        (
            "#263F#6P嘻嘻……\x01",
            "是教授最提防的\x01",
            "那位传说中的英雄吗。\x02\x03",

            "#1306F到底是什么样的人，很期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_31DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3263")

    ChrTalk(    #83
        0x105,
        (
            "#1383F#6P救国的英雄、\x01",
            "利贝尔的最高守护者……\x02\x03",

            "#1382F虽然不知道顶不顶用，\x01",
            "但是请允许我全力挑战。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_3263")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32F9")

    ChrTalk(    #84
        0x104,
        (
            "#1545F#6P呵呵，击退了黄金军马的\x01",
            "最强的剑士、稀世的战略家……\x02\x03",

            "#1540F作为今后的经验参考，\x01",
            "请一定让我和他交一交手。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_32F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3398")

    ChrTalk(    #85
        0x10F,
        (
            "#1446F#6P『剑圣』的英名……\x01",
            "我在星杯骑士团也听说过。\x02\x03",

            "#1448F虽然不知道我的法剑\x01",
            "到底能够做到何种地步……\x01",
            "但我会全力挑战的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3411")

    label("loc_3398")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3411")

    ChrTalk(    #86
        0x10B,
        (
            "#413F#6P听、听起来好像是个\x01",
            "强得无法无天的大叔啊……\x02\x03",

            "#210F不过，\x01",
            "反正我也会全力以赴的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3411")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3495")

    ChrTalk(    #87
        0x107,
        (
            "#563F#6P我、我能起多大作用，\x01",
            "实在是心里没数……\x02\x03",

            "#560F不过作为诸位姐姐的妹妹，\x01",
            "我一定会加油的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_3495")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3511")

    ChrTalk(    #88
        0x10B,
        (
            "#413F#6P听、听起来好像是个\x01",
            "强得无法无天的大叔啊……\x02\x03",

            "#210F不过，\x01",
            "反正我也会全力以赴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_3511")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35B0")

    ChrTalk(    #89
        0x10F,
        (
            "#1446F#6P『剑圣』的英名……\x01",
            "我在星杯骑士团也听说过。\x02\x03",

            "#1448F虽然不知道我的法剑\x01",
            "到底能够做到何种地步……\x01",
            "但我会全力挑战的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_35B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3646")

    ChrTalk(    #90
        0x104,
        (
            "#1545F#6P呵呵，击退了黄金军马的\x01",
            "最强的剑士、稀世的战略家……\x02\x03",

            "#1540F作为今后的经验参考，\x01",
            "请一定让我和他交一交手。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_3646")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36CA")

    ChrTalk(    #91
        0x105,
        (
            "#1383F#6P救国的英雄、\x01",
            "利贝尔的最高守护者……\x02\x03",

            "#1382F虽然不知道顶不顶用，\x01",
            "但是请允许我全力挑战。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_36CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3741")

    ChrTalk(    #92
        0x110,
        (
            "#260F#6P嘻嘻……\x01",
            "是教授最提防的\x01",
            "那位传说中的英雄吗。\x02\x03",

            "到底是什么样的人，很期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_3741")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37B3")

    ChrTalk(    #93
        0x10D,
        (
            "#270F#6P……正合我意。\x02\x03",

            "如雷贯耳的传说中的剑士，\x01",
            "无论如何请让我和他比试一把。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_37B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_383A")

    ChrTalk(    #94
        0x10A,
        (
            "#1316F#6P老、老实说，\x01",
            "我没有多少自信……\x02\x03",

            "#816F但作为同一流派的成员，\x01",
            "我也想展示一下我最强的力量！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_383A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38C2")

    ChrTalk(    #95
        0x10E,
        (
            "#179F#6P……我也是。\x02\x03",

            "#170F在士官学校里学到的基础……\x01",
            "现在能够施展到何种地步，\x01",
            "正想让他见识一下呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_38C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_393F")

    ChrTalk(    #96
        0x108,
        (
            "#573F#6P我也是。\x02\x03",

            "#070F泰斗流拳法……对『理』之达人\x01",
            "到底能起到多少效果，就让我试一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_393F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39B4")

    ChrTalk(    #97
        0x106,
        (
            "#053F#6P哼，我也是。\x02\x03",

            "#051F那个飘飘然的小胡子……\x01",
            "我一定让他吃惊到眼珠都瞪出来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_39B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A2D")

    ChrTalk(    #98
        0x103,
        (
            "#1521F#6P呵呵，我也是哦。\x02\x03",

            "#1536F作为他的游击士大弟子，\x01",
            "我也想展示一下自己的进步呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA0")

    label("loc_3A2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AA0")

    ChrTalk(    #99
        0x102,
        (
            "#1513F#6P……我也是。\x02\x03",

            "#1501F被照顾了六年……\x01",
            "我也想让他看看\x01",
            "我到底成长了多少呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA0")


    ChrTalk(    #100
        0x10C,
        (
            "#111F#5P……谢谢。\x02\x03",

            "#119F堵在我们前方的是最强的敌人。\x01",
            "雕虫小技对他是行不通的。\x02\x03",

            "#110F就像将军指示的那样，\x01",
            "以乾坤一掷的觉悟\x01",
            "迎接命运的挑战吧……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        "#1078F#6P明白了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B1F)
    OP_28(0x39, 0x1, 0x80)
    OP_28(0x39, 0x1, 0x100)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_11_2677 end

    def Function_12_3B81(): pass

    label("Function_12_3B81")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA2")
    Sleep(100)
    Jump("loc_3C1D")

    label("loc_3BA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB7")
    Sleep(200)
    Jump("loc_3C1D")

    label("loc_3BB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BCC")
    Sleep(300)
    Jump("loc_3C1D")

    label("loc_3BCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE1")
    Sleep(400)
    Jump("loc_3C1D")

    label("loc_3BE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF6")
    Sleep(500)
    Jump("loc_3C1D")

    label("loc_3BF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C0B")
    Sleep(600)
    Jump("loc_3C1D")

    label("loc_3C0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C1D")
    Sleep(700)

    label("loc_3C1D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C3F")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_3C1D")

    label("loc_3C3F")

    Return()

    # Function_12_3B81 end

    def Function_13_3C40(): pass

    label("Function_13_3C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0F")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(6656)
    Sleep(500)
    Jump("loc_3D12")

    label("loc_3D0F")

    TalkBegin(0xFF)

    label("loc_3D12")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #102
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3D3C")

    label("loc_3D3C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EA7")

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

    Jump("loc_3DA1")

    label("loc_3DA1")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3DBE"),
        (1, "loc_3E39"),
        (2, "loc_3E68"),
        (SWITCH_DEFAULT, "loc_3E97"),
    )


    label("loc_3DBE")

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
    OP_1D(0xE8)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EA4")

    label("loc_3E39")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #103
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3E65")

    label("loc_3E65")

    Jump("loc_3EA4")

    label("loc_3E68")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #104
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3E94")

    label("loc_3E94")

    Jump("loc_3EA4")

    label("loc_3E97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EA4")

    label("loc_3EA4")

    Jump("loc_3D4F")

    label("loc_3EA7")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED4")
    OP_A2(0x25A8)
    EventEnd(0x1)
    Jump("loc_3ED7")

    label("loc_3ED4")

    TalkEnd(0xFF)

    label("loc_3ED7")

    Return()

    # Function_13_3C40 end

    SaveToFile()

Try(main)
