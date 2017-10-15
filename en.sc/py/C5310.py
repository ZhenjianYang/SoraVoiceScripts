from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Luciola',                              # 9
        'Jubokko ',                             # 10
        'Zaqqum',                               # 11
        '残像',                                 # 12
        '残像',                                 # 13
        'Targeting Camera',                     # 14
        'Scherazard',                           # 15
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
        "Function_0_1AE",          # 00, 0
        "Function_1_20D",          # 01, 1
        "Function_2_288",          # 02, 2
        "Function_3_4F9",          # 03, 3
        "Function_4_792",          # 04, 4
        "Function_5_1259",         # 05, 5
        "Function_6_12DE",         # 06, 6
        "Function_7_1363",         # 07, 7
        "Function_8_1389",         # 08, 8
        "Function_9_13AF",         # 09, 9
        "Function_10_13D5",        # 0A, 10
        "Function_11_13FB",        # 0B, 11
        "Function_12_2214",        # 0C, 12
        "Function_13_2289",        # 0D, 13
        "Function_14_2339",        # 0E, 14
        "Function_15_23E9",        # 0F, 15
        "Function_16_3921",        # 10, 16
        "Function_17_560D",        # 11, 17
        "Function_18_56A6",        # 12, 18
        "Function_19_56CC",        # 13, 19
        "Function_20_56EB",        # 14, 20
        "Function_21_5711",        # 15, 21
        "Function_22_576D",        # 16, 22
        "Function_23_57E3",        # 17, 23
        "Function_24_58FE",        # 18, 24
        "Function_25_592F",        # 19, 25
        "Function_26_59B5",        # 1A, 26
        "Function_27_5A48",        # 1B, 27
    )


    def Function_0_1AE(): pass

    label("Function_0_1AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1BF")
    OP_A3(0x10F0)
    Event(0, 23)
    Jump("loc_20C")

    label("loc_1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9")
    Event(0, 24)
    Jump("loc_20C")

    label("loc_1E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203")
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_20C")

    label("loc_203")

    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_20C")

    Return()

    # Function_0_1AE end

    def Function_1_20D(): pass

    label("Function_1_20D")

    OP_22(0x1C3, 0x1, 0x64)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_END)), "loc_227")
    OP_64(0x0, 0x1)
    OP_71(0x2, 0x4)

    label("loc_227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_237")
    OP_72(0x4, 0x4)

    label("loc_237")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x462), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_265")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258")
    Call(0, 2)
    Jump("loc_265")

    label("loc_258")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 3)

    label("loc_265")

    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_20D end

    def Function_2_288(): pass

    label("Function_2_288")

    OP_D2(0x2701C8, 0x2701CD, 0x0)
    OP_D2(0x29017E, 0x290182, 0x1)
    OP_D2(0x9038E, 0x90392, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270111, 0x270121, 0x4)
    OP_D2(0x270130, 0x270140, 0x5)
    OP_D2(0x270131, 0x270141, 0x6)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_2FB"),
        (3, "loc_312"),
        (4, "loc_329"),
        (6, "loc_340"),
        (7, "loc_357"),
        (8, "loc_36E"),
        (10, "loc_385"),
        (14, "loc_39C"),
        (15, "loc_3B3"),
        (SWITCH_DEFAULT, "loc_3CA"),
    )


    label("loc_2FB")

    OP_D2(0x70218, 0x70224, 0x7)
    OP_D2(0x70219, 0x70225, 0x8)
    Jump("loc_3CA")

    label("loc_312")

    OP_D2(0x701E8, 0x701F4, 0x7)
    OP_D2(0x701E9, 0x701F5, 0x8)
    Jump("loc_3CA")

    label("loc_329")

    OP_D2(0x27036E, 0x27037B, 0x7)
    OP_D2(0x27036F, 0x27037C, 0x8)
    Jump("loc_3CA")

    label("loc_340")

    OP_D2(0x70230, 0x7023C, 0x7)
    OP_D2(0x70231, 0x7023D, 0x8)
    Jump("loc_3CA")

    label("loc_357")

    OP_D2(0x70248, 0x70254, 0x7)
    OP_D2(0x70249, 0x70255, 0x8)
    Jump("loc_3CA")

    label("loc_36E")

    OP_D2(0x270176, 0x270183, 0x7)
    OP_D2(0x270177, 0x270184, 0x8)
    Jump("loc_3CA")

    label("loc_385")

    OP_D2(0x702B4, 0x702BB, 0x7)
    OP_D2(0x702B5, 0x702BC, 0x8)
    Jump("loc_3CA")

    label("loc_39C")

    OP_D2(0x2702D6, 0x2702E0, 0x7)
    OP_D2(0x2702D7, 0x2702E1, 0x8)
    Jump("loc_3CA")

    label("loc_3B3")

    OP_D2(0x2702C2, 0x2702CC, 0x7)
    OP_D2(0x2702C3, 0x2702CD, 0x8)
    Jump("loc_3CA")

    label("loc_3CA")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_3F7"),
        (3, "loc_40E"),
        (4, "loc_425"),
        (6, "loc_43C"),
        (7, "loc_453"),
        (8, "loc_46A"),
        (10, "loc_481"),
        (14, "loc_498"),
        (15, "loc_4AF"),
        (SWITCH_DEFAULT, "loc_4C6"),
    )


    label("loc_3F7")

    OP_D2(0x70218, 0x70224, 0x9)
    OP_D2(0x70219, 0x70225, 0xA)
    Jump("loc_4C6")

    label("loc_40E")

    OP_D2(0x701E8, 0x701F4, 0x9)
    OP_D2(0x701E9, 0x701F5, 0xA)
    Jump("loc_4C6")

    label("loc_425")

    OP_D2(0x27036E, 0x27037B, 0x9)
    OP_D2(0x27036F, 0x27037C, 0xA)
    Jump("loc_4C6")

    label("loc_43C")

    OP_D2(0x70230, 0x7023C, 0x9)
    OP_D2(0x70231, 0x7023D, 0xA)
    Jump("loc_4C6")

    label("loc_453")

    OP_D2(0x70248, 0x70254, 0x9)
    OP_D2(0x70249, 0x70255, 0xA)
    Jump("loc_4C6")

    label("loc_46A")

    OP_D2(0x270176, 0x270183, 0x9)
    OP_D2(0x270177, 0x270184, 0xA)
    Jump("loc_4C6")

    label("loc_481")

    OP_D2(0x702B4, 0x702BB, 0x9)
    OP_D2(0x702B5, 0x702BC, 0xA)
    Jump("loc_4C6")

    label("loc_498")

    OP_D2(0x2702D6, 0x2702E0, 0x9)
    OP_D2(0x2702D7, 0x2702E1, 0xA)
    Jump("loc_4C6")

    label("loc_4AF")

    OP_D2(0x2702C2, 0x2702CC, 0x9)
    OP_D2(0x2702C3, 0x2702CD, 0xA)
    Jump("loc_4C6")

    label("loc_4C6")

    OP_D2(0x270256, 0x270260, 0xB)
    OP_D2(0x270257, 0x270261, 0xC)
    OP_D2(0x270258, 0x270262, 0xD)
    OP_D2(0x29017F, 0x290183, 0xE)
    OP_D2(0x9038F, 0x90393, 0xF)
    Return()

    # Function_2_288 end

    def Function_3_4F9(): pass

    label("Function_3_4F9")

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
        (5, "loc_580"),
        (3, "loc_597"),
        (4, "loc_5AE"),
        (6, "loc_5C5"),
        (7, "loc_5DC"),
        (8, "loc_5F3"),
        (10, "loc_60A"),
        (14, "loc_621"),
        (15, "loc_638"),
        (SWITCH_DEFAULT, "loc_64F"),
    )


    label("loc_580")

    OP_D2(0x70218, 0x70224, 0x9)
    OP_D2(0x70219, 0x70225, 0xA)
    Jump("loc_64F")

    label("loc_597")

    OP_D2(0x701E8, 0x701F4, 0x9)
    OP_D2(0x701E9, 0x701F5, 0xA)
    Jump("loc_64F")

    label("loc_5AE")

    OP_D2(0x27036E, 0x27037B, 0x9)
    OP_D2(0x27036F, 0x27037C, 0xA)
    Jump("loc_64F")

    label("loc_5C5")

    OP_D2(0x70230, 0x7023C, 0x9)
    OP_D2(0x70231, 0x7023D, 0xA)
    Jump("loc_64F")

    label("loc_5DC")

    OP_D2(0x70248, 0x70254, 0x9)
    OP_D2(0x70249, 0x70255, 0xA)
    Jump("loc_64F")

    label("loc_5F3")

    OP_D2(0x270176, 0x270183, 0x9)
    OP_D2(0x270177, 0x270184, 0xA)
    Jump("loc_64F")

    label("loc_60A")

    OP_D2(0x702B4, 0x702BB, 0x9)
    OP_D2(0x702B5, 0x702BC, 0xA)
    Jump("loc_64F")

    label("loc_621")

    OP_D2(0x2702D6, 0x2702E0, 0x9)
    OP_D2(0x2702D7, 0x2702E1, 0xA)
    Jump("loc_64F")

    label("loc_638")

    OP_D2(0x2702C2, 0x2702CC, 0x9)
    OP_D2(0x2702C3, 0x2702CD, 0xA)
    Jump("loc_64F")

    label("loc_64F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_67C"),
        (3, "loc_693"),
        (4, "loc_6AA"),
        (6, "loc_6C1"),
        (7, "loc_6D8"),
        (8, "loc_6EF"),
        (10, "loc_706"),
        (14, "loc_71D"),
        (15, "loc_734"),
        (SWITCH_DEFAULT, "loc_74B"),
    )


    label("loc_67C")

    OP_D2(0x70218, 0x70224, 0x9)
    OP_D2(0x70219, 0x70225, 0xA)
    Jump("loc_74B")

    label("loc_693")

    OP_D2(0x701E8, 0x701F4, 0x9)
    OP_D2(0x701E9, 0x701F5, 0xA)
    Jump("loc_74B")

    label("loc_6AA")

    OP_D2(0x27036E, 0x27037B, 0x9)
    OP_D2(0x27036F, 0x27037C, 0xA)
    Jump("loc_74B")

    label("loc_6C1")

    OP_D2(0x70230, 0x7023C, 0x9)
    OP_D2(0x70231, 0x7023D, 0xA)
    Jump("loc_74B")

    label("loc_6D8")

    OP_D2(0x70248, 0x70254, 0x9)
    OP_D2(0x70249, 0x70255, 0xA)
    Jump("loc_74B")

    label("loc_6EF")

    OP_D2(0x270176, 0x270183, 0x9)
    OP_D2(0x270177, 0x270184, 0xA)
    Jump("loc_74B")

    label("loc_706")

    OP_D2(0x702B4, 0x702BB, 0x9)
    OP_D2(0x702B5, 0x702BC, 0xA)
    Jump("loc_74B")

    label("loc_71D")

    OP_D2(0x2702D6, 0x2702E0, 0x9)
    OP_D2(0x2702D7, 0x2702E1, 0xA)
    Jump("loc_74B")

    label("loc_734")

    OP_D2(0x2702C2, 0x2702CC, 0x9)
    OP_D2(0x2702C3, 0x2702CD, 0xA)
    Jump("loc_74B")

    label("loc_74B")

    OP_D2(0x270256, 0x270260, 0xB)
    OP_D2(0x270257, 0x270261, 0xC)
    OP_D2(0x270258, 0x270262, 0xD)
    OP_D2(0x29017F, 0x290183, 0xE)
    OP_D2(0x9038F, 0x90393, 0xF)
    OP_D2(0x2601C6, 0x2601CB, 0x10)
    OP_D2(0x2601C7, 0x2601CC, 0x11)
    Return()

    # Function_3_4F9 end

    def Function_4_792(): pass

    label("Function_4_792")

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

    def lambda_810():
        OP_6B(3960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_810)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF9, 0x1)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 520, 0, 25630, 180)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #0
        0x8,
        "Woman's Voice",
        "Not quite who I was expecting.\x02",
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DE")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_91C")

    label("loc_8DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_905")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_91C")

    label("loc_905")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_91C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_948")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_986")

    label("loc_948")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_986")

    label("loc_96F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_986")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_998():
        OP_6D(-550, 0, 26000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_998)

    def lambda_9B0():
        OP_67(0, 4870, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B0)

    def lambda_9C8():
        OP_6B(3290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9C8)

    def lambda_9D8():
        OP_6E(288, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9D8)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x101, 1490, 0, 2610, 0)
    SetChrPos(0x102, 40, 0, 2660, 0)
    SetChrPos(0xF8, 1660, 0, 1390, 0)
    SetChrPos(0xF9, 260, 0, 1430, 0)

    ChrTalk(    #1
        0x101,
        "#1020F#2PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1042F#2PThe Bewitching Bell...\x01",
            "Hello, Luciola.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A78():
        OP_6D(-1500, 0, 22220, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A78)

    def lambda_A90():
        OP_67(0, 4210, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A90)

    def lambda_AA8():
        OP_6B(3400, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AA8)

    def lambda_AB8():
        OP_6E(292, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_AB8)
    Sleep(1000)

    def lambda_ACD():
        OP_8E(0xFE, 0x546, 0x0, 0x3FC9, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ACD)
    Sleep(80)

    def lambda_AED():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x40E2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AED)
    Sleep(100)

    def lambda_B0D():
        OP_8E(0xFE, 0x5BE, 0x0, 0x3A0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B0D)
    Sleep(40)
    OP_8E(0xF9, 0xFFFFFFD8, 0x0, 0x3980, 0x1770, 0x0)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #3
        0x8,
        (
            "#244FHow strange.\x01",
            "I was certain Scherazard would be here.\x02\x03",

            "#240FIt seems my fortune-telling still\x01",
            "needs some work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1002F#5PSchera's helping protect the Arseille.\x01",
            "Sorry to disappoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#1042F#5PDo you still intend to fight us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#244FHmm... Well, in truth, I don't owe the\x01",
            "professor anything at this point.\x01",
            "I could just walk away.\x02\x03",

            "#240FBut, to be honest, I didn't think you would\x01",
            "actually defeat Bleublanc and Walter\x01",
            "and make it this far.\x02\x03",

            "If I may be a little selfish...I'd like\x01",
            "to see how far you've come myself.\x02",
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

    def lambda_E54():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E54)
    LoadEffect(0x1, "scraft\\sc040_08.eff")
    PlayEffect(0x1, 0x0, 0xFF, 450, 0, 25660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x265, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_82(0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4F")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F8D")

    label("loc_F4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F76")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F8D")

    label("loc_F76")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F8D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FF7")

    label("loc_FB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE0")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FF7")

    label("loc_FE0")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_FF7")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101B")

    ChrTalk(    #7
        0x10F,
        "#178FBlast!\x02",
    )

    CloseMessageWindow()

    label("loc_101B")

    Sleep(300)
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

    ChrTalk(    #8
        0x8,
        (
            "#244F#6PAnd remember, if you can't defeat me,\x01",
            "you aren't possibly ready for the three\x01",
            "who await above.\x02\x03",

            "#241FShow me that you can break the\x01",
            "spell of the Bewitching Bell!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_111C():
        OP_6D(0, 0, 24000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_111C)

    def lambda_1134():
        OP_67(0, 4610, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1134)

    def lambda_114C():
        OP_6B(2600, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_114C)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 1)

    def lambda_1166():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1166)
    Sleep(30)
    SetChrChipByIndex(0x9, 15)
    SetChrFlags(0x9, 0x1000)

    def lambda_1190():
        OP_91(0xFE, 0x3E8, 0x0, 0xFFFFEC78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1190)

    def lambda_11AB():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11AB)
    Sleep(30)
    SetChrChipByIndex(0xA, 14)
    SetChrFlags(0xA, 0x1000)

    def lambda_11D5():
        OP_91(0xFE, 0xFFFFFC18, 0x0, 0xFFFFEC78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_11D5)

    def lambda_11F0():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_11F0)

    def lambda_120B():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_120B)
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

    # Function_4_792 end

    def Function_5_1259(): pass

    label("Function_5_1259")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 2)
    SetChrPos(0xFE, -2000, 2000, 26000, 180)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)

    def lambda_128A():

        label("loc_128A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_128A")

    QueueWorkItem2(0xFE, 3, lambda_128A)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_12A7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12A7)

    def lambda_12B9():
        OP_8F(0xFE, 0xFFFFF830, 0x1F4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12B9)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x21A, 0x0, 0x64)
    Return()

    # Function_5_1259 end

    def Function_6_12DE(): pass

    label("Function_6_12DE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 1)
    SetChrPos(0xFE, 2000, 2000, 26000, 180)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)

    def lambda_130F():

        label("loc_130F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_130F")

    QueueWorkItem2(0xFE, 3, lambda_130F)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_132C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_132C)

    def lambda_133E():
        OP_8F(0xFE, 0x7D0, 0x1F4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_133E)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x21A, 0x0, 0x64)
    Return()

    # Function_6_12DE end

    def Function_7_1363(): pass

    label("Function_7_1363")

    SetChrPos(0xFE, 870, 0, -25040, 0)
    OP_8E(0xFE, 0x366, 0x0, 0xFFFFB988, 0xBB8, 0x0)
    Return()

    # Function_7_1363 end

    def Function_8_1389(): pass

    label("Function_8_1389")

    SetChrPos(0xFE, -390, 0, -25050, 0)
    OP_8E(0xFE, 0xFFFFFE7A, 0x0, 0xFFFFB97E, 0xBB8, 0x0)
    Return()

    # Function_8_1389 end

    def Function_9_13AF(): pass

    label("Function_9_13AF")

    SetChrPos(0xFE, 1150, 0, -26400, 0)
    OP_8E(0xFE, 0x47E, 0x0, 0xFFFFB438, 0xBB8, 0x0)
    Return()

    # Function_9_13AF end

    def Function_10_13D5(): pass

    label("Function_10_13D5")

    SetChrPos(0xFE, -210, 0, -26410, 0)
    OP_8E(0xFE, 0xFFFFFF2E, 0x0, 0xFFFFB42E, 0xBB8, 0x0)
    Return()

    # Function_10_13D5 end

    def Function_11_13FB(): pass

    label("Function_11_13FB")

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

    ChrTalk(    #9
        0x8,
        (
            "#247FHeehee... I see.\x02\x03",

            "It seems you do have the right\x01",
            "to go farther up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1004F#5PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        "#1040F#5PLuciola... You'll withdraw, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "#240FYes. I don't really have a reason to remain.\x02",
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

    def lambda_15F3():
        OP_6D(-1400, 0, 24910, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15F3)

    def lambda_160B():
        OP_67(0, 4000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_160B)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1699")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16D7")

    label("loc_1699")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C0")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16D7")

    label("loc_16C0")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16D7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1703")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1741")

    label("loc_1703")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172A")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1741")

    label("loc_172A")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1741")

    Sleep(1000)

    ChrTalk(    #13
        0x101,
        (
            "#1020F#5PWait, hold on a sec!\x02\x03",

            "But what about you and...and Schera?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#247F#4PSchera, yes...\x01",
            "The karma between us remains uneven.\x02\x03",

            "#240FSo I'm certain fate will bring us\x01",
            "together again, someday.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x5A, 0x3E8)
    Sleep(500)

    ChrTalk(    #15
        0x8,
        (
            "#244F#4PAbove us are the three most dangerous\x01",
            "people you have ever met.\x02\x03",

            "Take care, because even one mistake\x01",
            "will cost you your life.\x02\x03",

            "#241FFarewell, then, my loves.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11E, 0x0, 0x64)

    def lambda_18D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18D8)

    def lambda_18EA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_18EA)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Sleep(500)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(    #16
        0x101,
        "#1026F#5PHey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#1035F#5PShe's gone.\x02",
    )

    CloseMessageWindow()

    def lambda_1950():
        OP_6D(-820, 0, 20460, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1950)

    def lambda_1968():
        OP_67(0, 4700, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1968)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A4F")

    ChrTalk(    #18
        0x10F,
        (
            "#176FPhew! It seems she was testing us.\x02\x03",

            "#170FIt is strange... She does not seem much like\x01",
            "the other Ouroboros members we've met.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1A4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AA7")

    ChrTalk(    #19
        0x108,
        (
            "#071F#1PGoodness. Not what you'd expect\x01",
            "from an Ouroboros member.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1AA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0B")

    ChrTalk(    #20
        0x104,
        (
            "#031F#5PHeh, it is easy to see where Schera\x01",
            "gets her sense of theatrics from.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1B0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B70")

    ChrTalk(    #21
        0x109,
        (
            "#1061F#5PMan, how to put it... She ain't quite\x01",
            "like those other goons, is she?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE0")

    ChrTalk(    #22
        0x106,
        (
            "#051F#5PHeh... Interesting woman. She's sort of an\x01",
            "odd one out for Ouroboros, you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1BE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3F")

    ChrTalk(    #23
        0x10B,
        (
            "#210F#5PHuh. She was kind of cool, actually.\x01",
            "Not like those other jerks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1C3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C97")

    ChrTalk(    #24
        0x105,
        (
            "#1168F#5PShe's so much more...gentle than\x01",
            "the others. I'm glad...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1C97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDD")

    ChrTalk(    #25
        0x107,
        (
            "#066FHeehee! She was kind of cool,\x01",
            "in her own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D51")

    ChrTalk(    #26
        0x110,
        (
            "#272FMmm... Even so, I imagine the Silver Streak\x01",
            "will be disappointed when she hears of this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207F")

    label("loc_1D51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB1")

    ChrTalk(    #27
        0x107,
        (
            "#561F#5PI think Schera might be a little sad\x01",
            "when she hears about this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207F")

    label("loc_1DB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1B")

    ChrTalk(    #28
        0x105,
        (
            "#1169F#5PI fear Scherazard will be disappointed\x01",
            "when she hears about this, however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207F")

    label("loc_1E1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E95")

    ChrTalk(    #29
        0x10B,
        (
            "#215F#5PEh, only problem is, that whip lady'll probably\x01",
            "be a bit sad when she hears Luciola's gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207F")

    label("loc_1E95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EFA")

    ChrTalk(    #30
        0x106,
        (
            "#551F#5PScherazard's gonna be sad she missed\x01",
            "Luciola when we tell her, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207F")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F5E")

    ChrTalk(    #31
        0x109,
        (
            "#1068FThink Ms. Schera's gonna be sad to\x01",
            "hear they missed each other, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207F")

    label("loc_1F5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2023")

    ChrTalk(    #32
        0x104,
        (
            "#34FMmm, but even so. I fear Scherazard\x01",
            "shall be disappointed to hear of this.\x02\x03",

            "#30FThe two of them share a connection,\x01",
            "and I feel Scherazard wished to settle\x01",
            "things as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207F")

    label("loc_2023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207F")

    ChrTalk(    #33
        0x108,
        (
            "#074FStill, I fear Scherazard will be dispirited\x01",
            "when she hears of this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207F")

    OP_8C(0x101, -180, 400)
    Sleep(300)

    ChrTalk(    #34
        0x101,
        (
            "#1007F#2PYeah...but I dunno, maybe it's for the best.\x02\x03",

            "#1015FI get the feeling the two of them meeting\x01",
            "would be kind of a problem, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)

    ChrTalk(    #35
        0x102,
        (
            "#1043F#6PYes... It's something for another day,\x01",
            "I think.\x02\x03",

            "#1035FRegardless, Luciola is gone, but our job\x01",
            "isn't done yet.\x02\x03",

            "#1040FWe should pay attention to her warning\x01",
            "and proceed carefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #36
        0x101,
        "#1006F#2PRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2237)
    OP_72(0x4, 0x4)
    OP_28(0x9F, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_11_13FB end

    def Function_12_2214(): pass

    label("Function_12_2214")


    def lambda_221A():
        OP_8E(0xFE, 0x352, 0x0, 0xFFFFBB54, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_221A)
    Sleep(40)

    def lambda_223A():
        OP_8E(0xFE, 0xFFFFFF24, 0x0, 0xFFFFBB72, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_223A)
    Sleep(100)

    def lambda_225A():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFB686, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_225A)
    Sleep(50)
    OP_8E(0xF9, 0xFFFFFCF4, 0x0, 0xFFFFB6D6, 0xBB8, 0x0)
    Return()

    # Function_12_2214 end

    def Function_13_2289(): pass

    label("Function_13_2289")

    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 12)
    SetChrPos(0xB, 520, 0, 26000, 180)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_91(0xB, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_2304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2338")
    OP_91(0xB, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_2304")

    label("loc_2338")

    Return()

    # Function_13_2289 end

    def Function_14_2339(): pass

    label("Function_14_2339")

    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xC, 12)
    SetChrPos(0xC, 520, 0, 26000, 180)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_91(0xC, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xC, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xC, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xC, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_23B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23E8")
    OP_91(0xC, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xC, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_23B4")

    label("loc_23E8")

    Return()

    # Function_14_2339 end

    def Function_15_23E9(): pass

    label("Function_15_23E9")

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

    def lambda_2467():
        OP_6B(3960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2467)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24ED")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_252B")

    label("loc_24ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2514")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_252B")

    label("loc_2514")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_252B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2557")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2595")

    label("loc_2557")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2595")

    label("loc_257E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2595")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25CA")

    ChrTalk(    #37
        0x10F,
        "#172FThe sound of a bell...?\x02",
    )

    CloseMessageWindow()

    label("loc_25CA")

    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 0, 0, 25630, 180)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #38
        0x8,
        "Woman's Voice",
        "Welcome.\x02",
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_21()
    OP_1D(0x6F)
    Sleep(500)

    def lambda_2614():
        OP_6D(-550, 0, 26000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2614)

    def lambda_262C():
        OP_67(0, 4870, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_262C)

    def lambda_2644():
        OP_6B(3290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2644)

    def lambda_2654():
        OP_6E(288, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2654)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x103, 330, 0, 350, 0)
    SetChrPos(0x101, 1300, 0, -1380, 0)
    SetChrPos(0x102, -100, 0, -1070, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B7")
    SetChrPos(0xF9, 920, 0, -3120, 0)
    Jump("loc_26C8")

    label("loc_26B7")

    SetChrPos(0xF8, 920, 0, -3120, 0)

    label("loc_26C8")


    ChrTalk(    #39
        0x101,
        "#1020F#2PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#1042F#2PThe Bewitching Bell...\x01",
            "Hello, Luciola.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2715():
        OP_6D(-1300, 0, 22700, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2715)

    def lambda_272D():
        OP_67(0, 4210, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_272D)

    def lambda_2745():
        OP_6B(3480, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2745)

    def lambda_2755():
        OP_6E(292, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2755)
    Sleep(1000)

    def lambda_276A():
        OP_8E(0xFE, 0x64, 0x0, 0x424A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_276A)
    Sleep(80)

    def lambda_278A():
        OP_8E(0xFE, 0x7D0, 0x0, 0x3E80, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_278A)
    Sleep(150)

    def lambda_27AA():
        OP_8E(0xFE, 0xFFFFFF38, 0x0, 0x3E1C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27AA)
    Sleep(40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E8")
    OP_8E(0xF9, 0x532, 0x0, 0x3A98, 0x1770, 0x0)
    Jump("loc_27FC")

    label("loc_27E8")

    OP_8E(0xF8, 0x532, 0x0, 0x3A98, 0x1770, 0x0)

    label("loc_27FC")

    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #41
        0x103,
        "#522F#5PLuci.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#244FYou actually got past Bleublanc and Walter.\x01",
            "I honestly didn't think you could.\x02\x03",

            "#240FWell done, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        (
            "#026F#5PLuci, please keep your promise.\x02\x03",

            "#022FYou said you'd explain what you said\x01",
            "about Mr. Harvey when we met next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        "#241FAh, yes. The reason I killed him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x103,
        "#522F#5PNgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#244FSo I did...\x02\x03",

            "...\x02\x03",

            "#240FHm. Scherazard, let me begin with\x01",
            "a question.\x02\x03",

            "What kind of man was Harvey to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        (
            "#024F#5PWh-What sort of question is that?!\x02\x03",

            "I owed him my life for rescuing me from\x01",
            "the streets! He was everything to me!\x02",
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

    ChrTalk(    #48
        0x103,
        (
            "#524F#5PI never knew my 'true' parents.\x02\x03",

            "I always imagined, however, that my father\x01",
            "would have to be someone like Harvey...\x02\x03",

            "#527FSo...how?! HOW could you--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#244FYes... He was a kind, warm, gentle soul.\x02\x03",

            "#242FBut you see...a circus cannot be\x01",
            "kindness alone. Purely performing\x01",
            "simply doesn't bring in enough mira.\x02\x03",

            "That income needs to be supplemented,\x01",
            "be it with dirty deals or having performers \x01",
            "engage in...other lines of work.\x02\x03",

            "#244FBut Harvey... Harvey insisted on keeping\x01",
            "us going with honest money.\x02\x03",

            "So, instead, he dipped into his private funds,\x01",
            "and then took on tremendous debt just to keep\x01",
            "us going.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x103,
        (
            "#024F#5PWhat?!\x02\x03",

            "But, I mean, Harvey never said anything\x01",
            "about that or acted like it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#240FDespite his kind exterior,\x01",
            "he had a will of iron.\x02\x03",

            "He ran up his debts here, there,\x01",
            "and all across the continent...\x02\x03",

            "#244FAnd in the end, he decided to leave\x01",
            "the troupe to save us from it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#023F#5PBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#244FHis plan was to entrust the entire troupe\x01",
            "to a wealthy acquaintance of his.\x02\x03",

            "If he remained troupe leader, it would only\x01",
            "invite trouble for us as people came to\x01",
            "collect his debts...\x02\x03",

            "In that case, it would be better to have\x01",
            "someone he trusted watching over us...\x02\x03",

            "#240FThat was how he explained it to me,\x01",
            "that day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        (
            "#522F#5PBut, no, but...why?\x02\x03",

            "#024FIf he'd just told us, we could\x01",
            "have helped him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#242FOh, when he told me, I tried to\x01",
            "convince him to stay.\x02\x03",

            "But he was...Harvey. Kind as he could be,\x01",
            "he was also stubborn as a mule.\x02\x03",

            "#244FI still remember exactly what he told me.\x02\x03",

            "'It's bad for a coward like me to stay\x01",
            "with good people like all of you.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        (
            "#025F#5P...\x02\x03",

            "#522FSo that's why you...you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "#240FYes, precisely.\x02\x03",

            "When he told me, I felt completely betrayed.\x02\x03",

            "#244FHe gave us peace and happiness, and\x01",
            "then he was going to leave us in the\x01",
            "hands of someone we didn't know?\x02\x03",

            "'If he's going to do that,' I thought, 'I wish\x01",
            "he'd never given us his hand in the first place!'\x02\x03",

            "#241FAnd so...I killed him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x103,
        (
            "#522F#5P...\x02\x03",

            "Then...what about me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "#243FWhat about... Ah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x103,
        (
            "#524F#5PYou and Harvey were the ones who\x01",
            "gave ME peace and happiness, Luci.\x02\x03",

            "You filled me with a warmth I never knew,\x01",
            "living in the slums.\x02\x03",

            "#025FBut...Harvey died, and then you disappeared...\x02\x03",

            "#527FThat... That's an even worse betrayal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#247F...Yes. So it is.\x02\x03",

            "#242FScherazard.\x01",
            "You have every right to hate me.\x02\x03",

            "Wield your hate, and stand against me.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34EF")
    SetChrPos(0xF9, 0, 0, 15040, 0)
    Jump("loc_3500")

    label("loc_34EF")

    SetChrPos(0xF8, 0, 0, 15040, 0)

    label("loc_3500")

    OP_0D()

    def lambda_3507():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3507)
    LoadEffect(0x1, "scraft\\sc040_08.eff")
    PlayEffect(0x1, 0x0, 0xFF, 450, 0, 25660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x265, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_82(0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362B")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3669")

    label("loc_362B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3652")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3669")

    label("loc_3652")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3669")

    Jump("loc_36D1")

    label("loc_366C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3693")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_36D1")

    label("loc_3693")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36BA")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_36D1")

    label("loc_36BA")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_36D1")

    Sleep(1000)

    ChrTalk(    #62
        0x103,
        "#523F#5PLuci...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#244F#6PIf nothing else...if you cannot defeat me,\x01",
            "you have no hope against the three who\x01",
            "await above.\x02\x03",

            "#241FShow me, now, that you can break\x01",
            "the spell of the Bewitching Bell!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    SetChrChipByIndex(0x103, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D3")
    SetChrChipByIndex(0xF9, 9)
    Jump("loc_37D8")

    label("loc_37D3")

    SetChrChipByIndex(0xF8, 9)

    label("loc_37D8")

    OP_0D()
    Sleep(500)

    def lambda_37E4():
        OP_6D(0, 0, 24000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37E4)

    def lambda_37FC():
        OP_67(0, 4610, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37FC)

    def lambda_3814():
        OP_6B(2600, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3814)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 1)

    def lambda_382E():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_382E)
    Sleep(30)
    SetChrChipByIndex(0x9, 15)
    SetChrFlags(0x9, 0x1000)

    def lambda_3858():
        OP_91(0xFE, 0x3E8, 0x0, 0xFFFFEC78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3858)

    def lambda_3873():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3873)
    Sleep(30)
    SetChrChipByIndex(0xA, 14)
    SetChrFlags(0xA, 0x1000)

    def lambda_389D():
        OP_91(0xFE, 0xFFFFFC18, 0x0, 0xFFFFEC78, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_389D)

    def lambda_38B8():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_38B8)

    def lambda_38D3():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_38D3)
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

    # Function_15_23E9 end

    def Function_16_3921(): pass

    label("Function_16_3921")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FA")
    SetChrPos(0xF9, 2020, 0, 21130, 315)
    Jump("loc_3A0B")

    label("loc_39FA")

    SetChrPos(0xF8, 2020, 0, 21130, 315)

    label("loc_3A0B")

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

    ChrTalk(    #64
        0x8,
        (
            "#247F#6PHeehee... I see.\x02\x03",

            "#240FYou do, I think, have a right\x01",
            "to go farther up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#025F#5P...Luci. I need to correct you on something.\x02\x03",

            "#524FDespite everything, I could never hate you.\x02\x03",

            "Even the fact that you left me,\x01",
            "or even this idea that you killed Harvey...\x02\x03",

            "#522FIt doesn't anger me, it just...breaks my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1026F#2PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "#243F#6PScherazard...you don't...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x103,
        (
            "#025F#5PBut...I just can't believe it, you know?\x02\x03",

            "#522FThat you'd kill Harvey over something\x01",
            "like that...\x02\x03",

            "Even if it was a bad decision, it must\x01",
            "have been hard for him, and he was\x01",
            "only trying to look out for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#240F#6P...\x02\x03",

            "#247FTeehee. I suppose I can't\x01",
            "really hide it, can I?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #70
        0x103,
        "#022F#5PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#240F#6PThere's...a little more to that story.\x02\x03",

            "As I said, Harvey was being a bit of a\x01",
            "mule, as he could be. Stubborn and\x01",
            "refusing to listen to my arguments...\x02\x03",

            "#244FSo to try and persuade him, I...\x01",
            "confessed something I'd felt but\x01",
            "kept secret for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#023F#5P#3SWH-WHAT?!#2S\x02\x03",

            "Luci, you...and Harvey...?\x02\x03",

            "#025FI... I...see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#240FYes, I imagine it's quite a\x01",
            "shock to you. You always saw him as\x01",
            "a father figure to the both of us.\x02\x03",

            "And...therein lay the problem.\x01",
            "So did he.\x02\x03",

            "#244FHe saw me as a daughter, and cared for me\x01",
            "deeply as one. There was no way he could\x01",
            "return my feelings.\x02\x03",

            "'Don't get carried away in the moment.\x01",
            "Find someone who suits you...'\x02\x03",

            "#240FAll these years later, I still remember\x01",
            "exactly how he refused me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        "#522F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#244F#6PThe refusal shocked me, of course, but\x01",
            "even more than that, it...scared me.\x02\x03",

            "I feared that now he knew how I felt,\x01",
            "he would do what he could to make sure\x01",
            "I 'found someone who suited me.'\x02\x03",

            "#242FThat he would leave me behind forever,\x01",
            "and we would never see one another again.\x01",
            "That I would have no choice but to 'move on'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        "#023F#5PBut...\x02",
    )

    CloseMessageWindow()

    def lambda_416A():
        OP_6B(3150, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_416A)

    ChrTalk(    #77
        0x8,
        (
            "#245F#6PThe moment I realized that was a possibility,\x01",
            "something within me...snapped.\x02\x03",

            "#244FSo that he could never 'leave' me...\x01",
            "so that he'd be mine forever...\x02\x03",

            "#241FI gave in to the urges...and took\x01",
            "his life with my own hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x103,
        "#522F#5PLuci...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#240F#6PThat was the very moment I realized\x01",
            "the darkness inside of me.\x02\x03",

            "And, eventually, Ouroboros and the Grandmaster\x01",
            "found me, and gave my inner darkness a\x01",
            "purpose.\x02\x03",

            "And eventually, the path they\x01",
            "set me on led me here.\x02\x03",

            "#247FNow I suppose...it leads to the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        "#023F#5PWh--\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)

    def lambda_439C():
        OP_6D(-5000, 0, 28000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_439C)

    def lambda_43B4():
        OP_67(0, 3470, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43B4)
    OP_8F(0x8, 0xFFFFE66A, 0x0, 0x7300, 0x3E8, 0x0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 17)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x103,
        "#024F#4SLUCI, NO!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x4)

    def lambda_4446():
        OP_6D(-6300, 0, 29440, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4446)

    def lambda_445E():
        OP_67(0, 4170, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_445E)

    def lambda_4476():
        OP_8F(0xFE, 0xFFFFE43A, 0xFFFFFF4C, 0x75B2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4476)

    def lambda_4491():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4491)

    def lambda_44A1():
        OP_8E(0xFE, 0xFFFFE43A, 0xFFFFFF4C, 0x75B2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_44A1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(3000)
    OP_D2(0x270009, 0x27000D, 0x3)
    OP_D2(0x270019, 0x27001D, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44FA")
    OP_D2(0x70055, 0x7005D, 0x5)
    Jump("loc_45CF")

    label("loc_44FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4515")
    OP_D2(0x70035, 0x7003D, 0x5)
    Jump("loc_45CF")

    label("loc_4515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4530")
    OP_D2(0x2703A1, 0x2703A5, 0x5)
    Jump("loc_45CF")

    label("loc_4530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_454B")
    OP_D2(0x70065, 0x7006D, 0x5)
    Jump("loc_45CF")

    label("loc_454B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4566")
    OP_D2(0x70075, 0x7007D, 0x5)
    Jump("loc_45CF")

    label("loc_4566")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4581")
    OP_D2(0x270089, 0x27008D, 0x5)
    Jump("loc_45CF")

    label("loc_4581")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_459C")
    OP_D2(0x2700A3, 0x2700A7, 0x5)
    Jump("loc_45CF")

    label("loc_459C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45B7")
    OP_D2(0x270448, 0x27044A, 0x5)
    Jump("loc_45CF")

    label("loc_45B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45CF")
    OP_D2(0x2702C6, 0x2702D0, 0x5)

    label("loc_45CF")

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

    def lambda_4697():

        label("loc_4697")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4697")

    QueueWorkItem2(0x8, 2, lambda_4697)
    SetChrPos(0xE, -8900, -2100, 31650, 0)
    FadeToBright(1000, 0)

    def lambda_46C4():
        OP_6D(-8950, -3200, 31840, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46C4)

    def lambda_46DC():
        OP_67(0, 7000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_46DC)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #82
        0xE,
        "#522F#4PGh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "#247FAhhh...\x01",
            "Your skill with a whip's certainly improved.\x02\x03",

            "You were so clumsy with it\x01",
            "when you started.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -2900, 0, 28690, 315)
    SetChrPos(0x102, -3920, 0, 27230, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47B9")
    SetChrPos(0xF9, -2360, 0, 27210, 315)
    Jump("loc_47CA")

    label("loc_47B9")

    SetChrPos(0xF8, -2360, 0, 27210, 315)

    label("loc_47CA")


    ChrTalk(    #84
        0x101,
        "#3PSCHERA!\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_47E5():
        OP_6D(-8950, -3000, 31840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_47E5)

    def lambda_47FD():
        OP_67(0, 7800, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47FD)
    OP_43(0x101, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x13)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_483E")
    OP_43(0xF9, 0x1, 0x0, 0x14)
    Jump("loc_4845")

    label("loc_483E")

    OP_43(0xF8, 0x1, 0x0, 0x14)

    label("loc_4845")

    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)

    ChrTalk(    #85
        0x8,
        (
            "#242FEstelle, Joshua...\x02\x03",

            "I only need a moment to speak\x01",
            "with her, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        "#1020F#3PBut, but!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        "#1043F#4PLuciola...you really...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xE,
        (
            "#523F#4PDoes this look like a time to be talking?!\x02\x03",

            "I'll pull you up! Just hold on!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_494A():
        OP_6B(1350, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_494A)

    ChrTalk(    #89
        0x8,
        (
            "#247FScherazard...listen.\x02\x03",

            "Even to this day, I don't actually regret\x01",
            "killing him.\x02\x03",

            "But leaving you...leaving you was the worst\x01",
            "thing I've ever done. I never forgave myself\x01",
            "for it.\x02\x03",

            "I was always so afraid for what happened to\x01",
            "that little girl I rescued from the streets...\x02\x03",

            "#240FBut you've turned out better than either\x01",
            "Harvey or I could have ever hoped for.\x02\x03",

            "You've found your way. And you're greater\x01",
            "than either of us ever were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xE,
        "#522F#4PLuci...please, I'm begging you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#246FJust finding that out has made coming\x01",
            "to Liberl worth it.\x02\x03",

            "Honestly, part of me wanted you to sit\x01",
            "in judgment over me...\x02\x03",

            "Hmm...\x01",
            "A little greedy of me, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #92
        0xE,
        "#527F#4PPlease, just HOLD ON!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#247FOh, and Schera, dear, remember: liquor is nice,\x01",
            "but do try to moderate yourself, all right?\x01",
            "Heehee...\x02\x03",

            "Goodbye...my darling little Schera.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_4CC5():
        OP_6B(1200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CC5)
    OP_44(0x8, 0x2)
    SetChrSubChip(0x8, 32)

    def lambda_4CDE():
        OP_99(0xFE, 0x20, 0x2A, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CDE)
    Sleep(100)
    OP_22(0x226, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)

    def lambda_4CFD():
        OP_6D(-12950, -5000, 31840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4CFD)

    def lambda_4D15():
        OP_67(0, 14000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D15)

    def lambda_4D2D():
        OP_6B(1000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D2D)
    SetChrFlags(0x8, 0x20)
    OP_43(0x8, 0x1, 0x0, 0x15)
    OP_99(0x8, 0x2A, 0x2F, 0x7D0)

    def lambda_4D52():

        label("loc_4D52")

        OP_99(0xFE, 0x30, 0x37, 0x7D0)
        OP_48()
        Jump("loc_4D52")

    QueueWorkItem2(0x8, 3, lambda_4D52)
    Sleep(1000)

    ChrTalk(    #94 op#A op#5
        0x103,
        "#20A#6P#4SLUCIOLAAAAAAAAAaaaaa...!\x05\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E77")
    SetChrPos(0xF9, -3310, 0, 27830, 315)
    Jump("loc_4E88")

    label("loc_4E77")

    SetChrPos(0xF8, -3310, 0, 27830, 315)

    label("loc_4E88")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #95
        0x103,
        "#522F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1026FSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#1043F#5POh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x103,
        "#026F...It's all right.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x103, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x103, 135, 400)
    Sleep(500)

    ChrTalk(    #99
        0x103,
        (
            "#524FLuci...always did love her theatrics. She'd never\x01",
            "take a fall...she couldn't recover from.\x02\x03",

            "I'm sure that, someday...\x02\x03",

            "Someday, we'll meet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1025FUmm... Yeah, totally!\x02\x03",

            "I mean, she can use that crazy paper\x01",
            "magic or whatever, and didn't I see her,\x01",
            "like, teleport or something?\x02\x03",

            "Yeah! I'm sure she'll be okay! Yeah...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x103,
        (
            "#021FYes...\x02\x03",

            "#524F...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50E3")

    ChrTalk(    #102
        0x104,
        (
            "#032FSchera...do not force yourself.\x02\x03",

            "Perhaps you should return to the Arseille for--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5475")

    label("loc_50E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5158")

    ChrTalk(    #103
        0x106,
        (
            "#555FScherazard...don't force yourself, all right?\x02\x03",

            "You can head back to the Arseille if you--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5475")

    label("loc_5158")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51C9")

    ChrTalk(    #104
        0x108,
        (
            "#572FScherazard...do not force yourself.\x02\x03",

            "You should head back to the Arseille,\x01",
            "perhaps...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5475")

    label("loc_51C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5249")

    ChrTalk(    #105
        0x109,
        (
            "#1067FHey, don't force yourself to keep goin',\x01",
            "okay?\x02\x03",

            "Nobody would complain if you want to\x01",
            "head back to--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5475")

    label("loc_5249")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52CD")

    ChrTalk(    #106
        0x105,
        (
            "#1163FScherazard, please, don't force\x01",
            "yourself to keep going.\x02\x03",

            "Perhaps you should return to the Arseille so--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5475")

    label("loc_52CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_534E")

    ChrTalk(    #107
        0x107,
        (
            "#063FUm, Schera...you don't need to come with us\x01",
            "still.\x02\x03",

            "It's okay if you wanna go back to the Arseille...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5475")

    label("loc_534E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53AD")

    ChrTalk(    #108
        0x10F,
        (
            "#175FScherazard...\x02\x03",

            "If you feel the need to return\x01",
            "to the Arseille, we--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5475")

    label("loc_53AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_540D")

    ChrTalk(    #109
        0x10B,
        (
            "#212FHey, don't force it, okay?\x02\x03",

            "You're wiped out, you should\x01",
            "head back--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5475")

    label("loc_540D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5475")

    ChrTalk(    #110
        0x110,
        (
            "#276FDo not force yourself to continue.\x02\x03",

            "You should return to the Arseille,\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5475")


    ChrTalk(    #111
        0x103,
        (
            "#026FNo. There's no need.\x02\x03",

            "Luciola would simply laugh at me\x01",
            "if I gave up here.\x02\x03",

            "#020FLet's keep going for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1004FSchera...\x02\x03",

            "#1025FYeah...let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        "#1035F#5PWell, then. We have a terminal to deal with.\x02",
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

    # Function_16_3921 end

    def Function_17_560D(): pass

    label("Function_17_560D")


    def lambda_5613():
        OP_8E(0xFE, 0x352, 0x0, 0xFFFFBB54, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5613)
    Sleep(40)

    def lambda_5633():
        OP_8E(0xFE, 0xFFFFFF24, 0x0, 0xFFFFBB72, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5633)
    Sleep(100)

    def lambda_5653():
        OP_8E(0xFE, 0x4F6, 0x0, 0xFFFFB686, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5653)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5691")
    OP_8E(0xF9, 0xFFFFFCF4, 0x0, 0xFFFFB6D6, 0xBB8, 0x0)
    Jump("loc_56A5")

    label("loc_5691")

    OP_8E(0xF8, 0xFFFFFCF4, 0x0, 0xFFFFB6D6, 0xBB8, 0x0)

    label("loc_56A5")

    Return()

    # Function_17_560D end

    def Function_18_56A6(): pass

    label("Function_18_56A6")

    OP_8E(0xFE, 0xFFFFE03E, 0xFFFFFA24, 0x7EAE, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_18_56A6 end

    def Function_19_56CC(): pass

    label("Function_19_56CC")

    OP_8E(0xFE, 0xFFFFDD0A, 0xFFFFFA24, 0x7738, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 4)
    Return()

    # Function_19_56CC end

    def Function_20_56EB(): pass

    label("Function_20_56EB")

    OP_8E(0xFE, 0xFFFFE1F6, 0xFFFFFA24, 0x7C1A, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 5)
    Return()

    # Function_20_56EB end

    def Function_21_5711(): pass

    label("Function_21_5711")


    def lambda_5717():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5717)
    Sleep(500)

    def lambda_5737():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5737)
    Sleep(500)

    def lambda_5757():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5757)
    Return()

    # Function_21_5711 end

    def Function_22_576D(): pass

    label("Function_22_576D")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #114
        "\x07\x05Barrier to upper levels and transport gate now unlocked.\x02",
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

    # Function_22_576D end

    def Function_23_57E3(): pass

    label("Function_23_57E3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57FA")
    Call(0, 25)
    Call(0, 26)

    label("loc_57FA")

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
    SetChrName("Voice")

    AnonymousTalk(    #115
        "\x07\x05Barrier to upper levels and transport gate now unlocked.\x02",
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

    # Function_23_57E3 end

    def Function_24_58FE(): pass

    label("Function_24_58FE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5915")
    Call(0, 25)
    Call(0, 26)

    label("loc_5915")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_592A")
    Call(0, 4)
    Jump("loc_592E")

    label("loc_592A")

    Call(0, 15)

    label("loc_592E")

    Return()

    # Function_24_58FE end

    def Function_25_592F(): pass

    label("Function_25_592F")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_59A8"),
        (1, "loc_59AE"),
        (SWITCH_DEFAULT, "loc_59B4"),
    )


    label("loc_59A8")

    OP_A2(0x1200)
    Jump("loc_59B4")

    label("loc_59AE")

    OP_A2(0x1201)
    Jump("loc_59B4")

    label("loc_59B4")

    Return()

    # Function_25_592F end

    def Function_26_59B5(): pass

    label("Function_26_59B5")

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

    # Function_26_59B5 end

    def Function_27_5A48(): pass

    label("Function_27_5A48")

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

    # Function_27_5A48 end

    SaveToFile()

Try(main)
