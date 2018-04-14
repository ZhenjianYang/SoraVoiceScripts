from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5310   ._SN',
        MapName             = 'Other',
        Location            = 'C5310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        '幻惑之铃露茜奥拉',                     # 9
        '无形迷雾',                             # 10
        '气雾兽',                               # 11
        '残像',                                 # 12
        '残像',                                 # 13
        '目标用照相机',                         # 14
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 32500,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = 32500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18E",          # 00, 0
        "Function_1_1ED",          # 01, 1
        "Function_2_268",          # 02, 2
        "Function_3_46D",          # 03, 3
        "Function_4_69A",          # 04, 4
        "Function_5_1036",         # 05, 5
        "Function_6_10BB",         # 06, 6
        "Function_7_1140",         # 07, 7
        "Function_8_1166",         # 08, 8
        "Function_9_118C",         # 09, 9
        "Function_10_11B2",        # 0A, 10
        "Function_11_11D8",        # 0B, 11
        "Function_12_1AFB",        # 0C, 12
        "Function_13_1B70",        # 0D, 13
        "Function_14_1C20",        # 0E, 14
        "Function_15_1CD0",        # 0F, 15
        "Function_16_2EB5",        # 10, 16
        "Function_17_4539",        # 11, 17
        "Function_18_45D2",        # 12, 18
        "Function_19_45F8",        # 13, 19
        "Function_20_4617",        # 14, 20
        "Function_21_463D",        # 15, 21
        "Function_22_4699",        # 16, 22
        "Function_23_4707",        # 17, 23
        "Function_24_481E",        # 18, 24
        "Function_25_484F",        # 19, 25
        "Function_26_48D6",        # 1A, 26
        "Function_27_4969",        # 1B, 27
    )


    def Function_0_18E(): pass

    label("Function_0_18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_19F")
    OP_A3(0x10F0)
    Event(0, 23)
    Jump("loc_1EC")

    label("loc_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C9")
    Event(0, 24)
    Jump("loc_1EC")

    label("loc_1C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3")
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_1EC")

    label("loc_1E3")

    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_1EC")

    Return()

    # Function_0_18E end

    def Function_1_1ED(): pass

    label("Function_1_1ED")

    OP_22(0x1C3, 0x1, 0x64)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_END)), "loc_207")
    OP_64(0x0, 0x1)
    OP_71(0x2, 0x4)

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_217")
    OP_72(0x4, 0x4)

    label("loc_217")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x462), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238")
    Call(0, 2)
    Jump("loc_245")

    label("loc_238")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 3)

    label("loc_245")

    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_1ED end

    def Function_2_268(): pass

    label("Function_2_268")

    OP_D2(0x2701C8, 0x2701CD, 0x0)
    OP_D2(0x29017E, 0x290182, 0x1)
    OP_D2(0x9038E, 0x90392, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270111, 0x270121, 0x4)
    OP_D2(0x270130, 0x270140, 0x5)
    OP_D2(0x270131, 0x270141, 0x6)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_2D3"),
        (3, "loc_2EA"),
        (4, "loc_301"),
        (6, "loc_318"),
        (7, "loc_32F"),
        (8, "loc_346"),
        (10, "loc_35D"),
        (SWITCH_DEFAULT, "loc_374"),
    )


    label("loc_2D3")

    OP_D2(0x70218, 0x70224, 0x7)
    OP_D2(0x70219, 0x70225, 0x8)
    Jump("loc_374")

    label("loc_2EA")

    OP_D2(0x701E8, 0x701F4, 0x7)
    OP_D2(0x701E9, 0x701F5, 0x8)
    Jump("loc_374")

    label("loc_301")

    OP_D2(0x27036E, 0x27037B, 0x7)
    OP_D2(0x27036F, 0x27037C, 0x8)
    Jump("loc_374")

    label("loc_318")

    OP_D2(0x70230, 0x7023C, 0x7)
    OP_D2(0x70231, 0x7023D, 0x8)
    Jump("loc_374")

    label("loc_32F")

    OP_D2(0x70248, 0x70254, 0x7)
    OP_D2(0x70249, 0x70255, 0x8)
    Jump("loc_374")

    label("loc_346")

    OP_D2(0x270176, 0x270183, 0x7)
    OP_D2(0x270177, 0x270184, 0x8)
    Jump("loc_374")

    label("loc_35D")

    OP_D2(0x702B4, 0x702BB, 0x7)
    OP_D2(0x702B5, 0x702BC, 0x8)
    Jump("loc_374")

    label("loc_374")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_399"),
        (3, "loc_3B0"),
        (4, "loc_3C7"),
        (6, "loc_3DE"),
        (7, "loc_3F5"),
        (8, "loc_40C"),
        (10, "loc_423"),
        (SWITCH_DEFAULT, "loc_43A"),
    )


    label("loc_399")

    OP_D2(0x70218, 0x70224, 0x9)
    OP_D2(0x70219, 0x70225, 0xA)
    Jump("loc_43A")

    label("loc_3B0")

    OP_D2(0x701E8, 0x701F4, 0x9)
    OP_D2(0x701E9, 0x701F5, 0xA)
    Jump("loc_43A")

    label("loc_3C7")

    OP_D2(0x27036E, 0x27037B, 0x9)
    OP_D2(0x27036F, 0x27037C, 0xA)
    Jump("loc_43A")

    label("loc_3DE")

    OP_D2(0x70230, 0x7023C, 0x9)
    OP_D2(0x70231, 0x7023D, 0xA)
    Jump("loc_43A")

    label("loc_3F5")

    OP_D2(0x70248, 0x70254, 0x9)
    OP_D2(0x70249, 0x70255, 0xA)
    Jump("loc_43A")

    label("loc_40C")

    OP_D2(0x270176, 0x270183, 0x9)
    OP_D2(0x270177, 0x270184, 0xA)
    Jump("loc_43A")

    label("loc_423")

    OP_D2(0x702B4, 0x702BB, 0x9)
    OP_D2(0x702B5, 0x702BC, 0xA)
    Jump("loc_43A")

    label("loc_43A")

    OP_D2(0x270256, 0x270260, 0xB)
    OP_D2(0x270257, 0x270261, 0xC)
    OP_D2(0x270258, 0x270262, 0xD)
    OP_D2(0x29017F, 0x290183, 0xE)
    OP_D2(0x9038F, 0x90393, 0xF)
    Return()

    # Function_2_268 end

    def Function_3_46D(): pass

    label("Function_3_46D")

    OP_D2(0x2701C8, 0x2701CD, 0x0)
    OP_D2(0x29017E, 0x290182, 0x1)
    OP_D2(0x9038E, 0x90392, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270111, 0x270121, 0x4)
    OP_D2(0x270130, 0x270140, 0x5)
    OP_D2(0x270131, 0x270141, 0x6)
    OP_D2(0x701D0, 0x701DC, 0x7)
    OP_D2(0x701D1, 0x701DD, 0x8)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_4EC"),
        (3, "loc_503"),
        (4, "loc_51A"),
        (6, "loc_531"),
        (7, "loc_548"),
        (8, "loc_55F"),
        (10, "loc_576"),
        (SWITCH_DEFAULT, "loc_58D"),
    )


    label("loc_4EC")

    OP_D2(0x70218, 0x70224, 0x9)
    OP_D2(0x70219, 0x70225, 0xA)
    Jump("loc_58D")

    label("loc_503")

    OP_D2(0x701E8, 0x701F4, 0x9)
    OP_D2(0x701E9, 0x701F5, 0xA)
    Jump("loc_58D")

    label("loc_51A")

    OP_D2(0x27036E, 0x27037B, 0x9)
    OP_D2(0x27036F, 0x27037C, 0xA)
    Jump("loc_58D")

    label("loc_531")

    OP_D2(0x70230, 0x7023C, 0x9)
    OP_D2(0x70231, 0x7023D, 0xA)
    Jump("loc_58D")

    label("loc_548")

    OP_D2(0x70248, 0x70254, 0x9)
    OP_D2(0x70249, 0x70255, 0xA)
    Jump("loc_58D")

    label("loc_55F")

    OP_D2(0x270176, 0x270183, 0x9)
    OP_D2(0x270177, 0x270184, 0xA)
    Jump("loc_58D")

    label("loc_576")

    OP_D2(0x702B4, 0x702BB, 0x9)
    OP_D2(0x702B5, 0x702BC, 0xA)
    Jump("loc_58D")

    label("loc_58D")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_5B2"),
        (3, "loc_5C9"),
        (4, "loc_5E0"),
        (6, "loc_5F7"),
        (7, "loc_60E"),
        (8, "loc_625"),
        (10, "loc_63C"),
        (SWITCH_DEFAULT, "loc_653"),
    )


    label("loc_5B2")

    OP_D2(0x70218, 0x70224, 0x9)
    OP_D2(0x70219, 0x70225, 0xA)
    Jump("loc_653")

    label("loc_5C9")

    OP_D2(0x701E8, 0x701F4, 0x9)
    OP_D2(0x701E9, 0x701F5, 0xA)
    Jump("loc_653")

    label("loc_5E0")

    OP_D2(0x27036E, 0x27037B, 0x9)
    OP_D2(0x27036F, 0x27037C, 0xA)
    Jump("loc_653")

    label("loc_5F7")

    OP_D2(0x70230, 0x7023C, 0x9)
    OP_D2(0x70231, 0x7023D, 0xA)
    Jump("loc_653")

    label("loc_60E")

    OP_D2(0x70248, 0x70254, 0x9)
    OP_D2(0x70249, 0x70255, 0xA)
    Jump("loc_653")

    label("loc_625")

    OP_D2(0x270176, 0x270183, 0x9)
    OP_D2(0x270177, 0x270184, 0xA)
    Jump("loc_653")

    label("loc_63C")

    OP_D2(0x702B4, 0x702BB, 0x9)
    OP_D2(0x702B5, 0x702BC, 0xA)
    Jump("loc_653")

    label("loc_653")

    OP_D2(0x270256, 0x270260, 0xB)
    OP_D2(0x270257, 0x270261, 0xC)
    OP_D2(0x270258, 0x270262, 0xD)
    OP_D2(0x29017F, 0x290183, 0xE)
    OP_D2(0x9038F, 0x90393, 0xF)
    OP_D2(0x2601C6, 0x2601CB, 0x10)
    OP_D2(0x2601C7, 0x2601CC, 0x11)
    Return()

    # Function_3_46D end

    def Function_4_69A(): pass

    label("Function_4_69A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 2)
    OP_6D(-720, 0, -17580, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x0, 0x0, 0x7)
    Sleep(80)
    OP_43(0x102, 0x0, 0x0, 0x8)
    Sleep(50)
    OP_43(0xF8, 0x0, 0x0, 0x9)
    Sleep(100)
    OP_43(0xF9, 0x0, 0x0, 0xA)

    def lambda_718():
        OP_6B(3960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_718)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF9, 0x1)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 520, 0, 25630, 180)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #0
        0x8,
        "女性的声音",
        (
            "哎呀……\x01",
            "预测有误吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DA")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_818")

    label("loc_7DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_801")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_818")

    label("loc_801")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_818")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_844")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_882")

    label("loc_844")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_882")

    label("loc_86B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_882")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_894():
        OP_6D(-550, 0, 26000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_894)

    def lambda_8AC():
        OP_67(0, 4870, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AC)

    def lambda_8C4():
        OP_6B(3290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C4)

    def lambda_8D4():
        OP_6E(288, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8D4)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x101, 1490, 0, 2610, 0)
    SetChrPos(0x102, 40, 0, 2660, 0)
    SetChrPos(0xF8, 1660, 0, 1390, 0)
    SetChrPos(0xF9, 260, 0, 1430, 0)

    ChrTalk(    #1
        0x101,
        "#1020F#2P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1042F#5P『幻惑之铃』……是你吗。\x02",
    )

    CloseMessageWindow()

    def lambda_96B():
        OP_6D(-1500, 0, 22220, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_96B)

    def lambda_983():
        OP_67(0, 4210, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_983)

    def lambda_99B():
        OP_6B(3400, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_99B)

    def lambda_9AB():
        OP_6E(292, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9AB)
    Sleep(1000)

    def lambda_9C0():
        OP_8E(0xFE, 0x546, 0x0, 0x3FC9, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C0)
    Sleep(80)

    def lambda_9E0():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x40E2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E0)
    Sleep(100)

    def lambda_A00():
        OP_8E(0xFE, 0x5BE, 0x0, 0x3A0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A00)
    Sleep(40)
    OP_8E(0xF9, 0xFFFFFFD8, 0x0, 0x3980, 0x1770, 0x0)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #3
        0x8,
        (
            "#244F我还预感那丫头\x01",
            "一定会来呢……\x02\x03",

            "#240F看来我的占卜还是不成熟呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1002F#6P……雪拉姐在\x01",
            "埃尔赛尤上待命呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1042F#6P即使如此……\x01",
            "你还是打算和我们战斗吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#244F……是啊。\x01",
            "我并没有帮助教授的义务，\x01",
            "直接离开也是可以的……\x02\x03",

            "#240F但说实话，没想到\x01",
            "你们能打败布卢布兰和瓦鲁特\x01",
            "来到这里。\x02\x03",

            "你们究竟成长到了什么程度……\x01",
            "我也想稍微见识一下。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 12)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x8, 13)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_71(0x0, 0x4)
    OP_6D(0, 0, 24000, 0)
    OP_67(0, 3240, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(0, 0)
    OP_6E(347, 0)
    SetChrPos(0x8, 0, 0, 25600, 180)
    SetChrPos(0x101, 600, 0, 17580, 0)
    SetChrPos(0x102, -600, 0, 17580, 0)
    SetChrPos(0xF8, 1200, 0, 16000, 0)
    SetChrPos(0xF9, -1200, 0, 16000, 0)
    OP_0D()

    def lambda_C92():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C92)
    LoadEffect(0x1, "scraft\\sc040_08.eff")
    PlayEffect(0x1, 0x0, 0xFF, 450, 0, 25660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x265, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_82(0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xA, 0x0, 0x0, 0x6)
    Sleep(800)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0x102, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DBD")

    label("loc_D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA6")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DBD")

    label("loc_DA6")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DBD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E27")

    label("loc_DE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E10")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E27")

    label("loc_E10")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E27")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    SetChrChipByIndex(0xF8, 7)
    SetChrChipByIndex(0xF9, 9)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 12)
    Sleep(500)

    ChrTalk(    #7
        0x8,
        (
            "#244F#5P要是连我也无法打倒的话，\x01",
            "你们就更没有可能\x01",
            "通过上面的挑战。\x02\x03",

            "#241F『幻惑之铃』的迷幻之舞……\x01",
            "请拿出真本事来破解吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EF9():
        OP_6D(0, 0, 24000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EF9)

    def lambda_F11():
        OP_67(0, 4610, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F11)

    def lambda_F29():
        OP_6B(2600, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F29)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 1)

    def lambda_F43():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F43)
    Sleep(30)
    SetChrChipByIndex(0x9, 15)
    SetChrFlags(0x9, 0x1000)

    def lambda_F6D():
        OP_91(0xFE, 0x3E8, 0x0, 0xFFFFEC78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_F6D)

    def lambda_F88():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F88)
    Sleep(30)
    SetChrChipByIndex(0xA, 14)
    SetChrFlags(0xA, 0x1000)

    def lambda_FB2():
        OP_91(0xFE, 0xFFFFFC18, 0x0, 0xFFFFEC78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_FB2)

    def lambda_FCD():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_FCD)

    def lambda_FE8():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_FE8)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x462, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 11)
    Return()

    # Function_4_69A end

    def Function_5_1036(): pass

    label("Function_5_1036")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 2)
    SetChrPos(0xFE, -2000, 2000, 26000, 180)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1067():

        label("loc_1067")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1067")

    QueueWorkItem2(0xFE, 3, lambda_1067)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_1084():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1084)

    def lambda_1096():
        OP_8F(0xFE, 0xFFFFF830, 0x1F4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1096)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x21A, 0x0, 0x64)
    Return()

    # Function_5_1036 end

    def Function_6_10BB(): pass

    label("Function_6_10BB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 1)
    SetChrPos(0xFE, 2000, 2000, 26000, 180)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)

    def lambda_10EC():

        label("loc_10EC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_10EC")

    QueueWorkItem2(0xFE, 3, lambda_10EC)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_1109():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1109)

    def lambda_111B():
        OP_8F(0xFE, 0x7D0, 0x1F4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_111B)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x21A, 0x0, 0x64)
    Return()

    # Function_6_10BB end

    def Function_7_1140(): pass

    label("Function_7_1140")

    SetChrPos(0xFE, 870, 0, -25040, 0)
    OP_8E(0xFE, 0x366, 0x0, 0xFFFFB988, 0xBB8, 0x0)
    Return()

    # Function_7_1140 end

    def Function_8_1166(): pass

    label("Function_8_1166")

    SetChrPos(0xFE, -390, 0, -25050, 0)
    OP_8E(0xFE, 0xFFFFFE7A, 0x0, 0xFFFFB97E, 0xBB8, 0x0)
    Return()

    # Function_8_1166 end

    def Function_9_118C(): pass

    label("Function_9_118C")

    SetChrPos(0xFE, 1150, 0, -26400, 0)
    OP_8E(0xFE, 0x47E, 0x0, 0xFFFFB438, 0xBB8, 0x0)
    Return()

    # Function_9_118C end

    def Function_10_11B2(): pass

    label("Function_10_11B2")

    SetChrPos(0xFE, -210, 0, -26410, 0)
    OP_8E(0xFE, 0xFFFFFF2E, 0x0, 0xFFFFB42E, 0xBB8, 0x0)
    Return()

    # Function_10_11B2 end

    def Function_11_11D8(): pass

    label("Function_11_11D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    SetChrPos(0x101, 1000, 0, 19000, 0)
    SetChrPos(0x102, -460, 0, 19000, 0)
    SetChrPos(0xF8, 1510, 0, 17400, 0)
    SetChrPos(0xF9, -110, 0, 17400, 0)
    OP_6D(-970, 0, 23910, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(315000, 0)
    OP_6E(334, 0)
    SetChrSubChip(0x8, 3)
    SetChrPos(0x8, 520, 0, 26000, 180)
    SetChrChipByIndex(0x8, 11)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    FadeToBright(1000, 0)
    OP_6B(3130, 2000)
    OP_0D()

    ChrTalk(    #8
        0x8,
        (
            "#247F呵呵……原来如此。\x02\x03",

            "这样的话……说不定\x01",
            "你们有资格继续向上层前进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#1040F#6P露茜奥拉……\x01",
            "你愿意退下了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#240F是啊……没有\x01",
            "继续待在这里的理由了。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x3, 0x0, 0x3E8)
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 12)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x8, 13)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)

    def lambda_13C3():
        OP_6D(-1400, 0, 24910, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13C3)

    def lambda_13DB():
        OP_67(0, 4000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13DB)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 12)
    OP_43(0xB, 0x1, 0x0, 0xD)
    OP_43(0xC, 0x1, 0x0, 0xE)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1469")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14A7")

    label("loc_1469")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1490")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14A7")

    label("loc_1490")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_14A7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D3")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1511")

    label("loc_14D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FA")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1511")

    label("loc_14FA")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1511")

    Sleep(1000)

    ChrTalk(    #12
        0x101,
        (
            "#1020F#6P等、等一下！\x02\x03",

            "雪拉姐的事……\x01",
            "你到底打算怎样！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#247F#2P我与那丫头的因缘\x01",
            "还没有了断……\x02\x03",

            "#240F所以，今后一定还会在\x01",
            "某处重逢吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x5A, 0x3E8)
    Sleep(500)

    ChrTalk(    #14
        0x8,
        (
            "#244F#2P……话说回来，前方\x01",
            "可是真正意义的死地哦。\x02\x03",

            "请你们做好准备后\x01",
            "再慎重前进吧。\x02\x03",

            "#241F……那么祝你们顺利………\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11E, 0x0, 0x64)

    def lambda_163B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_163B)

    def lambda_164D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_164D)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Sleep(500)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(    #15
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1035F#6P……走了吗。\x02",
    )

    CloseMessageWindow()

    def lambda_16B6():
        OP_6D(-820, 0, 20460, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16B6)

    def lambda_16CE():
        OP_67(0, 4700, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16CE)
    WaitChrThread(0x101, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1763")

    ChrTalk(    #17
        0x108,
        (
            "#071F#6P哎呀呀……\x01",
            "倒也是个通情达理的好女人嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_1763")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A3")

    ChrTalk(    #18
        0x104,
        (
            "#031F#6P呼，不愧是身为\x01",
            "雪拉的大姐的女人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_17A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E4")

    ChrTalk(    #19
        0x109,
        (
            "#1061F#6P怎么说呢……\x01",
            "有成熟女性的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_17E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_181E")

    ChrTalk(    #20
        0x106,
        (
            "#051F#6P嘿……\x01",
            "很明白事理的女人嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_181E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1858")

    ChrTalk(    #21
        0x10B,
        (
            "#210F#6P嗯……\x01",
            "有成熟女性的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_1858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188D")

    ChrTalk(    #22
        0x105,
        "#1168F#6P这么通情理真是太好了……\x02",
    )

    CloseMessageWindow()

    label("loc_188D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D3")

    ChrTalk(    #23
        0x107,
        (
            "#561F#6P但是，雪拉姐要是知道了\x01",
            "会不会失望呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E1")

    label("loc_18D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1920")

    ChrTalk(    #24
        0x105,
        (
            "#1169F#6P但是，雪拉扎德要是知道了，\x01",
            "说不定会失望呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E1")

    label("loc_1920")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1964")

    ChrTalk(    #25
        0x10B,
        (
            "#215F#6P但是，那个甩鞭子的\x01",
            "姐姐可能会失望呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E1")

    label("loc_1964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A8")

    ChrTalk(    #26
        0x106,
        (
            "#551F#6P但是，雪拉扎德那家伙\x01",
            "大概会很失望吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E1")

    label("loc_19A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E1")

    ChrTalk(    #27
        0x109,
        (
            "#1068F但是雪拉姐\x01",
            "不知道会不会失望啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E1")

    OP_8C(0x101, -180, 400)
    Sleep(300)

    ChrTalk(    #28
        0x101,
        (
            "#1007F#2P嗯……但是也没办法呢。\x02\x03",

            "#1015F那两人要是碰头了\x01",
            "就更令人担心……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)

    ChrTalk(    #29
        0x102,
        (
            "#1043F#5P也是……\x01",
            "我想这也是一种缘分。\x02\x03",

            "#1035F虽然她从舞台上退场了，\x01",
            "但我们的演出还未结束……\x02\x03",

            "#1040F就按照她的忠告谨慎前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #30
        0x101,
        "#1006F#4P……嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2237)
    OP_72(0x4, 0x4)
    OP_28(0x9F, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_11_11D8 end

    def Function_12_1AFB(): pass

    label("Function_12_1AFB")


    def lambda_1B01():
        OP_8E(0xFE, 0x352, 0x0, 0xFFFFBB54, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B01)
    Sleep(40)

    def lambda_1B21():
        OP_8E(0xFE, 0xFFFFFF24, 0x0, 0xFFFFBB72, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B21)
    Sleep(100)

    def lambda_1B41():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFB686, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1B41)
    Sleep(50)
    OP_8E(0xF9, 0xFFFFFCF4, 0x0, 0xFFFFB6D6, 0xBB8, 0x0)
    Return()

    # Function_12_1AFB end

    def Function_13_1B70(): pass

    label("Function_13_1B70")

    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 12)
    SetChrPos(0xB, 520, 0, 26000, 180)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_91(0xB, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_1BEB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C1F")
    OP_91(0xB, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_1BEB")

    label("loc_1C1F")

    Return()

    # Function_13_1B70 end

    def Function_14_1C20(): pass

    label("Function_14_1C20")

    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xC, 12)
    SetChrPos(0xC, 520, 0, 26000, 180)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_91(0xC, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xC, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xC, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xC, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_1C9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CCF")
    OP_91(0xC, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xC, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_1C9B")

    label("loc_1CCF")

    Return()

    # Function_14_1C20 end

    def Function_15_1CD0(): pass

    label("Function_15_1CD0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 3)
    OP_6D(-720, 0, -17580, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x0, 0x0, 0x7)
    Sleep(80)
    OP_43(0x102, 0x0, 0x0, 0x8)
    Sleep(50)
    OP_43(0xF8, 0x0, 0x0, 0x9)
    Sleep(100)
    OP_43(0xF9, 0x0, 0x0, 0xA)

    def lambda_1D4E():
        OP_6B(3960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D4E)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF9, 0x1)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 0, 0, 25630, 180)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #31
        0x8,
        "女性的声音",
        "呵呵……来得好。\x02",
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E75")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E34")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E72")

    label("loc_1E34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E5B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E72")

    label("loc_1E5B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1E72")

    Jump("loc_1EDA")

    label("loc_1E75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9C")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1EDA")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC3")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1EDA")

    label("loc_1EC3")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1EDA")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_1EEC():
        OP_6D(-550, 0, 26000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EEC)

    def lambda_1F04():
        OP_67(0, 4870, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F04)

    def lambda_1F1C():
        OP_6B(3290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F1C)

    def lambda_1F2C():
        OP_6E(288, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F2C)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x103, 330, 0, 350, 0)
    SetChrPos(0x101, 1300, 0, -1380, 0)
    SetChrPos(0x102, -100, 0, -1070, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8F")
    SetChrPos(0xF9, 920, 0, -3120, 0)
    Jump("loc_1FA0")

    label("loc_1F8F")

    SetChrPos(0xF8, 920, 0, -3120, 0)

    label("loc_1FA0")


    ChrTalk(    #32
        0x101,
        "#1020F#2P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#1042F#5P『幻惑之铃』……是你吗。\x02",
    )

    CloseMessageWindow()

    def lambda_1FE4():
        OP_6D(-1300, 0, 22700, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FE4)

    def lambda_1FFC():
        OP_67(0, 4210, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FFC)

    def lambda_2014():
        OP_6B(3480, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2014)

    def lambda_2024():
        OP_6E(292, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2024)
    Sleep(1000)

    def lambda_2039():
        OP_8E(0xFE, 0x64, 0x0, 0x424A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2039)
    Sleep(80)

    def lambda_2059():
        OP_8E(0xFE, 0x7D0, 0x0, 0x3E80, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2059)
    Sleep(150)

    def lambda_2079():
        OP_8E(0xFE, 0xFFFFFF38, 0x0, 0x3E1C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2079)
    Sleep(40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B7")
    OP_8E(0xF9, 0x532, 0x0, 0x3A98, 0x1770, 0x0)
    Jump("loc_20CB")

    label("loc_20B7")

    OP_8E(0xF8, 0x532, 0x0, 0x3A98, 0x1770, 0x0)

    label("loc_20CB")

    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #34
        0x103,
        "#522F#6P露茜奥拉……姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#244F竟能打败布卢布兰和瓦鲁特\x01",
            "到达这里……\x02\x03",

            "#240F你们还挺不赖的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#026F#6P姐姐……\x01",
            "请履行约定吧。\x02\x03",

            "#022F你说再次见面时，\x01",
            "会把哈维团长的事\x01",
            "全部告诉我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#241F啊啊……\x01",
            "杀死他的理由吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        "#522F#6P…………唔……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#244F这样啊……\x02\x03",

            "…………………………………\x02\x03",

            "#240F……我问你，雪拉扎德。\x02\x03",

            "对你来说，\x01",
            "团长是个怎样的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        (
            "#024F#6P这、这\x01",
            "还用说吗！\x02\x03",

            "当然是将身为孤儿的我\x01",
            "收养培育的恩人啊！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x24007F, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0x103,
        (
            "#524F#6P我虽然完全\x01",
            "不知道父母的样子……\x02\x03",

            "但是所谓的父亲大概\x01",
            "就是这样的感觉吧。\x01",
            "我一直是这么想的……\x02\x03",

            "#527F……然而……\x01",
            "然而为什么……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#244F是啊……\x01",
            "他是个温柔和蔼的人。\x02\x03",

            "#242F但是，身为旅行艺人的团长，\x01",
            "只有温柔和蔼是行不通的。\x02\x03",

            "从事肮脏的交易，把女艺人卖给客人\x01",
            "这种事，在我们这个行业中屡见不鲜。\x02\x03",

            "#244F但是团长……他却\x01",
            "从没做过那种事。\x02\x03",

            "因此他散尽了自己的全部财产……\x01",
            "还背上了巨大的债务。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x103,
        (
            "#024F#6P骗、骗人吧……！？\x02\x03",

            "团长他…\x01",
            "从来没有表现出那种……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#240F呵呵，他人虽好，\x01",
            "却非常要强。\x02\x03",

            "自然不会让我们察觉，\x01",
            "独自一人到处奔走，筹调资金……\x02\x03",

            "#244F……而最后，\x01",
            "他决定卖掉整个剧团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x103,
        "#023F#6P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#244F他打算把整个剧团\x01",
            "都托付给一名认识的贵族。\x02\x03",

            "说什么如果自己继续当团长，\x01",
            "我们就会永远贫苦下去……\x02\x03",

            "既然这样，还不如让可靠的人\x01",
            "来照顾我们更好……\x02\x03",

            "#240F……他大概就是这样的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        (
            "#522F#6P怎、怎么会……为什么……\x02\x03",

            "#024F要是他当时和我们商量的话，\x01",
            "我们一定会全力帮忙的……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#242F当他和我说明这一切时，\x01",
            "我也是这样劝说他的。\x02\x03",

            "但是，那个人太过顽固，\x01",
            "完全听不进去。\x02\x03",

            "#244F坚持认为自己太无能，\x01",
            "对我们的前途没有任何好处……\x02\x03",

            "这样钻进了牛角尖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x103,
        (
            "#025F#6P………………………………\x02\x03",

            "#522F就因为这个理由……\x01",
            "……姐姐就把团长……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#240F嗯，是啊。\x02\x03",

            "对我来说，他这种决定\x01",
            "完全就是难以容忍的背叛。\x02\x03",

            "#244F将廉价的幸福和安逸给我们，\x01",
            "却把更重要百倍的东西带走……\x02\x03",

            "要是这样的话，\x01",
            "在一开始就不应该收留大家。\x02\x03",

            "#241F所以，我杀了他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        (
            "#522F#6P…………………………………\x02\x03",

            "那样的话……\x01",
            "……我又算是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "#243F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#524F#6P我……全靠团长和姐姐\x01",
            "才能得到安逸幸福的生活……\x02\x03",

            "在你们的照顾下，我拥有了在贫民街中\x01",
            "从来没有得到过的温暖……\x02\x03",

            "#025F但是……团长死了……\x01",
            "……连姐姐也离开了……\x02\x03",

            "#527F这难道……\x01",
            "……不是更残酷的背叛吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#247F……呵呵，是啊……\x02\x03",

            "#242F雪拉扎德。\x01",
            "你有恨我的权利。\x02\x03",

            "带着那份恨意\x01",
            "来和我一战吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 12)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x8, 13)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_71(0x0, 0x4)
    OP_6D(0, 0, 24000, 0)
    OP_67(0, 3240, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(0, 0)
    OP_6E(347, 0)
    SetChrPos(0x8, 0, 0, 25600, 180)
    SetChrPos(0x103, 40, 0, 18530, 0)
    SetChrPos(0x101, 950, 0, 17000, 0)
    SetChrPos(0x102, -950, 0, 17000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC3")
    SetChrPos(0xF9, 0, 0, 15040, 0)
    Jump("loc_2AD4")

    label("loc_2AC3")

    SetChrPos(0xF8, 0, 0, 15040, 0)

    label("loc_2AD4")

    OP_0D()

    def lambda_2ADB():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2ADB)
    LoadEffect(0x1, "scraft\\sc040_08.eff")
    PlayEffect(0x1, 0x0, 0xFF, 450, 0, 25660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x265, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_82(0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xA, 0x0, 0x0, 0x6)
    Sleep(800)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0x102, 0x2)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C32")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF1")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C2F")

    label("loc_2BF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C18")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C2F")

    label("loc_2C18")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2C2F")

    Jump("loc_2C97")

    label("loc_2C32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C59")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C97")

    label("loc_2C59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C80")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C97")

    label("loc_2C80")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2C97")

    Sleep(1000)

    ChrTalk(    #55
        0x103,
        "#523F#6P姐姐……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#244F#5P要是连我也无法打倒的话，\x01",
            "你们就更没有可能\x01",
            "通过上面的挑战。\x02\x03",

            "#241F『幻惑之铃』的迷幻之舞……\x01",
            "请拿出真本事来破解吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    SetChrChipByIndex(0x103, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D67")
    SetChrChipByIndex(0xF9, 9)
    Jump("loc_2D6C")

    label("loc_2D67")

    SetChrChipByIndex(0xF8, 9)

    label("loc_2D6C")

    OP_0D()
    Sleep(500)

    def lambda_2D78():
        OP_6D(0, 0, 24000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D78)

    def lambda_2D90():
        OP_67(0, 4610, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D90)

    def lambda_2DA8():
        OP_6B(2600, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2DA8)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 1)

    def lambda_2DC2():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DC2)
    Sleep(30)
    SetChrChipByIndex(0x9, 15)
    SetChrFlags(0x9, 0x1000)

    def lambda_2DEC():
        OP_91(0xFE, 0x3E8, 0x0, 0xFFFFEC78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2DEC)

    def lambda_2E07():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E07)
    Sleep(30)
    SetChrChipByIndex(0xA, 14)
    SetChrFlags(0xA, 0x1000)

    def lambda_2E31():
        OP_91(0xFE, 0xFFFFFC18, 0x0, 0xFFFFEC78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2E31)

    def lambda_2E4C():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_2E4C)

    def lambda_2E67():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_2E67)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x462, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 16)
    Return()

    # Function_15_1CD0 end

    def Function_16_2EB5(): pass

    label("Function_16_2EB5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    Call(0, 3)
    OP_6D(-4300, 0, 27440, 0)
    OP_67(0, 3170, -10000, 0)
    OP_6B(3550, 0)
    OP_6C(315000, 0)
    OP_6E(317, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -5930, 0, 28960, 135)
    SetChrPos(0x103, -450, 0, 23490, 315)
    SetChrPos(0x101, 1530, 0, 22630, 315)
    SetChrPos(0x102, 320, 0, 21580, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8E")
    SetChrPos(0xF9, 2020, 0, 21130, 315)
    Jump("loc_2F9F")

    label("loc_2F8E")

    SetChrPos(0xF8, 2020, 0, 21130, 315)

    label("loc_2F9F")

    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 16)
    SetChrSubChip(0x8, 0)
    FadeToBright(1000, 0)
    OP_6B(3350, 2000)
    OP_0D()

    ChrTalk(    #57
        0x8,
        (
            "#247F#5P呵呵……原来如此。\x02\x03",

            "#240F这样的话……或许你们\x01",
            "有资格继续往上前进了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x103,
        (
            "#025F#6P……姐姐。\x01",
            "有一点，我需要更正。\x02\x03",

            "#524F我并没有办法让\x01",
            "自己憎恨姐姐。\x02\x03",

            "即使你离我而去，\x01",
            "即使你杀害了团长……\x02\x03",

            "#522F只是……\x01",
            "我的心里好难过，好悲哀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1026F#4P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        "#243F#5P……雪拉扎德………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#025F#6P而且，我还是无法相信。\x02\x03",

            "#522F姐姐竟会为了这样的理由\x01",
            "杀害了团长……\x02\x03",

            "杀害了那个因为替我们着想\x01",
            "才做了如此痛苦决定的团长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#240F#5P…………………………………\x02\x03",

            "#247F……呵呵……\x01",
            "果然是瞒不过你吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #63
        0x103,
        "#022F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "#240F#5P刚才的话……还有下文。\x02\x03",

            "当我明白他的决心已经到了\x01",
            "连我都无法说服的时候……\x02\x03",

            "#244F我便向他和盘托出了\x01",
            "自己长久以来埋藏在心底的感情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#023F#6P#3S！！！#2S\x02\x03",

            "姐姐……原来你对团长……\x02\x03",

            "#025F……原来……是这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#240F呵呵，他的年纪都能当我的父亲了，\x01",
            "所以你应该是无法想象的吧。\x02\x03",

            "所以……\x01",
            "他的想法也是一样。\x02\x03",

            "#244F虽然他把我当女儿一样地爱护，\x01",
            "但是不可能会接受我的感情。\x02\x03",

            "他劝我不要为一时的感情所困，\x01",
            "而应该去找一个合适的对象……\x02\x03",

            "#240F……对，他像说教一般地拒绝了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x103,
        "#522F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#244F#5P虽然遭到拒绝很受打击，\x01",
            "但对我来说，更为强烈的感觉却是恐惧。\x02\x03",

            "为了不让我继续迷恋他……\x01",
            "他竟然说要替我另寻良缘。\x02\x03",

            "#242F这时我已经完全意识到，\x01",
            "这个人可能很快就要从我身边离开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        "#023F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_34D6():
        OP_6B(3150, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34D6)

    ChrTalk(    #70
        0x8,
        (
            "#245F#5P……在我明白到这一点的一瞬间，\x01",
            "我的内心响起了一个声音。\x02\x03",

            "#244F……不要让他离开我……\x01",
            "要让他永远都属于我一个人……\x02\x03",

            "#241F于是我就顺从了那个声音……\x01",
            "向他出手了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x103,
        "#522F#6P……露茜奥拉……姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#240F#5P我就是从那时开始\x01",
            "才发现了自己内心的黑暗。\x02\x03",

            "之后，在黑暗的引导下，\x01",
            "……我接受了『噬身之蛇』的邀请……\x02\x03",

            "不知不觉之间……\x01",
            "就走到了今天这一步。\x02\x03",

            "#247F呵呵，或许已经到了该落幕的时候吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x103,
        "#023F#6P咦……\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrFlags(0x8, 0x40)

    def lambda_36A2():
        OP_6D(-5000, 0, 28000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36A2)

    def lambda_36BA():
        OP_67(0, 3470, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36BA)
    OP_8F(0x8, 0xFFFFE66A, 0x0, 0x7300, 0x3E8, 0x0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 17)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x103,
        "#024F#4S姐姐，不要！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x4)

    def lambda_3741():
        OP_6D(-6300, 0, 29440, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3741)

    def lambda_3759():
        OP_67(0, 4170, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3759)

    def lambda_3771():
        OP_8F(0xFE, 0xFFFFE43A, 0xFFFFFF4C, 0x75B2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3771)

    def lambda_378C():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_378C)

    def lambda_379C():
        OP_8E(0xFE, 0xFFFFE43A, 0xFFFFFF4C, 0x75B2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_379C)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(3000)
    OP_D2(0x270009, 0x27000D, 0x3)
    OP_D2(0x270019, 0x27001D, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F5")
    OP_D2(0x70055, 0x7005D, 0x5)
    Jump("loc_3894")

    label("loc_37F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3810")
    OP_D2(0x70035, 0x7003D, 0x5)
    Jump("loc_3894")

    label("loc_3810")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_382B")
    OP_D2(0x2703A1, 0x2703A5, 0x5)
    Jump("loc_3894")

    label("loc_382B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3846")
    OP_D2(0x70065, 0x7006D, 0x5)
    Jump("loc_3894")

    label("loc_3846")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3861")
    OP_D2(0x70075, 0x7007D, 0x5)
    Jump("loc_3894")

    label("loc_3861")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_387C")
    OP_D2(0x270089, 0x27008D, 0x5)
    Jump("loc_3894")

    label("loc_387C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3894")
    OP_D2(0x2700A3, 0x2700A7, 0x5)

    label("loc_3894")

    OP_D2(0x70025, 0x7002D, 0x6)
    OP_D2(0x2601C8, 0x2601CD, 0xB)
    OP_D2(0x2601CE, 0x2601D3, 0xC)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_6D(-8950, -8350, 31840, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(1480, 0)
    OP_6C(90000, 0)
    OP_6E(500, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 12)
    SetChrFlags(0x103, 0x2)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 11)
    SetChrPos(0x103, -8900, -1500, 31650, 0)
    SetChrPos(0x8, -9000, -6000, 32030, 0)

    def lambda_395C():

        label("loc_395C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_395C")

    QueueWorkItem2(0x8, 2, lambda_395C)
    FadeToBright(1000, 0)

    def lambda_3978():
        OP_6D(-8950, -3200, 31840, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3978)

    def lambda_3990():
        OP_67(0, 7000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3990)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #75
        0x103,
        "#522F#5P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#247F呵呵……你的鞭术\x01",
            "也大有进步呢。\x02\x03",

            "刚开始的时候\x01",
            "是那么地拙笨呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -2900, 0, 28690, 315)
    SetChrPos(0x102, -3920, 0, 27230, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4C")
    SetChrPos(0xF9, -2360, 0, 27210, 315)
    Jump("loc_3A5D")

    label("loc_3A4C")

    SetChrPos(0xF8, -2360, 0, 27210, 315)

    label("loc_3A5D")


    ChrTalk(    #77
        0x101,
        "#3P雪拉姐！\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_3A79():
        OP_6D(-8950, -3000, 31840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A79)

    def lambda_3A91():
        OP_67(0, 7800, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A91)
    OP_43(0x101, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x13)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD2")
    OP_43(0xF9, 0x1, 0x0, 0x14)
    Jump("loc_3AD9")

    label("loc_3AD2")

    OP_43(0xF8, 0x1, 0x0, 0x14)

    label("loc_3AD9")

    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)

    ChrTalk(    #78
        0x8,
        (
            "#242F艾丝蒂尔，约修亚……\x02\x03",

            "给我一点点时间就好……\x01",
            "就让我这样子再和这孩子说几句话吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1020F#3P可、可是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#1043F#4P露茜奥拉……你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x103,
        (
            "#523F#5P现、现在可不是\x01",
            "说话的时候吧！？\x02\x03",

            "抓紧了，我拉你上来！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BC9():
        OP_6B(1350, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BC9)

    ChrTalk(    #82
        0x8,
        (
            "#247F呵呵，雪拉扎德……\x02\x03",

            "直到现在，我都没有\x01",
            "后悔过对他下手……\x02\x03",

            "但我唯一不能释怀的，\x01",
            "就是从你的身边离开。\x02\x03",

            "在我离开后，你过得好不好…\x01",
            "这件事一直都是我心底的牵挂。\x02\x03",

            "#240F不过，即便没有我在你的身边，\x01",
            "你也仍然成长了不少呢，\x02\x03",

            "而且也找到了属于自己的道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x103,
        "#522F#5P姐姐……求求你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#246F只要能够确认到这一点，\x01",
            "我也就算没有白来利贝尔。\x02\x03",

            "其实，我本来是想让你亲手\x01",
            "对我的过错进行惩罚和制裁的…\x02\x03",

            "可是……\x01",
            "那果然只是我一厢情愿的想法罢了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #85
        0x103,
        (
            "#527F#5P……求求你！！\x01",
            "好好抓紧啊！！\x02",
        )
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#247F呵呵，喝酒我不反对……\x01",
            "……不过可要有节制哦。\x02\x03",

            "别了……我的雪拉扎德。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_3E36():
        OP_6B(1200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E36)
    OP_44(0x8, 0x2)
    SetChrSubChip(0x8, 32)

    def lambda_3E4F():
        OP_99(0xFE, 0x20, 0x2A, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E4F)
    Sleep(100)
    OP_22(0x226, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)

    def lambda_3E6E():
        OP_6D(-12950, -5000, 31840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E6E)

    def lambda_3E86():
        OP_67(0, 14000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E86)

    def lambda_3E9E():
        OP_6B(1000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E9E)
    SetChrFlags(0x8, 0x20)
    OP_43(0x8, 0x1, 0x0, 0x15)
    OP_99(0x8, 0x2A, 0x2F, 0x7D0)

    def lambda_3EC3():

        label("loc_3EC3")

        OP_99(0xFE, 0x30, 0x37, 0x7D0)
        OP_48()
        Jump("loc_3EC3")

    QueueWorkItem2(0x8, 3, lambda_3EC3)
    Sleep(1000)

    ChrTalk(    #87 op#A op#5
        0x103,
        "#20A#6P#4S露茜奥拉姐姐——！！！\x05\x02",
    )

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    Sleep(1000)
    SetChrFlags(0x8, 0x80)
    OP_22(0x11E, 0x0, 0x46)
    Sleep(3000)
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_6D(-5370, 0, 28490, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrChipByIndex(0x103, 6)
    SetChrPos(0x103, -6060, 0, 29160, 315)
    SetChrPos(0x101, -3810, 0, 26970, 315)
    SetChrPos(0x102, -4800, 0, 26550, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE6")
    SetChrPos(0xF9, -3310, 0, 27830, 315)
    Jump("loc_3FF7")

    label("loc_3FE6")

    SetChrPos(0xF8, -3310, 0, 27830, 315)

    label("loc_3FF7")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #88
        0x103,
        "#522F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1026F雪、雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#1043F#6P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x103,
        "#026F…………没事了………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x103, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x103, 135, 400)
    Sleep(500)

    ChrTalk(    #92
        0x103,
        (
            "#524F……姐姐她\x01",
            "一定不会这么容易就摔死的。\x02\x03",

            "总有一天，一定能……\x02\x03",

            "……一定能……再见面的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1025F嗯、嗯……一定会的！\x02\x03",

            "她会使用那么厉害的式神\x01",
            "和幻术呢！\x02\x03",

            "绝对……\x01",
            "……绝对没问题的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        (
            "#021F呵呵……是啊……\x02\x03",

            "#524F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41E4")

    ChrTalk(    #95
        0x104,
        (
            "#032F雪拉……\x01",
            "别太勉强了。\x02\x03",

            "还是先回埃尔赛尤吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C2")

    label("loc_41E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4231")

    ChrTalk(    #96
        0x106,
        (
            "#555F雪拉扎德……\x01",
            "别太勉强了。\x02\x03",

            "还是先回埃尔赛尤吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C2")

    label("loc_4231")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_427E")

    ChrTalk(    #97
        0x108,
        (
            "#572F雪拉扎德……\x01",
            "别太勉强了。\x02\x03",

            "还是先回埃尔赛尤吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C2")

    label("loc_427E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42C7")

    ChrTalk(    #98
        0x109,
        (
            "#1067F大姐……别太勉强了。\x02\x03",

            "还是先回埃尔赛尤吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C2")

    label("loc_42C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_431F")

    ChrTalk(    #99
        0x105,
        (
            "#1163F雪拉扎德小姐……\x01",
            "请不要太勉强自己。\x02\x03",

            "还是先回埃尔赛尤吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C2")

    label("loc_431F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4378")

    ChrTalk(    #100
        0x107,
        (
            "#063F那个，雪拉姐姐……\x01",
            "不要太勉强自己……\x02\x03",

            "还是先回埃尔赛尤吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C2")

    label("loc_4378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43C2")

    ChrTalk(    #101
        0x10B,
        (
            "#212F我说……\x01",
            "太勉强自己可不好哦？\x02\x03",

            "还是先回船上吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C2")


    ChrTalk(    #102
        0x103,
        (
            "#026F不……没那个必要。\x02\x03",

            "……如果这样就气馁的话，\x01",
            "姐姐会笑话我的……\x02\x03",

            "#020F所以，我们现在继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1004F雪拉姐……\x02\x03",

            "#1025F嗯……明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x102,
        (
            "#1035F#6P那么……\x01",
            "解除终端吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_6D(-2420, 0, 25750, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2420, 0, 25750, 0)
    SetChrPos(0x1, -2420, 0, 25750, 0)
    SetChrPos(0x2, -2420, 0, 25750, 0)
    SetChrPos(0x3, -2420, 0, 25750, 0)
    OP_1D(0x40)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x2238)
    OP_72(0x4, 0x4)
    OP_28(0x9F, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_16_2EB5 end

    def Function_17_4539(): pass

    label("Function_17_4539")


    def lambda_453F():
        OP_8E(0xFE, 0x352, 0x0, 0xFFFFBB54, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_453F)
    Sleep(40)

    def lambda_455F():
        OP_8E(0xFE, 0xFFFFFF24, 0x0, 0xFFFFBB72, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_455F)
    Sleep(100)

    def lambda_457F():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFB686, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_457F)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45BD")
    OP_8E(0xF9, 0xFFFFFCF4, 0x0, 0xFFFFB6D6, 0xBB8, 0x0)
    Jump("loc_45D1")

    label("loc_45BD")

    OP_8E(0xF8, 0xFFFFFCF4, 0x0, 0xFFFFB6D6, 0xBB8, 0x0)

    label("loc_45D1")

    Return()

    # Function_17_4539 end

    def Function_18_45D2(): pass

    label("Function_18_45D2")

    OP_8E(0xFE, 0xFFFFE03E, 0xFFFFFA24, 0x7EAE, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_18_45D2 end

    def Function_19_45F8(): pass

    label("Function_19_45F8")

    OP_8E(0xFE, 0xFFFFDD0A, 0xFFFFFA24, 0x7738, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 4)
    Return()

    # Function_19_45F8 end

    def Function_20_4617(): pass

    label("Function_20_4617")

    OP_8E(0xFE, 0xFFFFE1F6, 0xFFFFFA24, 0x7C1A, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 5)
    Return()

    # Function_20_4617 end

    def Function_21_463D(): pass

    label("Function_21_463D")


    def lambda_4643():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4643)
    Sleep(500)

    def lambda_4663():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4663)
    Sleep(500)

    def lambda_4683():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4683)
    Return()

    # Function_21_463D end

    def Function_22_4699(): pass

    label("Function_22_4699")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #105
        (
            "\x07\x05通往上层区域方向的隔离壁，\x01",
            "以及传送门的锁定解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5305   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_22_4699 end

    def Function_23_4707(): pass

    label("Function_23_4707")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_471E")
    Call(0, 25)
    Call(0, 26)

    label("loc_471E")

    OP_6D(-800, 0, 33180, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(327000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 700, 0, 31480, 0)
    SetChrPos(0x102, -170, 0, 31400, 0)
    SetChrPos(0xF8, 1210, 0, 29860, 0)
    SetChrPos(0xF9, 70, 0, 29750, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #106
        (
            "\x07\x05向上层区域方向的隔离壁，\x01",
            "以及传送门的锁定已经解除了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_71(0x2, 0x4)
    OP_0D()
    Sleep(500)
    OP_64(0x0, 0x1)
    OP_A2(0x2239)
    OP_28(0x9F, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_23_4707 end

    def Function_24_481E(): pass

    label("Function_24_481E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4835")
    Call(0, 25)
    Call(0, 26)

    label("loc_4835")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_484A")
    Call(0, 4)
    Jump("loc_484E")

    label("loc_484A")

    Call(0, 15)

    label("loc_484E")

    Return()

    # Function_24_481E end

    def Function_25_484F(): pass

    label("Function_25_484F")

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
        (0, "loc_48C9"),
        (1, "loc_48CF"),
        (SWITCH_DEFAULT, "loc_48D5"),
    )


    label("loc_48C9")

    OP_A2(0x1200)
    Jump("loc_48D5")

    label("loc_48CF")

    OP_A2(0x1201)
    Jump("loc_48D5")

    label("loc_48D5")

    Return()

    # Function_25_484F end

    def Function_26_48D6(): pass

    label("Function_26_48D6")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_26_48D6 end

    def Function_27_4969(): pass

    label("Function_27_4969")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_27_4969 end

    SaveToFile()

Try(main)
