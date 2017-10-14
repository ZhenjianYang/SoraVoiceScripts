from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5311   ._SN',
        MapName             = 'Other',
        Location            = 'C5311.x',
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
        'Renne',                                # 9
        'Pater-Mater',                          # 10
        'Targeting Camera',                     # 11
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
        TriggerX            = -32500,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = -32500,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_12E",          # 00, 0
        "Function_1_177",          # 01, 1
        "Function_2_1B8",          # 02, 2
        "Function_3_469",          # 03, 3
        "Function_4_472",          # 04, 4
        "Function_5_1D66",         # 05, 5
        "Function_6_39AD",         # 06, 6
        "Function_7_3A2E",         # 07, 7
        "Function_8_3AA3",         # 08, 8
        "Function_9_3AC9",         # 09, 9
        "Function_10_3AEF",        # 0A, 10
        "Function_11_3B15",        # 0B, 11
        "Function_12_4240",        # 0C, 12
        "Function_13_42B6",        # 0D, 13
        "Function_14_43D1",        # 0E, 14
        "Function_15_4457",        # 0F, 15
    )


    def Function_0_12E(): pass

    label("Function_0_12E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_148")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 11)
    Jump("loc_176")

    label("loc_148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_159")
    OP_A3(0x10F1)
    Event(0, 13)
    Jump("loc_176")

    label("loc_159")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_176")

    Return()

    # Function_0_12E end

    def Function_1_177(): pass

    label("Function_1_177")

    OP_22(0x1C3, 0x1, 0x64)
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_END)), "loc_191")
    OP_64(0x0, 0x1)
    OP_71(0x2, 0x4)

    label("loc_191")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x463), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AE")

    Call(0, 2)
    OP_72(0x0, 0x4)

    label("loc_1B7")

    Return()

    # Function_1_177 end

    def Function_2_1B8(): pass

    label("Function_2_1B8")

    OP_D2(0x2701C7, 0x2701CC, 0x0)
    OP_D2(0x270110, 0x270120, 0x1)
    OP_D2(0x270111, 0x270121, 0x2)
    OP_D2(0x270130, 0x270140, 0x3)
    OP_D2(0x270131, 0x270141, 0x4)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_21B"),
        (5, "loc_232"),
        (3, "loc_249"),
        (4, "loc_260"),
        (6, "loc_277"),
        (7, "loc_28E"),
        (8, "loc_2A5"),
        (10, "loc_2BC"),
        (14, "loc_2D3"),
        (15, "loc_2EA"),
        (SWITCH_DEFAULT, "loc_301"),
    )


    label("loc_21B")

    OP_D2(0x701D0, 0x701DC, 0x5)
    OP_D2(0x701D1, 0x701DD, 0x6)
    Jump("loc_301")

    label("loc_232")

    OP_D2(0x70218, 0x70224, 0x5)
    OP_D2(0x70219, 0x70225, 0x6)
    Jump("loc_301")

    label("loc_249")

    OP_D2(0x701E8, 0x701F4, 0x5)
    OP_D2(0x701E9, 0x701F5, 0x6)
    Jump("loc_301")

    label("loc_260")

    OP_D2(0x27036E, 0x27037B, 0x5)
    OP_D2(0x27036F, 0x27037C, 0x6)
    Jump("loc_301")

    label("loc_277")

    OP_D2(0x70230, 0x7023C, 0x5)
    OP_D2(0x70231, 0x7023D, 0x6)
    Jump("loc_301")

    label("loc_28E")

    OP_D2(0x70248, 0x70254, 0x5)
    OP_D2(0x70249, 0x70255, 0x6)
    Jump("loc_301")

    label("loc_2A5")

    OP_D2(0x270176, 0x270183, 0x5)
    OP_D2(0x270177, 0x270184, 0x6)
    Jump("loc_301")

    label("loc_2BC")

    OP_D2(0x702B4, 0x702BB, 0x5)
    OP_D2(0x702B5, 0x702BC, 0x6)
    Jump("loc_301")

    label("loc_2D3")

    OP_D2(0x2702D6, 0x2702E0, 0x5)
    OP_D2(0x2702D7, 0x2702E1, 0x6)
    Jump("loc_301")

    label("loc_2EA")

    OP_D2(0x2702C2, 0x2702CC, 0x5)
    OP_D2(0x2702C3, 0x2702CD, 0x6)
    Jump("loc_301")

    label("loc_301")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_332"),
        (5, "loc_349"),
        (3, "loc_360"),
        (4, "loc_377"),
        (6, "loc_38E"),
        (7, "loc_3A5"),
        (8, "loc_3BC"),
        (10, "loc_3D3"),
        (14, "loc_3EA"),
        (15, "loc_401"),
        (SWITCH_DEFAULT, "loc_418"),
    )


    label("loc_332")

    OP_D2(0x701D0, 0x701DC, 0x7)
    OP_D2(0x701D1, 0x701DD, 0x8)
    Jump("loc_418")

    label("loc_349")

    OP_D2(0x70218, 0x70224, 0x7)
    OP_D2(0x70219, 0x70225, 0x8)
    Jump("loc_418")

    label("loc_360")

    OP_D2(0x701E8, 0x701F4, 0x7)
    OP_D2(0x701E9, 0x701F5, 0x8)
    Jump("loc_418")

    label("loc_377")

    OP_D2(0x27036E, 0x27037B, 0x7)
    OP_D2(0x27036F, 0x27037C, 0x8)
    Jump("loc_418")

    label("loc_38E")

    OP_D2(0x70230, 0x7023C, 0x7)
    OP_D2(0x70231, 0x7023D, 0x8)
    Jump("loc_418")

    label("loc_3A5")

    OP_D2(0x70248, 0x70254, 0x7)
    OP_D2(0x70249, 0x70255, 0x8)
    Jump("loc_418")

    label("loc_3BC")

    OP_D2(0x270176, 0x270183, 0x7)
    OP_D2(0x270177, 0x270184, 0x8)
    Jump("loc_418")

    label("loc_3D3")

    OP_D2(0x702B4, 0x702BB, 0x7)
    OP_D2(0x702B5, 0x702BC, 0x8)
    Jump("loc_418")

    label("loc_3EA")

    OP_D2(0x2702D6, 0x2702E0, 0x7)
    OP_D2(0x2702D7, 0x2702E1, 0x8)
    Jump("loc_418")

    label("loc_401")

    OP_D2(0x2702C2, 0x2702CC, 0x7)
    OP_D2(0x2702C3, 0x2702CD, 0x8)
    Jump("loc_418")

    label("loc_418")

    OP_D2(0x27023E, 0x270248, 0x9)
    OP_D2(0x270244, 0x27024E, 0xA)
    OP_D2(0x2601CF, 0x2601D4, 0xB)
    OP_D2(0x2601D0, 0x2601D5, 0xC)
    OP_D2(0x270246, 0x270250, 0xD)
    OP_D2(0x2600D3, 0x2600D8, 0xE)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    Return()

    # Function_2_1B8 end

    def Function_3_469(): pass

    label("Function_3_469")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_469 end

    def Function_4_472(): pass

    label("Function_4_472")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_493")
    Call(0, 14)
    Call(0, 15)

    label("loc_493")

    Call(0, 2)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    OP_A1(0x9, 0x0)
    SetChrPos(0x9, -23640, 20000, 120, 90)
    OP_72(0x0, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(18160, 0, 1020, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23580, 0, -420, 270)
    SetChrPos(0x102, 23550, 0, 850, 270)
    SetChrPos(0xF8, 24710, 0, -660, 270)
    SetChrPos(0xF9, 24630, 0, 720, 270)

    def lambda_5A0():
        OP_6B(3960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5A0)

    def lambda_5B0():
        OP_8E(0xFE, 0x4556, 0x0, 0xFFFFFE5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B0)
    Sleep(80)

    def lambda_5D0():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D0)
    Sleep(100)

    def lambda_5F0():
        OP_8E(0xFE, 0x4A6A, 0x0, 0xFFFFFD6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5F0)
    Sleep(150)

    def lambda_610():
        OP_8E(0xFE, 0x49C0, 0x0, 0x2D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_610)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, -18090, 0, 240, 90)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #0
        0x8,
        "Girl's Voice",
        "Heehee... So you did make it!\x02",
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_725")

    label("loc_6E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_725")

    label("loc_70E")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_725")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_751")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_78F")

    label("loc_751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_778")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_78F")

    label("loc_778")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_78F")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_7A1():
        OP_6D(-18810, 0, 1110, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7A1)

    def lambda_7B9():
        OP_67(0, 5310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B9)

    def lambda_7D1():
        OP_6B(3430, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_801")

    ChrTalk(    #1
        0x107,
        "#065FAh!\x02",
    )

    CloseMessageWindow()

    label("loc_801")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_836")

    ChrTalk(    #2
        0x10F,
        "#178FThe Angel of Slaughter...\x02",
    )

    CloseMessageWindow()
    Jump("loc_866")

    label("loc_836")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_866")

    ChrTalk(    #3
        0x110,
        "#270FThe Angel of Slaughter.\x02",
    )

    CloseMessageWindow()

    label("loc_866")


    ChrTalk(    #4
        0x101,
        "#1002FRenne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#1042FI thought it would be you next.\x02",
    )

    CloseMessageWindow()

    def lambda_8A9():
        OP_8E(0xFE, 0xFFFFDCEC, 0x0, 0xFFFFFE3E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A9)

    def lambda_8C4():
        OP_6D(-14650, 0, 2440, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C4)

    def lambda_8DC():
        OP_67(0, 3910, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8DC)

    def lambda_8F4():
        OP_6B(3680, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F4)

    def lambda_904():
        OP_6E(311, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_904)
    Sleep(300)

    def lambda_919():
        OP_8E(0xFE, 0xFFFFDD82, 0x0, 0x316, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_919)
    Sleep(100)

    def lambda_939():
        OP_8E(0xFE, 0xFFFFE46C, 0x0, 0xFFFFFBB4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_939)
    Sleep(300)
    OP_8E(0xF9, 0xFFFFE444, 0x0, 0x172, 0x1770, 0x0)
    WaitChrThread(0x102, 0x2)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        (
            "#1306F#6PI bet it must've been reeeally\x01",
            "hard to beat those three...\x02\x03",

            "#261FBut I always believed.\x02\x03",

            "I knew the two of you would\x01",
            "get this far!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1002F#2PRenne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1043F#2PDo you still intend to fight us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#263F#6PHeehee, I wonder.\x02\x03",

            "I did say I would, but then I couldn't\x01",
            "kill you at the castle.\x02\x03",

            "#1306FAnd really, I think it'll aaaall depend\x01",
            "on you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1015F#2PIt'll...what now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#261F#6PHee! It's easy, silly!\x02\x03",

            "#265FJust take back what you said\x01",
            "about me before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1020F#2PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#265F#6PAt the top of that tower, you said\x01",
            "me being in the society was wrong.\x02\x03",

            "Take that back and I'll fly away,\x01",
            "just like that!\x02\x03",

            "#261FHow about it? Easy choice, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1026F#2P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C57")

    ChrTalk(    #15
        0x107,
        "#063F#2PRenne...\x02",
    )

    CloseMessageWindow()

    label("loc_C57")


    ChrTalk(    #16
        0x102,
        (
            "#1042F#2PRenne, that deal won't solve anything.\x02\x03",

            "Even if she says she takes the words back,\x01",
            "if she doesn't mean it, there isn't any point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1010F#2PJoshua...it's okay.\x02\x03",

            "#1025FI think I've got this.\x01",
            "Can you leave it to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#1044F#2PEstelle...of course.\x02\x03",

            "#1035FIt's yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1025F#2PThanks.\x02",
    )

    CloseMessageWindow()

    def lambda_D91():
        OP_6D(-16000, 0, 2180, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D91)

    def lambda_DA9():
        OP_67(0, 3400, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA9)

    def lambda_DC1():
        OP_6B(3440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DC1)
    OP_8F(0x101, 0xFFFFD72E, 0x0, 0x1E, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #20
        0x8,
        (
            "#261F#6PHeehee! Gonna say it, right?\x02\x03",

            "#265FCome on, come on! Say it!\x02\x03",

            "Say, 'Renne, you being in the society is A-OK!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1007F#2PRenne...you...\x02\x03",

            "#1019F...need to stop bullying people into\x01",
            " giving you what you want.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0x8,
        "#264F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1002F#2PThe world doesn't revolve just\x01",
            "around you.\x02\x03",

            "And it won't always change just\x01",
            "because you demand it.\x02\x03",

            "#1003FEven if you possess incredible\x01",
            "power, Renne...\x02\x03",

            "Even if your big Pater-Mater will\x01",
            "save you every time you misjudge...\x02\x03",

            "#1010FEven with all that...you can't just\x01",
            "change a person's heart on demand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "#262F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1007F#2PI'll admit, maybe I'M just being a selfish\x01",
            "doofus for not wanting you in the society.\x01",
            "I'm not sure myself!\x02\x03",

            "That's why I won't try to force you out.\x02\x03",

            "#1025FBut I want you to realize something.\x02\x03",

            "That, like Joshua, you can do whatever\x01",
            "you want with your life. You aren't trapped...\x01",
            "You have us. Always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1040F#2P...That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#1300F...\x02\x03",

            "#266FI see.\x02\x03",

            "I give you all the chances in the\x01",
            "world and you slap them all away.\x02\x03",

            "#1306FYou're a stupid idiot, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 14)

    def lambda_1235():
        OP_99(0x8, 0xE, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1235)
    WaitChrThread(0x8, 0x1)
    Sleep(200)

    def lambda_124F():
        OP_99(0x8, 0x8, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_124F)
    Sleep(200)
    Fade(500)

    def lambda_1269():
        OP_6B(3300, 0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1269)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_1288():
        OP_99(0x8, 0x2, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1288)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    OP_0D()

    def lambda_12A3():
        OP_6D(-13120, 0, 1130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12A3)

    def lambda_12BB():
        OP_6B(3510, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12BB)

    def lambda_12CB():
        OP_6C(302000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_12CB)
    Sleep(500)
    SetChrChipByIndex(0x8, 10)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x113, 0x0, 0x50)

    def lambda_1349():

        label("loc_1349")

        OP_7C(0xA, 0xA, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_1349")

    QueueWorkItem2(0x101, 2, lambda_1349)
    Sleep(500)
    OP_43(0x102, 0x0, 0x0, 0x6)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x102, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0xF8, 5)
    SetChrChipByIndex(0xF9, 7)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #28
        0x101,
        (
            "#1003F#2PSorry, everyone.\x02\x03",

            "Maybe we could've avoided this fight,\x01",
            "but...I couldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1035F#2PThere's no need to apologize.\x02\x03",

            "#1040FYou told her what I wanted to\x01",
            "say anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FA")

    ChrTalk(    #30
        0x107,
        (
            "#562F#2PNo, Estelle! You're right!\x01",
            "Totally right!\x02\x03",

            "#062FI don't want to leave Renne\x01",
            "the way she is any more than\x01",
            "you do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_14FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1554")

    ChrTalk(    #31
        0x109,
        (
            "#1061F#2PHeeeey, guidin' lost lambs is part\x01",
            "of the job description!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_1554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C7")

    ChrTalk(    #32
        0x104,
        (
            "#031F#2PHeh, fear not.\x02\x03",

            "Sometimes, little kittens who misbehave\x01",
            "must be dealt with directly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_15C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161C")

    ChrTalk(    #33
        0x106,
        (
            "#051F#2PNo sweat. Disciplinin' kids is part\x01",
            "of an adult's job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_161C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1687")

    ChrTalk(    #34
        0x110,
        (
            "#277FYes, do not apologize.\x02\x03",

            "It is the duty of adults to discipline\x01",
            "unruly children.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_1687")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D5")

    ChrTalk(    #35
        0x108,
        (
            "#070F#2PThis is part of our job as adults.\x01",
            "Don't worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_16D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1738")

    ChrTalk(    #36
        0x105,
        (
            "#1162F#2PI feel the same as you, Estelle.\x01",
            "I'm with you. We won't stand down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_1738")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1798")

    ChrTalk(    #37
        0x103,
        (
            "#027F#2PDon't worry, Estelle. Disciplining the\x01",
            "kiddies is an adult's job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_1798")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_181F")

    ChrTalk(    #38
        0x10F,
        (
            "#176FI admit I...feel like I'm missing some details.\x02\x03",

            "#170FBut something that must be corrected,\x01",
            "must be corrected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1858")

    ChrTalk(    #39
        0x10B,
        "#210F#2PHeheh. C'mon! Let's do it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_1858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188B")

    ChrTalk(    #40
        0x10F,
        "#179FI shall give it my all!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_188B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18C3")

    ChrTalk(    #41
        0x103,
        "#027F#2PHeh. Time to get serious.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_18C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(    #42
        0x105,
        "#1162F#2PI'll give it everything I have.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_1902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1953")

    ChrTalk(    #43
        0x108,
        (
            "#074F#2PAll right. We have a hell of a\x01",
            "fight on our hands!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_1953")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1985")

    ChrTalk(    #44
        0x110,
        "#277FYou shall have my all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_1985")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C4")

    ChrTalk(    #45
        0x106,
        "#051F#2PHeh... All right. Let's do this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_19C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A03")

    ChrTalk(    #46
        0x104,
        "#031F#2PVery well! With love, for Renne!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_1A03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3E")

    ChrTalk(    #47
        0x109,
        "#1060F#2PHeheh! Time to tend the flock!\x02",
    )

    CloseMessageWindow()

    label("loc_1A3E")


    ChrTalk(    #48
        0x101,
        "#1025F#2PGuys...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 201)
    OP_70(0x0, 0xDC)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_71(0x1, 0x4)
    OP_6D(-14790, 8500, 0, 0)
    OP_67(0, -1000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(352, 0)
    SetChrPos(0x8, -20420, 0, 80, 90)
    SetChrPos(0x9, -23900, 20000, 120, 90)

    def lambda_1AED():

        label("loc_1AED")

        OP_7C(0x32, 0x32, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_1AED")

    QueueWorkItem2(0x101, 2, lambda_1AED)
    OP_24(0x113, 0x55)
    Sleep(100)
    OP_24(0x113, 0x5A)
    Sleep(100)
    OP_24(0x113, 0x5F)
    Sleep(100)
    OP_24(0x113, 0x64)
    Sleep(100)

    def lambda_1B2C():
        OP_8F(0xFE, 0xFFFFA3A8, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B2C)
    Sleep(500)

    def lambda_1B4C():
        OP_6D(-14790, 5500, 0, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B4C)

    def lambda_1B64():
        OP_67(0, 2200, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B64)

    def lambda_1B7C():
        OP_6B(1600, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1B7C)
    WaitChrThread(0x9, 0x1)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 221)
    OP_70(0x0, 0xF0)
    WaitChrThread(0x9, 0x1)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_44(0x101, 0x2)
    OP_7C(0x0, 0x320, 0xBB8, 0x578)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x28)
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    Sleep(2000)

    def lambda_1BFE():
        OP_6D(-24500, 2400, 0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1BFE)

    def lambda_1C16():
        OP_67(0, 1980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C16)

    def lambda_1C2E():
        OP_6B(2460, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C2E)

    def lambda_1C3E():
        OP_6E(415, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1C3E)
    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    OP_0D()
    WaitChrThread(0x102, 0x0)
    Sleep(500)

    ChrTalk(    #49
        0x8,
        (
            "#1302F#5PAll of you, then.\x01",
            "ALL my enemies.\x02\x03",

            "I hate this. I HATE YOU.\x01",
            "I'll rip you, cut you, tear you.\x01",
            "MAKE YOU SCREAM.\x02\x03",

            "#1304FPater-Mater.\x01",
            "FULL. OUTPUT.\x02\x03",

            "Slaughter them all! Hold nothing back!\x01",
            "Kill them, KILL them, KILL THEM!!!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Battle(0x463, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_4_472 end

    def Function_5_1D66(): pass

    label("Function_5_1D66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    Call(0, 2)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    OP_A1(0x9, 0x0)
    SetChrPos(0x9, -20000, 0, 5500, 135)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 521)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -9460, 0, -820, 270)
    SetChrPos(0x102, -9160, 0, 360, 270)
    SetChrPos(0xF8, -8020, 0, -1850, 270)
    SetChrPos(0xF9, -7600, 0, -600, 270)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0xF8, 5)
    SetChrChipByIndex(0xF9, 7)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, -18600, 0, 2700, 0)
    OP_6D(-15000, 1300, 2300, 0)
    OP_67(0, 4100, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(326000, 0)
    OP_6E(394, 0)

    def lambda_1EF9():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EF9)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #50
        0x8,
        (
            "#1308F#6PWhat...?\x02\x03",

            "How? How, how, how?!\x01",
            "How could Pater-Mater lose to\x01",
            "someone like Estelle?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x102,
        (
            "#1035F#2PSo the Gordias design isn't as\x01",
            "complete as I thought.\x02\x03",

            "#1043FThe burden on the leg section\x01",
            "was too much. It's immobilized\x01",
            "at this point.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)
    Sleep(300)

    ChrTalk(    #52
        0x8,
        "#1308F#6PCan't be... Can't be!\x02",
    )

    CloseMessageWindow()

    def lambda_2069():
        OP_6D(-21870, 0, 8680, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2069)

    def lambda_2081():
        OP_67(0, 4720, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2081)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x101, 0x0)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #53
        0x8,
        (
            "#1303F#5P#3SPATER-MATER!#2S\x02\x03",

            "STAND UP! PLEASE!\x02\x03",

            "There are enemies to kill!\x01",
            "Kill them! STAND UP! DO IT!\x01",
            "PLEASE!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    OP_22(0xF4, 0x0, 0x64)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x23)
    OP_6F(0x0, 481)
    OP_70(0x0, 0x208)
    Sleep(5200)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(1000)

    ChrTalk(    #54
        0x8,
        "#1307F#5PPater-Mater...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 11)
    OP_22(0xD1, 0x0, 0x50)
    OP_99(0x8, 0x0, 0x4, 0x4B0)
    Sleep(500)
    Fade(500)
    OP_6D(-15270, 0, 3370, 0)
    OP_67(0, 3950, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(326000, 0)
    OP_6E(394, 0)
    OP_0D()

    ChrTalk(    #55
        0x8,
        "#268F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1026F#2POh, Renne...\x02",
    )

    CloseMessageWindow()

    def lambda_223C():
        OP_6D(-18010, 0, 3600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_223C)

    def lambda_2254():
        OP_67(0, 3800, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2254)

    def lambda_226C():
        OP_6B(3050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_226C)

    def lambda_227C():
        OP_8F(0xFE, 0xFFFFC194, 0x0, 0x7B2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_227C)
    Sleep(800)

    def lambda_229C():
        OP_8F(0xFE, 0xFFFFC9AA, 0x0, 0x618, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_229C)
    Sleep(200)

    def lambda_22BC():
        OP_8F(0xFE, 0xFFFFCBBC, 0x0, 0xFFFFFDA8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_22BC)
    Sleep(200)

    def lambda_22DC():
        OP_8F(0xFE, 0xFFFFD08A, 0x0, 0x32, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_22DC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #57
        0x8,
        (
            "#268F#6PWhat do you want?\x02\x03",

            "You won, Estelle. You got what you wanted.\x01",
            "Doesn't matter anymore.\x02\x03",

            "Go unlock the gate and...go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1006F#4PI do need to do that, but that can wait a bit.\x02\x03",

            "Because right now, you're more important.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #59
        0x8,
        (
            "#1303F#6POH, SHUT UP!\x01",
            "YOU DON'T KNOW ANYTHING ABOUT ME!\x02\x03",

            "WHY?! WHY WON'T YOU GO AWAY?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1012F#4PIt should be obvious.\x02\x03",

            "#1006FBecause I really care about you, Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "#1308F#6PHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1002F#4PThat's why... Okay, step one is something\x01",
            "I think needs doing.\x02\x03",

            "I'm sorry. This'll be light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "#1307F#6PHuh--\x02",
    )

    CloseMessageWindow()

    def lambda_254C():
        OP_6D(-19570, 0, 4110, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_254C)

    def lambda_2564():
        OP_6B(2630, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2564)
    OP_8F(0x101, 0xFFFFBA78, 0x0, 0x992, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Fade(1000)

    def lambda_2592():
        OP_6B(2480, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2592)
    SetChrFlags(0x101, 0x80)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 12)

    def lambda_25C0():
        OP_99(0xFE, 0x0, 0xD, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25C0)
    Sleep(500)
    OP_20(0x0)
    OP_22(0xA5, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #64
        0x8,
        (
            "#1308F#6P...Ow.\x02\x03",

            "#40WYou...hit me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x76)
    Sleep(500)

    ChrTalk(    #65
        0x101,
        (
            "#1007F#4PI'm sorry, but you've had that coming.\x02\x03",

            "I kinda get the impression you've needed\x01",
            "to feel other people's pain for a while now.\x02\x03",

            "#1006FThat's part of growing up, you know?\x01",
            "Understanding the pain OTHER people feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#1309F#6P#40WYou're...just like them...\x02\x03",

            "#40WYou know you'll hurt me...\x01",
            "But you still do it...\x02\x03",

            "#40WYou... You're the same as those people...\x01",
            "The ones who hurt little Renne so much...\x01",
            "Hate... I Hate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1025F#4PIs that what you really think?\x02\x03",

            "Do you really think there's no difference\x01",
            "between me and them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#1309F#6P#40WI...\x02\x03",

            "#40WI don't know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1006F#4PHow about if I do this?\x02",
    )

    CloseMessageWindow()

    def lambda_2888():
        OP_6D(-19900, 0, 4500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2888)
    OP_99(0x8, 0xD, 0x13, 0x5DC)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #70
        0x8,
        "#1307F#6PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1012F#4PI won't lecture any more.\x02\x03",

            "Renne, you answer how your heart\x01",
            "tells you. If it's hate...then all right.\x01",
            "But listen to yourself. Please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#1307F#6P#40W...\x02\x03",

            "#40WI'm... I'm confused. My head is fuzzy.\x01",
            "But I...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x13, 0x15, 0x3E8)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #73
        0x8,
        (
            "#1309F#6P#40WI don't...dislike being hugged...\x01",
            "Maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1016F#4PWell, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#1309F#6P...\x02\x03",

            "#268FHome...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1004F#4PHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #77
        0x8,
        (
            "#1303F#6P#3SPater-Mater!\x02\x03",

            "Deactivate your leg actuators!\x01",
            "Engage booster mode!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1500)

    def lambda_2AB6():
        OP_6D(-22500, 500, 9860, 2500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2AB6)

    def lambda_2ACE():
        OP_67(0, 5300, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2ACE)

    def lambda_2AE6():
        OP_6B(3600, 2500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2AE6)
    Sleep(500)
    Play3DEffect(0x3, 0x0, 0x0, "Frame86__jet_0", 0x0, 0xFFFFFE0C, 0x0, 0x3C, 0xFFA6, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x3, 0x1, 0x0, "Frame87__jet_1", 0x0, 0xFFFFFE0C, 0x0, 0x1E, 0x46, 0xFF4C, 0x3E8, 0x3E8, 0x3E8, 0x0)

    def lambda_2B65():
        OP_8F(0xFE, 0xFFFFAFEC, 0x5DC, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B65)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 521)
    OP_70(0x0, 0x230)
    PlayEffect(0x1, 0x2, 0x9, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_22(0x113, 0x0, 0x64)
    OP_22(0x114, 0x0, 0x64)
    Sleep(100)
    Fade(250)
    SetChrPos(0x101, -18000, 0, 2450, 270)
    SetChrPos(0x8, -18700, 0, 2660, 90)
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x40)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)

    def lambda_2C2A():
        OP_8F(0xFE, 0xFFFFB3A2, 0x0, 0xBE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2C2A)
    WaitChrThread(0x8, 0x0)
    OP_0D()
    Sleep(300)
    OP_8C(0x101, 315, 400)

    def lambda_2C57():
        OP_8F(0xFE, 0xFFFFBFB4, 0x0, 0x5AA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C57)
    OP_43(0x102, 0x1, 0x0, 0x8)
    Sleep(50)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x1)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_B0(0x0, 0x1)
    OP_6F(0x0, 30)
    Sleep(300)
    Fade(500)
    OP_71(0x1, 0x4)
    OP_6D(-20000, 1800, 3140, 0)
    OP_67(0, 3170, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(291000, 0)
    OP_6E(598, 0)

    def lambda_2CFE():
        OP_8F(0xFE, 0xFFFFAFEC, 0x0, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CFE)
    WaitChrThread(0x9, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    OP_72(0x0, 0x20)
    OP_0D()
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_22(0x115, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_D8(0x0, 0x320)
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    Sleep(1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_2D82():

        label("loc_2D82")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2D82")

    QueueWorkItem2(0x101, 3, lambda_2D82)

    def lambda_2D93():
        OP_6D(-24790, 0, 4270, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D93)

    def lambda_2DAB():
        OP_67(0, 5140, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2DAB)

    def lambda_2DC3():
        OP_6B(2200, 1000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2DC3)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 2)
    OP_96(0x8, 0xFFFFAE3E, 0xE10, 0x9C4, 0x1194, 0xBB8)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0x8, 0x1)
    OP_CF(0x8, 0x0, "Frame85__ren")
    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7D(0x1, 0x8, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 315, 0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #78
        0x101,
        "#1020F#5PRenne!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #79
        0x8,
        (
            "#1309F#6PMy head is all fuzzy... I need...\x01",
            "I need to think. Alone, for a bit.\x02\x03",

            "Estelle, you can go on up to the roof.\x02\x03",

            "Loewe's waiting for you there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1002F#5PLoewe? Knew it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#1040F#2PI see. Thank you for telling us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#1307F#6PJoshua...be careful, okay?\x02\x03",

            "Loewe is really serious about\x01",
            "stopping you this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#1035F#2PYes, I know.\x02\x03",

            "#1040FBut don't worry. I'm always\x01",
            "prepared, remember?\x02\x03",

            "Just like he taught us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#1307F#6POkay...\x02\x03",

            "#268FWell, um.\x01",
            "I'm...going, then.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_22(0x114, 0x0, 0x64)
    OP_22(0xCC, 0x0, 0x64)
    Play3DEffect(0x2, 0x0, 0x0, "Frame86__jet_0", 0x0, 0xFFFFFD44, 0x0, 0x3C, 0xFFA6, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x2, 0x1, 0x0, "Frame87__jet_1", 0x0, 0xFFFFFD44, 0x0, 0x1E, 0x46, 0xFF4C, 0x3E8, 0x3E8, 0x3E8, 0x0)

    def lambda_30CB():
        OP_8F(0xFE, 0xFFFFB1E0, 0x7D0, 0x157C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_30CB)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3128")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3166")

    label("loc_3128")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314F")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3166")

    label("loc_314F")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3166")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3192")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_31D0")

    label("loc_3192")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B9")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_31D0")

    label("loc_31B9")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_31D0")


    def lambda_31D6():
        OP_6D(-20260, 4500, 4520, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_31D6)

    def lambda_31EE():
        OP_67(0, 3530, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31EE)

    def lambda_3206():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3206)

    def lambda_3216():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3216)

    def lambda_3226():
        OP_6E(388, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3226)
    Sleep(800)
    OP_D8(0x0, 0x1F4)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x5)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x104)

    def lambda_3256():

        label("loc_3256")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3256")

    QueueWorkItem2(0x101, 3, lambda_3256)

    def lambda_3267():

        label("loc_3267")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3267")

    QueueWorkItem2(0x102, 3, lambda_3267)

    def lambda_3278():

        label("loc_3278")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3278")

    QueueWorkItem2(0xF8, 3, lambda_3278)

    def lambda_3289():

        label("loc_3289")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3289")

    QueueWorkItem2(0xF9, 3, lambda_3289)
    Sleep(300)

    def lambda_329F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_329F)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x1)
    PlayEffect(0x1, 0x2, 0x9, 0, -1500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, -13180, 0, -540, 270)
    SetChrPos(0x102, -12060, 0, 230, 270)
    SetChrPos(0xF8, -11210, 0, -1500, 270)
    SetChrPos(0xF9, -11210, 0, -1500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33DF")

    ChrTalk(    #85
        0x107,
        "#065F#5PRenne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        "#1020F#5PRenne, wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#1300F#6PBye-bye, Estelle, Tita.\x02\x03",

            "I need to go for a bit, but...\x02\x01",

            "#1301FBut if you die, I'll never forgive you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3469")

    label("loc_33DF")


    ChrTalk(    #88
        0x101,
        "#1020F#5PRenne, wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#1300F#6PBye-bye, Estelle.\x02\x03",

            "I need to go for a bit, but...\x02\x01",

            "#1301FBut if you die, I'll never forgive you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3469")


    def lambda_346F():
        OP_6D(-20220, 7330, 11320, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_346F)

    def lambda_3487():
        OP_67(0, 2760, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3487)

    def lambda_349F():
        OP_6B(4000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_349F)

    def lambda_34AF():
        OP_6C(327000, 4500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34AF)

    def lambda_34BF():
        OP_6E(362, 4500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_34BF)
    PlayEffect(0x2, 0x0, 0x9, 4750, 2300, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x9, -4750, 2300, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_24(0x113, 0x5F)

    def lambda_353D():
        OP_8C(0xFE, 0, 50)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_353D)

    def lambda_354B():
        OP_8F(0xFE, 0xFFFFB1E0, 0x1388, 0x157C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_354B)
    Sleep(100)

    def lambda_356B():
        OP_8F(0xFE, 0xFFFFB1E0, 0x1388, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_356B)
    OP_82(0x2, 0x2)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x2)
    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x118)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x0)
    OP_D8(0x0, 0x1F4)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 281)
    OP_70(0x0, 0x12C)
    PlayEffect(0x3, 0x2, 0x9, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x9, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x9, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x9, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x9, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x9, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    PlayEffect(0x2, 0x2, 0x9, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x9, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x9, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x9, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x9, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x9, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3896():
        OP_6D(-21400, 6800, 20800, 1800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3896)

    def lambda_38AE():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38AE)
    Sleep(300)

    def lambda_38CE():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38CE)
    Sleep(200)

    def lambda_38EE():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38EE)
    Sleep(100)

    def lambda_390E():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_390E)
    Sleep(100)

    def lambda_392E():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_392E)
    Sleep(100)

    def lambda_394E():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_394E)
    Sleep(100)

    def lambda_396E():
        OP_8F(0xFE, 0xFFFFB1E0, 0x2EE0, 0xD8CC, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_396E)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x10FF)
    OP_A2(0x10FA)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1D66 end

    def Function_6_39AD(): pass

    label("Function_6_39AD")


    def lambda_39B3():
        OP_8F(0xFE, 0xFFFFE070, 0x0, 0xFFFFFEC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39B3)
    Sleep(120)

    def lambda_39D3():
        OP_8F(0xFE, 0xFFFFE76E, 0x0, 0x276, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_39D3)
    Sleep(80)

    def lambda_39F3():
        OP_8F(0xFE, 0xFFFFE7E6, 0x0, 0xFFFFFCCC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_39F3)
    Sleep(100)

    def lambda_3A13():
        OP_8F(0xFE, 0xFFFFE066, 0x0, 0x3B6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A13)
    WaitChrThread(0x101, 0x0)
    Return()

    # Function_6_39AD end

    def Function_7_3A2E(): pass

    label("Function_7_3A2E")


    def lambda_3A34():
        OP_8E(0xFE, 0x448E, 0x0, 0xFFFFFF24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A34)
    Sleep(40)

    def lambda_3A54():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A54)
    Sleep(100)

    def lambda_3A74():
        OP_8E(0xFE, 0x49DE, 0x0, 0x4F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3A74)
    Sleep(50)
    OP_8E(0xF9, 0x498E, 0x0, 0xFFFFFCF4, 0xBB8, 0x0)
    Return()

    # Function_7_3A2E end

    def Function_8_3AA3(): pass

    label("Function_8_3AA3")

    OP_8F(0xFE, 0xFFFFC306, 0x0, 0x83E, 0x7D0, 0x0)

    def lambda_3ABD():

        label("loc_3ABD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3ABD")

    QueueWorkItem2(0xFE, 3, lambda_3ABD)
    Return()

    # Function_8_3AA3 end

    def Function_9_3AC9(): pass

    label("Function_9_3AC9")

    OP_8F(0xFE, 0xFFFFC694, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_3AE3():

        label("loc_3AE3")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3AE3")

    QueueWorkItem2(0xFE, 3, lambda_3AE3)
    Return()

    # Function_9_3AC9 end

    def Function_10_3AEF(): pass

    label("Function_10_3AEF")

    OP_8F(0xFE, 0xFFFFCB62, 0x0, 0x3B6, 0x7D0, 0x0)

    def lambda_3B09():

        label("loc_3B09")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3B09")

    QueueWorkItem2(0xFE, 3, lambda_3B09)
    Return()

    # Function_10_3AEF end

    def Function_11_3B15(): pass

    label("Function_11_3B15")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B2C")
    Call(0, 14)
    Call(0, 15)

    label("loc_3B2C")

    OP_6D(-18300, 0, 10600, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -17750, 0, 10660, 0)
    SetChrPos(0x102, -16059, 0, 9050, 0)
    SetChrPos(0xF8, -17240, 0, 7850, 0)
    SetChrPos(0xF9, -15710, 0, 7250, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #90
        0x101,
        (
            "#1026F#6P...\x02\x03",

            "#1003FDid that...turn out okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#1035F#5PI think she'll be all right.\x02\x03",

            "#1040FYou kind of piled a lot on her plate,\x01",
            "Estelle. She hasn't felt things like that\x01",
            "in a long time. A very long time.\x02\x03",

            "She needs time to think it through.\x01",
            "She'll find an answer someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1025F#6PMmm...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D2D")

    ChrTalk(    #93
        0x107,
        "#067F#5PHeehee... I hope we see her again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FCC")

    label("loc_3D2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D6D")

    ChrTalk(    #94
        0x105,
        "#1168F#5PI hope we see her again someday.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FCC")

    label("loc_3D6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA7")

    ChrTalk(    #95
        0x103,
        "#027F#5PHaha. We'll meet her again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FCC")

    label("loc_3DA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DFA")

    ChrTalk(    #96
        0x104,
        (
            "#035F#5PHeh. Your paths shall cross again\x01",
            "one day, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FCC")

    label("loc_3DFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E42")

    ChrTalk(    #97
        0x109,
        "#1062F#5PHeheh! You'll run into her again, I bet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FCC")

    label("loc_3E42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E85")

    ChrTalk(    #98
        0x106,
        "#051F#5PHeh... I'm sure we'll see her again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FCC")

    label("loc_3E85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ECD")

    ChrTalk(    #99
        0x108,
        "#070F#1PHaha. I look forward to seeing her again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FCC")

    label("loc_3ECD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F5C")

    ChrTalk(    #100
        0x10F,
        (
            "#179FPatience, Estelle.\x02\x03",

            "#170F'You can always turn back'...\x01",
            "wasn't that your entire message?\x01",
            "She'll find her way to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FCC")

    label("loc_3F5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FCC")

    ChrTalk(    #101
        0x10B,
        (
            "#210FHeh, just mean's she's still a kid.\x02\x03",

            "Give her some time to pout.\x01",
            "You'll find her again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FCC")


    ChrTalk(    #102
        0x101,
        (
            "#1025F#6PYeah... I hope so.\x02\x03",

            "#1012FRenne...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(300)

    ChrTalk(    #103
        0x101,
        (
            "#1006F#6PAll righty.\x01",
            "Time to get my game face back on.\x02\x03",

            "Let's open the lock and get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x102,
        "#1043F#5PYes. We should.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #105
        0x101,
        (
            "#1026F#6POh, right.\x02\x03",

            "#1002FShe said Loewe's waiting for\x01",
            "us just ahead, didn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x102,
        "#1043F#5PShe did.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(500)

    ChrTalk(    #107
        0x102,
        (
            "#1035F#5PEnforcer No. II.\x01",
            "Leonhardt the Bladelord.\x02\x03",

            "One of the deadliest fighters the\x01",
            "society has. Maybe THE deadliest.\x02\x03",

            "#1042FWe need to be absolutely, completely\x01",
            "certain we're prepared before we proceed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1002F#6PRight.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_421E")
    OP_A2(0x2240)

    label("loc_421E")

    OP_A2(0x223A)
    OP_28(0x9F, 0x1, 0x400)
    OP_28(0x9F, 0x1, 0x800)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0x40)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_3B15 end

    def Function_12_4240(): pass

    label("Function_12_4240")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #109
        "\x07\x05Barrier to upper levels and transport gate now unlocked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5306   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_12_4240 end

    def Function_13_42B6(): pass

    label("Function_13_42B6")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42CD")
    Call(0, 14)
    Call(0, 15)

    label("loc_42CD")

    OP_6D(-33350, 0, 660, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3430, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -31400, 0, -720, 270)
    SetChrPos(0x102, -31400, 0, 210, 270)
    SetChrPos(0xF8, -29800, 0, -1260, 270)
    SetChrPos(0xF9, -29800, 0, 10, 270)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #110
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
    OP_A2(0x223B)
    OP_28(0x9F, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_13_42B6 end

    def Function_14_43D1(): pass

    label("Function_14_43D1")

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
        (0, "loc_444A"),
        (1, "loc_4450"),
        (SWITCH_DEFAULT, "loc_4456"),
    )


    label("loc_444A")

    OP_A2(0x1200)
    Jump("loc_4456")

    label("loc_4450")

    OP_A2(0x1201)
    Jump("loc_4456")

    label("loc_4456")

    Return()

    # Function_14_43D1 end

    def Function_15_4457(): pass

    label("Function_15_4457")

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

    # Function_15_4457 end

    SaveToFile()

Try(main)
