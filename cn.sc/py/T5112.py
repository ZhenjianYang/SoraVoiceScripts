from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T5112   ._SN',
        MapName             = 'Other',
        Location            = 'T5112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '罗伯特',                               # 9
        '折断的枪',                             # 10
        '小说',                                 # 11
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
        'ED6_DT07/CH01450 ._CH',             # 00
        'ED6_DT26/CH20267 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01450P._CP',             # 00
        'ED6_DT26/CH20267P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
    )

    DeclNpc(
        X                   = 26690,
        Z                   = 0,
        Y                   = 5140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 18860,
        Z                   = -300,
        Y                   = 5310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 140520,
        Z                   = 650,
        Y                   = -33440,
        Direction           = 85,
        Unknown2            = 0,
        Unknown3            = 1703938,
        ChipIndex           = 0x2,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 25470,
        TriggerZ            = -300,
        TriggerY            = 4940,
        TriggerRange        = 800,
        ActorX              = 26690,
        ActorZ              = 1500,
        ActorY              = 5140,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18860,
        TriggerZ            = -300,
        TriggerY            = 5310,
        TriggerRange        = 800,
        ActorX              = 18860,
        ActorZ              = -300,
        ActorY              = 5310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21170,
        TriggerZ            = 0,
        TriggerY            = 17380,
        TriggerRange        = 800,
        ActorX              = 20960,
        ActorZ              = 1000,
        ActorY              = 18200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26900,
        TriggerZ            = 0,
        TriggerY            = 7220,
        TriggerRange        = 800,
        ActorX              = 28160,
        ActorZ              = 1000,
        ActorY              = 7060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19970,
        TriggerZ            = -300,
        TriggerY            = 5580,
        TriggerRange        = 800,
        ActorX              = 19970,
        ActorZ              = -300,
        ActorY              = 5580,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26550,
        TriggerZ            = 110,
        TriggerY            = 15520,
        TriggerRange        = 800,
        ActorX              = 27430,
        ActorZ              = 1110,
        ActorY              = 16059,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14070,
        TriggerZ            = 0,
        TriggerY            = 17590,
        TriggerRange        = 800,
        ActorX              = 14070,
        ActorZ              = 1000,
        ActorY              = 17590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85780,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 700,
        ActorX              = 85180,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 113640,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 700,
        ActorX              = 113040,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140520,
        TriggerZ            = 0,
        TriggerY            = -33440,
        TriggerRange        = 800,
        ActorX              = 140520,
        ActorZ              = 1000,
        ActorY              = -33440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28A",          # 00, 0
        "Function_1_2B0",          # 01, 1
        "Function_2_328",          # 02, 2
        "Function_3_3CF",          # 03, 3
        "Function_4_3D4",          # 04, 4
        "Function_5_64F",          # 05, 5
        "Function_6_82E",          # 06, 6
        "Function_7_848",          # 07, 7
        "Function_8_862",          # 08, 8
        "Function_9_87C",          # 09, 9
        "Function_10_896",         # 0A, 10
        "Function_11_8B0",         # 0B, 11
        "Function_12_8CA",         # 0C, 12
        "Function_13_921",         # 0D, 13
        "Function_14_978",         # 0E, 14
        "Function_15_A3C",         # 0F, 15
        "Function_16_AF7",         # 10, 16
        "Function_17_BBC",         # 11, 17
        "Function_18_C78",         # 12, 18
        "Function_19_D3F",         # 13, 19
        "Function_20_1C4B",        # 14, 20
    )


    def Function_0_28A(): pass

    label("Function_0_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29F")
    SetChrFlags(0x8, 0x80)
    OP_64(0x0, 0x1)

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AF")
    Event(0, 5)

    label("loc_2AF")

    Return()

    # Function_0_28A end

    def Function_1_2B0(): pass

    label("Function_1_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    OP_64(0x0, 0x1)
    Jump("loc_302")

    label("loc_2D2")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_65(0x0, 0x1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 5)), scpexpr(EXPR_END)), "loc_312")
    SetChrFlags(0xA, 0x80)
    OP_64(0x9, 0x1)

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_END)), "loc_327")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_327")

    Return()

    # Function_1_2B0 end

    def Function_2_328(): pass

    label("Function_2_328")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_359"),
        (1, "loc_365"),
        (2, "loc_371"),
        (3, "loc_37D"),
        (4, "loc_389"),
        (5, "loc_395"),
        (6, "loc_3A1"),
        (SWITCH_DEFAULT, "loc_3AD"),
    )


    label("loc_359")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_3B9")

    label("loc_365")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_3B9")

    label("loc_371")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_3B9")

    label("loc_37D")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_3B9")

    label("loc_389")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3B9")

    label("loc_395")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_3B9")

    label("loc_3A1")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B9")

    label("loc_3AD")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B9")

    label("loc_3B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B9")

    label("loc_3CE")

    Return()

    # Function_2_328 end

    def Function_3_3CF(): pass

    label("Function_3_3CF")

    Call(0, 4)
    Return()

    # Function_3_3CF end

    def Function_4_3D4(): pass

    label("Function_4_3D4")

    TalkBegin(0x8)
    OP_A2(0x1007)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x2D6, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")

    ChrTalk(    #0
        0x8,
        (
            "啊，艾丝蒂尔……\x01",
            "得到『天眼』了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "那可是所谓的\x01",
            "高级结晶回路呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "要镶嵌它的话\x01",
            "就必须先强化结晶孔才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "虽然需要耗费相对数量的耀晶片，\x01",
            "不过也能提高最大ＥＰ，所以建议一试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "工房的菜单里\x01",
            "选[改造·换钱]-[结晶孔]\x01",
            "就能强化结晶孔。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1041)
    TalkEnd(0x8)
    Return()

    label("loc_4EF")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "买东西\x01",          # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558")
    OP_0D()
    OP_A9(0xFA)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_558")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571")
    OP_0D()
    OP_A9(0xFB)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_571")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_582")
    TalkEnd(0x8)
    Return()

    label("loc_582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_604")

    ChrTalk(    #5
        0x8,
        (
            "若不是强化过的结晶孔，\x01",
            "就无法装配高级结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "但是，在战斗中应该会很有帮助。\x01",
            "希望你们都能够事先强化结晶孔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64B")

    label("loc_604")


    ChrTalk(    #7
        0x8,
        "你们两人都要小心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "需要调整导力器的时候，\x01",
            "请随时来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64B")

    TalkEnd(0x8)
    Return()

    # Function_4_3D4 end

    def Function_5_64F(): pass

    label("Function_5_64F")

    EventBegin(0x0)
    OP_6D(20200, 0, 18730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 18800, -800, 500, 0)
    SetChrPos(0x10A, 19720, -800, 500, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_6CC():
        OP_6D(18420, -300, 3580, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6CC)
    Sleep(2000)

    def lambda_6E9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E9)

    def lambda_6FB():
        OP_8E(0x101, 0x4970, 0xFFFFFDDA, 0x85C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FB)
    Sleep(200)

    def lambda_71B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_71B)
    OP_8E(0x10A, 0x4D08, 0xFFFFFDDA, 0x6AE, 0x7D0, 0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x101,
        (
            "#1026F#6P啊……\x02\x03",

            "那枪，是克鲁茨前辈的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10A,
        "#813F…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10A, 270, 500)
    Sleep(500)

    ChrTalk(    #11
        0x10A,
        (
            "#810F总之……\x01",
            "先调查宿舍里看看吧。\x02\x03",

            "说不定能找到\x01",
            "什么线索……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)

    ChrTalk(    #12
        0x101,
        "#1002F#6P嗯……明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x101C)
    OP_28(0x80, 0x1, 0x2)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_5_64F end

    def Function_6_82E(): pass

    label("Function_6_82E")

    EventBegin(0x0)
    Call(0, 13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_840")
    EventEnd(0x0)
    Jump("loc_842")

    label("loc_840")

    EventEnd(0x1)

    label("loc_842")

    SetMapFlags(0x2000000)
    Return()

    # Function_6_82E end

    def Function_7_848(): pass

    label("Function_7_848")

    EventBegin(0x0)
    Call(0, 14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_85A")
    EventEnd(0x0)
    Jump("loc_85C")

    label("loc_85A")

    EventEnd(0x1)

    label("loc_85C")

    SetMapFlags(0x2000000)
    Return()

    # Function_7_848 end

    def Function_8_862(): pass

    label("Function_8_862")

    EventBegin(0x0)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_874")
    EventEnd(0x0)
    Jump("loc_876")

    label("loc_874")

    EventEnd(0x1)

    label("loc_876")

    SetMapFlags(0x2000000)
    Return()

    # Function_8_862 end

    def Function_9_87C(): pass

    label("Function_9_87C")

    EventBegin(0x0)
    Call(0, 16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_88E")
    EventEnd(0x0)
    Jump("loc_890")

    label("loc_88E")

    EventEnd(0x1)

    label("loc_890")

    SetMapFlags(0x2000000)
    Return()

    # Function_9_87C end

    def Function_10_896(): pass

    label("Function_10_896")

    EventBegin(0x0)
    Call(0, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_8A8")
    EventEnd(0x0)
    Jump("loc_8AA")

    label("loc_8A8")

    EventEnd(0x1)

    label("loc_8AA")

    SetMapFlags(0x2000000)
    Return()

    # Function_10_896 end

    def Function_11_8B0(): pass

    label("Function_11_8B0")

    EventBegin(0x0)
    Call(0, 18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_8C2")
    EventEnd(0x0)
    Jump("loc_8C4")

    label("loc_8C2")

    EventEnd(0x1)

    label("loc_8C4")

    SetMapFlags(0x2000000)
    Return()

    # Function_11_8B0 end

    def Function_12_8CA(): pass

    label("Function_12_8CA")

    SetChrFlags(0xA, 0x80)
    OP_64(0x9, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\x3A\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23A, 1)
    OP_A2(0x10B5)
    TalkEnd(0xFF)
    Return()

    # Function_12_8CA end

    def Function_13_921(): pass

    label("Function_13_921")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #14
        (
            "\x07\x05折断的枪滚落在地。\x01",
            "看来是克鲁茨的武器。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_13_921 end

    def Function_14_978(): pass

    label("Function_14_978")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05窗户玻璃碎片散乱一地。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A37")
    OP_A2(0x101D)
    OP_28(0x80, 0x1, 0x4)

    ChrTalk(    #16
        0x101,
        (
            "#1015F这是昨天晚上\x01",
            "猎兵闯入时留下的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#812F嗯……\x02\x03",

            "那身体的动作……\x01",
            "恐怕是经过了专门的训练。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A37")

    Call(0, 19)
    Return()

    # Function_14_978 end

    def Function_15_A3C(): pass

    label("Function_15_A3C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05通讯器被破坏了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF2")
    OP_A2(0x101E)
    OP_28(0x80, 0x1, 0x8)

    ChrTalk(    #19
        0x10A,
        (
            "#1316F不愧是职业佣兵。\x01",
            "连这个都不放过吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1002F原来如此。\x01",
            "不让我们求援吧。\x02\x03",

            "这可是重创……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF2")

    Call(0, 19)
    Return()

    # Function_15_A3C end

    def Function_16_AF7(): pass

    label("Function_16_AF7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #21
        "\x07\x05地上都是血污。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7")
    OP_A2(0x101F)
    OP_28(0x80, 0x1, 0x10)

    ChrTalk(    #22
        0x101,
        (
            "#1026F这个……\x01",
            "难道是克鲁茨前辈的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#813F嗯……\x01",
            "很可能是前辈的。\x02\x03",

            "从地面的血量判断，\x01",
            "他并未受致命伤……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB7")

    Call(0, 19)
    Return()

    # Function_16_AF7 end

    def Function_17_BBC(): pass

    label("Function_17_BBC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #24
        (
            "\x07\x05放食材的罐子\x01",
            "空了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C73")
    OP_A2(0x1020)
    OP_28(0x80, 0x1, 0x20)

    ChrTalk(    #25
        0x101,
        (
            "#1004F这个……\x01",
            "是敌人拿走的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10A,
        (
            "#812F嗯、嗯～\x01",
            "很有可能。\x02\x03",

            "管理员也不在，\x01",
            "到底怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C73")

    Call(0, 19)
    Return()

    # Function_17_BBC end

    def Function_18_C78(): pass

    label("Function_18_C78")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #27
        "\x07\x05好像有什么东西被撕破了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3A")
    OP_A2(0x1021)
    OP_28(0x80, 0x1, 0x40)

    ChrTalk(    #28
        0x101,
        (
            "#1002F我记得这里\x01",
            "好像贴着地图吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10A,
        (
            "#812F嗯，和我们\x01",
            "持有的是一样的。\x02\x03",

            "#818F把那个拿走也就是说……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A")

    Call(0, 19)
    Return()

    # Function_18_C78 end

    def Function_19_D3F(): pass

    label("Function_19_D3F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 5)), scpexpr(EXPR_END)), "loc_D5A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 6)), scpexpr(EXPR_END)), "loc_D6B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 7)), scpexpr(EXPR_END)), "loc_D7C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 0)), scpexpr(EXPR_END)), "loc_D8D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 1)), scpexpr(EXPR_END)), "loc_D9E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DAC")
    Return()

    label("loc_DAC")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 21280, 0, 9960, 170)
    SetChrPos(0x10A, 22640, 0, 9100, 262)
    OP_6D(23000, 0, 10260, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(3230, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x101,
        (
            "#1P#1015F大致已经把整个宿舍\x01",
            "调查了一遍……\x02\x03",

            "二楼完全没有异常。\x01",
            "被弄乱的似乎只有一楼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10A,
        (
            "#2P#1316F嗯……\x01",
            "应该有什么理由吧。\x02\x03",

            "#816F不过，敌人要做什么\x01",
            "大体上明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1P#1004F咦……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10A,
        (
            "#2P#812F敌人的行动虽然疑点众多\x01",
            "却也有连贯的地方。\x02\x03",

            "这个宿舍，还有森林的帐篷。\x02\x03",

            "把两个地方发现的\x01",
            "线索联系起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1P#1006F啊……难不成！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x18\x07\x05敌人采取的行动是？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【从峡谷撤退了】\x01",          # 0
            "【封锁了峡谷的入口】\x01",      # 1
            "【向新的据点转移了】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_104E"),
        (1, "loc_1137"),
        (2, "loc_11F8"),
        (SWITCH_DEFAULT, "loc_128B"),
    )


    label("loc_104E")


    ChrTalk(    #36
        0x10A,
        (
            "#2P#813F不，我想不会的。\x02\x03",

            "如果撤退了，应该没有\x01",
            "把前辈们带走的必要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1P#1007F啊，那倒也是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        (
            "#2P#812F大概在森林里的帐篷\x01",
            "是为了袭击这个宿舍\x01",
            "而建造的临时据点吧。\x02\x03",

            "这样的话……\x01",
            "那里人烟稀少，\x01",
            "想必是转移到其他据点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128B")

    label("loc_1137")

    OP_2B(0x7E, 0x1)

    ChrTalk(    #39
        0x10A,
        (
            "#2P#817F嗯……\x01",
            "这个可能性很高哦。\x02\x03",

            "#810F不过，还有比这\x01",
            "更确定的事。\x02\x03",

            "多半森林里的帐篷\x01",
            "是为了袭击这个宿舍\x01",
            "而建造的临时据点吧。\x02\x03",

            "这样的话……\x01",
            "那里人烟稀少，\x01",
            "想必是转移到其他据点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128B")

    label("loc_11F8")

    OP_2B(0x7E, 0x3)

    ChrTalk(    #40
        0x10A,
        (
            "#2P#810F嗯，我也这么想。\x02\x03",

            "多半森林里的帐篷\x01",
            "是为了袭击这个宿舍\x01",
            "而建造的临时据点吧。\x02\x03",

            "这样的话……\x01",
            "那里人烟稀少，\x01",
            "想必是转移到其他据点了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128B")


    ChrTalk(    #41
        0x101,
        (
            "#1P#1004F啊，原来如此……\x02\x03",

            "#1015F不过，不打算\x01",
            "用这个宿舍当据点了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        (
            "#2P#812F从昨天的袭击也能看出来，\x01",
            "这里的防守不太稳固。\x02\x03",

            "万一，协会的支援来了，\x01",
            "那能和人质一起隐藏起来的地方……\x02\x03",

            "应该是把据点\x01",
            "移往这样的地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1P#1006F嗯嗯。\x01",
            "这样考虑似乎很合理。\x02\x03",

            "如果是这样，\x01",
            "他们转移的地方……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 20220, -550, 0, 181)

    NpcTalk(    #44
        0x8,
        "男人的声音",
        "#1P你、你们！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_141D():
        OP_6D(22240, -300, 7440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_141D)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x10A, 0x8, 400)
    OP_4A(0x8, 255)
    OP_9F(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)

    def lambda_1457():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1457)
    OP_8E(0x8, 0x4F1A, 0xFFFFFDDA, 0x7A8, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #45
        0x10A,
        "#814F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1004F罗伯特先生！？\x02\x03",

            "#1018F没、没事吗！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14CB():
        OP_8E(0xFE, 0x57DA, 0xFFFFFED4, 0x1B1C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_14CB)
    Sleep(100)

    def lambda_14EB():
        OP_8E(0xFE, 0x52A8, 0xFFFFFED4, 0x1B80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14EB)
    Sleep(200)

    def lambda_150B():
        OP_8E(0xFE, 0x5334, 0xFFFFFED4, 0x14BE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_150B)
    WaitChrThread(0x10A, 0x0)
    OP_8C(0x10A, 224, 500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x8, 0x0)

    NpcTalk(    #47
        0x8,
        "维修师罗伯特",
        (
            "昨夜，克鲁茨前辈\x01",
            "看准间隙让我逃走……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #48
        0x8,
        "维修师罗伯特",
        "之前一直想办法躲着。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1P#1008F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10A,
        (
            "#5P#1314F太好了……\x01",
            "他平安无事……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #51
        0x8,
        "维修师罗伯特",
        (
            "抱歉……\x01",
            "我竟然一个人逃跑。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #52
        0x8,
        "维修师罗伯特",
        (
            "真是的……\x01",
            "身为男人实在是太丢脸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1P#1016F别、别消沉啦～\x01",
            "毕竟对方是职业的佣兵嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10A,
        (
            "#5P#1310F嗯嗯，就是说啊。\x02\x03",

            "没有成为人质\x01",
            "就已经很幸运了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #55
        0x8,
        "维修师罗伯特",
        (
            "是吗……\x01",
            "听你们这么说，我心里好受多了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x8,
        "维修师罗伯特",
        (
            "那么最后，克鲁茨前辈\x01",
            "和管理员去哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1P#1003F这、这个……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "\x07\x05说出了敌方集团将两人\x01",
            "转移到其它据点的可能性。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    NpcTalk(    #59
        0x8,
        "维修师罗伯特",
        (
            "原来如此……\x01",
            "容易守卫的据点啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #60
        0x8,
        "维修师罗伯特",
        (
            "这么说来……\x01",
            "不就是『格林姆瑟尔小要塞』吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1P#1004F要、要塞！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10A,
        "#5P#814F这、这附近有那种东西吗？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #63
        0x8,
        "维修师罗伯特",
        (
            "虽说是要塞，\x01",
            "但并不是真的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #64
        0x8,
        "维修师罗伯特",
        (
            "是最近才刚刚建造而成的，\x01",
            "模仿军事设施的训练设施。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x8,
        "维修师罗伯特",
        "主要用做反恐训练。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1P#1015F还、还有这种地方啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)
    Sleep(500)

    ChrTalk(    #67
        0x101,
        "#6P#1002F……亚妮拉丝。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(    #68
        0x10A,
        "#5P#816F嗯……明白！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #69
        0x8,
        "维修师罗伯特",
        "喂、喂……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #70
        0x8,
        "维修师罗伯特",
        (
            "你们两个该不是\x01",
            "打算挑战那个集团吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #71
        0x8,
        "维修师罗伯特",
        (
            "还是联络协会\x01",
            "求援比较好吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    TurnDirection(0x10A, 0x8, 500)

    ChrTalk(    #72
        0x101,
        "#1P#1002F啊，通信器坏掉了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #73
        0x8,
        "维修师罗伯特",
        "…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10A,
        (
            "#5P#812F嗯，罗伯特先生\x01",
            "通讯器的修理就拜托了。\x02\x03",

            "一修好就通知协会\x01",
            "向他们求援行吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0x8,
        "维修师罗伯特",
        "……明白了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0x8,
        "维修师罗伯特",
        (
            "如果需要整备导力器\x01",
            "就到工房来。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0x8,
        "维修师罗伯特",
        "那么祝你们好运！\x02",
    )

    CloseMessageWindow()

    def lambda_1AEE():
        OP_6D(24810, 0, 6590, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AEE)

    def lambda_1B06():
        OP_8E(0xFE, 0x5BF4, 0x0, 0x16E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B06)
    OP_8C(0x101, 89, 500)
    OP_8C(0x10A, 89, 500)
    WaitChrThread(0x8, 0x0)

    def lambda_1B34():
        OP_8E(0xFE, 0x609A, 0x0, 0x1AB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B34)
    WaitChrThread(0x8, 0x0)

    def lambda_1B54():
        OP_8E(0xFE, 0x68CE, 0x0, 0x1AEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B54)
    WaitChrThread(0x8, 0x0)

    def lambda_1B74():
        OP_8E(0xFE, 0x6842, 0x0, 0x1414, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B74)
    WaitChrThread(0x8, 0x0)
    OP_8C(0x8, 258, 500)
    OP_43(0x8, 0x0, 0x0, 0x2)
    WaitChrThread(0x8, 0x1)

    def lambda_1BA7():
        OP_6D(22920, -300, 7620, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BA7)
    OP_4B(0x8, 255)
    OP_65(0x0, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x10A, 262, 500)

    ChrTalk(    #78
        0x10A,
        (
            "#2P#816F好了……\x01",
            "走吧，艾丝蒂尔。\x02\x03",

            "去那个『格林姆瑟尔小要塞』！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#6P#1018F喔，明白了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1022)
    OP_28(0x80, 0x1, 0x80)
    OP_28(0x80, 0x1, 0x100)
    OP_28(0x80, 0x1, 0x200)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    Return()

    # Function_19_D3F end

    def Function_20_1C4B(): pass

    label("Function_20_1C4B")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "休息\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD3")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    OP_8C(0x0, 270, 0)
    OP_30(0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_0D()
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1CD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CED")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1CED")

    Return()

    # Function_20_1C4B end

    SaveToFile()

Try(main)
