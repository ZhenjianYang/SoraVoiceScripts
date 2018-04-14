from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T2300   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2300.x',
        MapIndex            = 86,
        MapDefaultBGM       = "ed60015",
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
        '萨蒂',                                 # 9
        '卢西亚',                               # 10
        '塞尔吉村长',                           # 11
        '玛诺利亚间道方向',                     # 12
        '梅威海道方向',                         # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01150 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01150P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 0,
        Y                   = 23500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 4000,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 38210,
        Z                   = -50,
        Y                   = 17840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 7990,
        Y                   = 68620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 75410,
        Z                   = -40,
        Y                   = 20810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 16870,
        Y                   = 7000,
        Z                   = -7690,
        Range               = -9400,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFFD80,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 27540,
        Y                   = 0,
        Z                   = 18980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 53410,
        Y                   = 0,
        Z                   = 22710,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4000,
        Z                   = 20210,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = 4450,
        TriggerZ            = 6500,
        TriggerY            = -2640,
        TriggerRange        = 800,
        ActorX              = 4450,
        ActorZ              = 7500,
        ActorY              = -2740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 37440,
        TriggerZ            = -10,
        TriggerY            = 19280,
        TriggerRange        = 800,
        ActorX              = 37440,
        ActorZ              = 1500,
        ActorY              = 18980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38140,
        TriggerZ            = -40,
        TriggerY            = 10680,
        TriggerRange        = 1000,
        ActorX              = 38310,
        ActorZ              = -1540,
        ActorY              = 7000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_2C2",          # 01, 1
        "Function_2_32C",          # 02, 2
        "Function_3_5C9",          # 03, 3
        "Function_4_9DE",          # 04, 4
        "Function_5_D34",          # 05, 5
        "Function_6_1053",         # 06, 6
        "Function_7_10A5",         # 07, 7
        "Function_8_14FB",         # 08, 8
        "Function_9_1A53",         # 09, 9
        "Function_10_1CB7",        # 0A, 10
        "Function_11_1D50",        # 0B, 11
        "Function_12_1DCA",        # 0C, 12
        "Function_13_1EB5",        # 0D, 13
        "Function_14_1EB9",        # 0E, 14
        "Function_15_1EBD",        # 0F, 15
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_269")
    SetChrPos(0x9, 15050, 3980, 22520, 161)
    Jump("loc_298")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_273")
    Jump("loc_298")

    label("loc_273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_27D")
    Jump("loc_298")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_287")
    Jump("loc_298")

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_298")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_298")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2C1"),
    )


    label("loc_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_2BE")

    Jump("loc_2C1")

    label("loc_2C1")

    Return()

    # Function_0_24E end

    def Function_1_2C2(): pass

    label("Function_1_2C2")

    OP_16(0x2, 0xFA0, 0xFFFE5A20, 0xFFFE13D0, 0x23004B)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_2E9")
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_304")
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x1)
    OP_71(0x7, 0x4)
    OP_64(0x1, 0x1)

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_321")
    OP_72(0x2, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x2, 0x10)
    OP_64(0x0, 0x1)
    Jump("loc_32B")

    label("loc_321")

    OP_71(0x2, 0x4)
    OP_72(0x8, 0x10)

    label("loc_32B")

    Return()

    # Function_1_2C2 end

    def Function_2_32C(): pass

    label("Function_2_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_359")

    label("loc_333")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_356")
    OP_8D(0xFE, 16309, 21410, 13470, 24720, 3000)
    Jump("loc_333")

    label("loc_356")

    Jump("loc_5C8")

    label("loc_359")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C")
    Return()

    label("loc_36C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    SetChrPos(0xFE, 45290, -10, 21290, 0)
    OP_8E(0xFE, 0x9A24, 0xFFFFFF88, 0x3E76, 0xDAC, 0x0)
    OP_8E(0xFE, 0x1428, 0xFA0, 0x3B42, 0xDAC, 0x0)
    Jump("loc_424")

    label("loc_3B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    SetChrPos(0xFE, 5130, 4030, 10940, 0)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0xBD6, 0xFBE, 0x32DC, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_424")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C8")
    OP_8E(0xFE, 0x1428, 0xFA0, 0x3B42, 0xDAC, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x1B80, 0xFBE, 0x323C, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x140A, 0xFBE, 0x2ABC, 0xDAC, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0xBD6, 0xFBE, 0x32DC, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C5")
    OP_8E(0xFE, 0x9A24, 0xFFFFFF88, 0x3E76, 0xDAC, 0x0)
    OP_8E(0xFE, 0xB0EA, 0xFFFFFFF6, 0x532A, 0xDAC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E")
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_54E")

    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 180, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59B")
    OP_62(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)

    label("loc_59B")

    Sleep(1500)
    OP_8C(0xFE, 250, 400)
    OP_8E(0xFE, 0x9A24, 0xFFFFFF88, 0x3E76, 0xDAC, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C5")

    Jump("loc_424")

    label("loc_5C8")

    Return()

    # Function_2_32C end

    def Function_3_5C9(): pass

    label("Function_3_5C9")

    OP_A2(0x2)
    TalkBegin(0x8)
    OP_63(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2")
    OP_0D()
    OP_A9(0x71)
    OP_56(0x0)
    TalkEnd(0x8)
    OP_A3(0x2)
    Return()

    label("loc_5F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_606")
    TalkEnd(0x8)
    OP_A3(0x2)
    Return()

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_686")

    ChrTalk(    #0
        0x8,
        (
            "导力器不能使用\x01",
            "我们也很为难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "不过家里的婆婆\x01",
            "却完全不介意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "老人的智慧和经验\x01",
            "真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6CF")

    label("loc_686")


    ChrTalk(    #3
        0x8,
        (
            "婆婆即使没有导力器\x01",
            "也完全没事的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "简直比龟甲还……结实呢。\x02",
    )

    CloseMessageWindow()

    label("loc_6CF")

    Jump("loc_9D7")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_72C")

    ChrTalk(    #5
        0x8,
        (
            "附近的海岸好像有军队的警备艇\x01",
            "被迫降落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "好像还有伤员\x01",
            "在旅店休息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D7")

    label("loc_72C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_7CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_783")

    ChrTalk(    #7
        0x8,
        (
            "上次的时候\x01",
            "还是个孩子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "这次的选举对我来说\x01",
            "是第一次经历。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8")

    label("loc_783")

    OP_A2(0x0)

    ChrTalk(    #9
        0x8,
        (
            "我在这次选举中\x01",
            "是第一次投票哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "打算好好看人品\x01",
            "来投票。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C8")

    Jump("loc_9D7")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_81A")

    ChrTalk(    #11
        0x8,
        (
            "欢迎光临，\x01",
            "要买花吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "不仅有欣赏用的,\x01",
            "还有能做料理的花哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D7")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_8E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_871")

    ChrTalk(    #13
        0x8,
        (
            "孩子们好像也完全\x01",
            "恢复了精神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "果然空之女神\x01",
            "在守护着我们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E5")

    label("loc_871")

    OP_A2(0x0)

    ChrTalk(    #15
        0x8,
        (
            "孩子们好像也完全\x01",
            "恢复了精神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "纵火事件的时候\x01",
            "还以为会变成怎样呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "果然空之女神\x01",
            "在守护着我们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E5")

    Jump("loc_9D7")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_98D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_93D")

    ChrTalk(    #18
        0x8,
        (
            "太阳已经\x01",
            "升得这么高了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "差不多到\x01",
            "主日学校结束的时间了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A")

    label("loc_93D")

    OP_A2(0x0)

    ChrTalk(    #20
        0x8,
        (
            "哎呀，太阳已经\x01",
            "升得这么高了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "差不多到\x01",
            "主日学校结束的时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98A")

    Jump("loc_9D7")

    label("loc_98D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_9D7")

    ChrTalk(    #22
        0x8,
        (
            "一个打扮奇怪的\x01",
            "神父刚才经过这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "那就是新的巡回神父吗。\x02",
    )

    CloseMessageWindow()

    label("loc_9D7")

    OP_A3(0x2)
    TalkEnd(0x8)
    Return()

    # Function_3_5C9 end

    def Function_4_9DE(): pass

    label("Function_4_9DE")

    TalkBegin(0xFE)
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4E")

    ChrTalk(    #24
        0xFE,
        (
            "好想去找\x01",
            "孤儿院的大家玩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "妈妈又说\x01",
            "不行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "说有很多\x01",
            "可怕～的魔兽。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_A8C")

    label("loc_A4E")


    ChrTalk(    #27
        0xFE,
        (
            "妈妈说，不能\x01",
            "出去村子外面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "说有很多\x01",
            "可怕～的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8C")

    Jump("loc_D30")

    label("loc_A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFF")

    ChrTalk(    #29
        0xFE,
        (
            "卢西亚\x01",
            "也不是来去玩的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "是妈妈要我\x01",
            "来找柴火的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "嗯～有没有好的树枝\x01",
            "落下呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_B32")

    label("loc_AFF")


    ChrTalk(    #32
        0xFE,
        (
            "是妈妈要我\x01",
            "来找柴火哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "嘿嘿，了不起吧？\x02",
    )

    CloseMessageWindow()

    label("loc_B32")

    Jump("loc_D30")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_B8B")

    ChrTalk(    #34
        0xFE,
        (
            "嘿嘿，赶快\x01",
            "到上学的日子就好了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "可以和波利他们\x01",
            "在外面尽情的玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D30")

    label("loc_B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_C19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BC3")

    ChrTalk(    #36
        0xFE,
        (
            "嗯～不过，叔叔他\x01",
            "为什么不回家呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C16")

    label("loc_BC3")

    OP_A2(0x1)

    ChrTalk(    #37
        0xFE,
        (
            "我们家是住宿酒馆，\x01",
            "有很多喝醉的客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "叔叔他，\x01",
            "好像碰到很痛苦的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C16")

    Jump("loc_D30")

    label("loc_C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_D30")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEA")
    TurnDirection(0xFE, 0x109, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C6D")

    ChrTalk(    #39
        0xFE,
        (
            "老师，下次来的时候\x01",
            "也要再读书给我们听哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE7")

    label("loc_C6D")

    OP_A2(0x1)

    ChrTalk(    #40
        0xFE,
        "啊～是凯文老师～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "老师，再读书给我们听哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1062F哦，交给我吧。\x02\x03",

            "卢西亚\x01",
            "也要乖乖的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "嗯，等你哦～\x02",
    )

    CloseMessageWindow()

    label("loc_CE7")

    Jump("loc_D30")

    label("loc_CEA")


    ChrTalk(    #44
        0xFE,
        "今天的老师是个很快乐的人呢⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "嘿嘿，下次的主日学校也好期待。\x02",
    )

    CloseMessageWindow()

    label("loc_D30")

    TalkEnd(0xFE)
    Return()

    # Function_4_9DE end

    def Function_5_D34(): pass

    label("Function_5_D34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_E26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DB0")

    ChrTalk(    #46
        0xFE,
        (
            "身为贵族的前市长被逮捕，\x01",
            "平民出身的候选人在竞争其继任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "此次的市长选举\x01",
            "真像是时代变化的象征。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E23")

    label("loc_DB0")

    OP_A2(0x3)

    ChrTalk(    #48
        0xFE,
        (
            "诺曼氏和波尔多斯氏\x01",
            "都是平民出身，\x01",
            "两人都是出色的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "以前的选举\x01",
            "都是从贵族中选出的，\x01",
            "时代真是变了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E23")

    Jump("loc_104F")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E81")

    ChrTalk(    #50
        0xFE,
        (
            "上次选举时\x01",
            "这里是投票所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "许多人相信戴尔蒙家\x01",
            "的家名而投了票……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF2")

    label("loc_E81")

    OP_A2(0x3)

    ChrTalk(    #52
        0xFE,
        (
            "上次选举时\x01",
            "这里曾经是投票所……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "……唔，怎么看都很狭窄啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "大概还是只有拜托\x01",
            "白之木莲亭合作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    Jump("loc_104F")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_F60")

    ChrTalk(    #55
        0xFE,
        (
            "孤儿院开始重建工程时，\x01",
            "村里的年轻人好像\x01",
            "也都去帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "真希望他们能一直\x01",
            "保持这种心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104F")

    label("loc_F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_104F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FC5")

    ChrTalk(    #57
        0xFE,
        (
            "前市长引起的事件\x01",
            "对玛诺利亚来说也是重伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "发生大事件之后\x01",
            "游客也都不来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104F")

    label("loc_FC5")

    OP_A2(0x3)

    ChrTalk(    #59
        0xFE,
        (
            "哎呀，旅行的人吗？\x01",
            "欢迎来到玛诺利亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "烧掉的孤儿院也被重建，\x01",
            "一切恢复到平常的生活了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "之后就等待\x01",
            "下任的市长被选出来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104F")

    TalkEnd(0xFE)
    Return()

    # Function_5_D34 end

    def Function_6_1053(): pass

    label("Function_6_1053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_1064")
    TalkEnd(0xFF)
    Call(0, 9)
    Jump("loc_10A4")

    label("loc_1064")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #62
        "\x07\x05主日学校·授课中\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_10A4")

    Return()

    # Function_6_1053 end

    def Function_7_10A5(): pass

    label("Function_7_10A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B6")
    Call(0, 10)

    label("loc_10B6")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 64319, 0, 21000, 270)
    SetChrPos(0xF7, 64170, 0, 19800, 270)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6C(45000, 0)
    OP_C8(0x200, 0x46, "C_PLAC06._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_123B")

    ChrTalk(    #63
        0x106,
        (
            "#050F玛诺利亚啊……\x01",
            "捐款被抢事件以来都没来过啊。\x02\x03",

            "还是那么悠闲的村子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #64
        0x101,
        (
            "#1006F#5P这不是很好吗。\x02\x03",

            "阿加特的故乡拉文努村\x01",
            "也很悠闲，多好啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #65
        0x106,
        (
            "#552F哼，是吗。\x02\x03",

            "#053F总之，主日学校\x01",
            "好像在村里进行呢。\x02\x03",

            "去确认一下情况吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DC")

    label("loc_123B")


    ChrTalk(    #66
        0x103,
        (
            "#021F玛诺利亚村啊。\x01",
            "好久没来了呢。\x02\x03",

            "#020F不过说实话\x01",
            "包括卢安我也很少来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #67
        0x101,
        (
            "#1004F#5P哦，这样啊。\x02\x03",

            "我还以为老爸和雪拉姐\x01",
            "都是在洛连特以外的地方\x01",
            "到处跑的呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #68
        0x103,
        (
            "#020F我的行动范围\x01",
            "还是以洛连特周边为主。\x02\x03",

            "柏斯和王都也都会常去。\x02\x03",

            "不特定所属支部的\x01",
            "也就是阿加特吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1011F#5P这么一说确实是，\x01",
            "阿加特很有流浪者的感觉呢。\x02\x03",

            "#1015F不过，我好像不记得\x01",
            "有在洛连特见过阿加特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#027F洛连特因为有卡西乌斯老师在\x01",
            "好像他就不大愿意来。\x02\x03",

            "他有些难以面对老师\x01",
            "或是自卑之类的情结。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1016F#5P啊哈哈……\x01",
            "这方面倒是有点可爱呢。\x02\x03",

            "#1017F阿加特他们\x01",
            "现在在干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#020F调查才刚刚开始，\x01",
            "还是要靠摸索吧。\x02\x03",

            "#021F好了，主日学校\x01",
            "好像在村里进行呢。\x02\x03",

            "先去确认地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DC")


    ChrTalk(    #73
        0x101,
        "#1006F#5P嗯，ＯＫ。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1218)
    EventEnd(0x0)
    Return()

    # Function_7_10A5 end

    def Function_8_14FB(): pass

    label("Function_8_14FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 1)), scpexpr(EXPR_END)), "loc_1503")
    Return()

    label("loc_1503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151D")
    Call(0, 10)
    FadeToBright(0, 0)

    label("loc_151D")

    EventBegin(0x0)
    OP_8C(0x0, 180, 0)
    OP_8C(0x1, 180, 0)

    ChrTalk(    #74
        0x101,
        "#1026F啊……\x02",
    )

    CloseMessageWindow()
    OP_82(0x85, 0x0)

    def lambda_1548():
        OP_6D(2428, 6000, -13190, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1548)

    def lambda_1560():
        OP_6B(8450, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1560)

    def lambda_1570():
        OP_6C(60000, 7000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1570)

    def lambda_1580():
        OP_67(0, 5095, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1580)
    StopSound(0x186A0, 0x3D090, 0x1B58)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 5180, 6000, -10280, 180)
    SetChrPos(0xF7, 6160, 6000, -8180, 180)
    OP_6D(5470, 6010, -12430, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_67(0, 8140, -10000, 0)
    StopSound(0x0, 0x0, 0x0)
    Sleep(500)

    def lambda_161D():
        OP_8E(0x101, 0x143C, 0x177A, 0xFFFFCEDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_161D)

    def lambda_1638():
        OP_8E(0xF7, 0x1810, 0x1770, 0xFFFFCEF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1638)
    FadeToBright(1000, 0)
    WaitChrThread(0xF7, 0x1)
    OP_AD(0x24002A, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x3E8)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        "#1025F#5P…………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_16D1")
    TurnDirection(0x106, 0x101, 400)
    Sleep(500)

    ChrTalk(    #76
        0x106,
        "#052F#4P什么，怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_16FF")

    label("loc_16D1")

    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #77
        0x103,
        "#023F#4P艾丝蒂尔……怎么了？\x02",
    )

    CloseMessageWindow()

    label("loc_16FF")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #78
        0x101,
        (
            "#1016F#5P啊哈哈……\x02\x03",

            "在这里和约修亚一起\x01",
            "吃过午饭……\x02\x03",

            "#1025F想起一点往事。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1776")

    ChrTalk(    #79
        0x106,
        "#552F#4P是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1790")

    label("loc_1776")


    ChrTalk(    #80
        0x103,
        "#522F#4P……这样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1790")


    ChrTalk(    #81
        0x101,
        (
            "#1008F#5P啊，不过，\x01",
            "其实不算什么重要的回忆。\x02\x03",

            "#1007F我就像连自己的心情\x01",
            "也没注意到的孩子一样……\x02\x03",

            "完全不在意别人的眼光，\x01",
            "还满不在乎地给约修亚\x01",
            "喂饭什么的……\x02\x03",

            "唉，想必约修亚\x01",
            "相当受不了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_189E")

    ChrTalk(    #82
        0x106,
        (
            "#051F#4P哼，现在也还是\x01",
            "很孩子气啊。\x02\x03",

            "怎样？\x01",
            "在这里稍事休息吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E3")

    label("loc_189E")


    ChrTalk(    #83
        0x103,
        (
            "#021F#4P呵呵……\x01",
            "很像艾丝蒂尔呢。\x02\x03",

            "#027F怎样？\x01",
            "在这里稍事休息？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(    #84
        0x101,
        (
            "#1012F#5P不了，现在\x01",
            "可不能再停留了。\x02\x03",

            "#1011F比起这个，得先去确认\x01",
            "主日学校是不是还在上课才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DA")

    label("loc_1950")


    ChrTalk(    #85
        0x101,
        (
            "#1012F#5P不了，现在\x01",
            "可不能再停留了。\x02\x03",

            "#1011F比起这个，机会难得，\x01",
            "去孤儿院看看吧。\x02\x03",

            "想和老师他们打个招呼，\x01",
            "还要打听关于『白影』的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_19FE")

    ChrTalk(    #86
        0x106,
        "#051F#4P啊啊，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_19FE")


    ChrTalk(    #87
        0x103,
        "#020F#4P嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1A18")

    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A2(0x1219)
    EventEnd(0x0)
    Return()

    # Function_8_14FB end

    def Function_9_1A53(): pass

    label("Function_9_1A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A6D")
    Call(0, 10)
    FadeToBright(0, 0)

    label("loc_1A6D")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 5780, 6000, -2110, 266)
    SetChrPos(0xF7, 5900, 6000, -3190, 271)
    OP_6D(4140, 6480, -3460, 0)
    OP_67(0, 8060, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(245000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #88
        "\x07\x05主日学校·授课中\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #89
        0x101,
        (
            "#1011F啊，主日学校\x01",
            "好像在这里开课呢。\x02\x03",

            "#1015F好像还没结束的样子，\x01",
            "在上什么课呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1BB8")

    ChrTalk(    #90
        0x106,
        (
            "#051F#6P看看里面吧。\x02\x03",

            "也有可能已经结束了，\x01",
            "但是忘记取掉贴纸了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C07")

    label("loc_1BB8")


    ChrTalk(    #91
        0x103,
        (
            "#020F#6P看看里面的情况怎样？\x02\x03",

            "也有可能已经结束了，\x01",
            "但是忘记取掉贴纸了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C07")


    ChrTalk(    #92
        0x101,
        "#1006F嗯，看看吧。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x11BC, 0x1946, 0xFFFFF736, 0x7D0, 0x0)
    OP_8C(0x101, 270, 0)
    Sleep(500)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x3)
    Sleep(1000)

    ChrTalk(    #93
        0x101,
        "#1015F（嗯～我看看……）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        "#1004F（咦，那个人……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1A53 end

    def Function_10_1CB7(): pass

    label("Function_10_1CB7")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D31"),
        (1, "loc_1D37"),
        (SWITCH_DEFAULT, "loc_1D3D"),
    )


    label("loc_1D31")

    OP_A2(0x1200)
    Jump("loc_1D3D")

    label("loc_1D37")

    OP_A2(0x1201)
    Jump("loc_1D3D")

    label("loc_1D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1D4B")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1D4F")

    label("loc_1D4B")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1D4F")

    Return()

    # Function_10_1CB7 end

    def Function_11_1D50(): pass

    label("Function_11_1D50")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #95
        (
            "\x07\x05      卢安市长选举\x01",
            "※投票日请务必\x01",
            "　前往投票所\x01",
            "　　　　　选举管理委员会\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_1D50 end

    def Function_12_1DCA(): pass

    label("Function_12_1DCA")

    EventBegin(0x1)

    ChrTalk(    #96
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_1DF6():
        OP_6D(38050, -50, 9240, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1DF6)

    def lambda_1E0E():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1E0E)

    def lambda_1E1E():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1E1E)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #97
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA5")
    OP_C0(0xE, 0x15, 0x94FC, 0xFFFFFFD8, 0x29B8, 0xB4, 0x95A6, 0xFFFFF9FC, 0x1B58)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_1EB4")

    label("loc_1EA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB4")
    EventEnd(0x1)

    label("loc_1EB4")

    Return()

    # Function_12_1DCA end

    def Function_13_1EB5(): pass

    label("Function_13_1EB5")

    SetPlaceName(0x58)
    Return()

    # Function_13_1EB5 end

    def Function_14_1EB9(): pass

    label("Function_14_1EB9")

    SetPlaceName(0x57)
    Return()

    # Function_14_1EB9 end

    def Function_15_1EBD(): pass

    label("Function_15_1EBD")

    SetPlaceName(0x59)
    Return()

    # Function_15_1EBD end

    SaveToFile()

Try(main)
