from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5308   ._SN',
        MapName             = 'Other',
        Location            = 'C5308.x',
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
        'Bleublanc',                            # 9
        'Balancing Clown',                      # 10
        'Balancing Clown',                      # 11
        'Targeting Camera',                     # 12
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
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_14E",          # 00, 0
        "Function_1_19C",          # 01, 1
        "Function_2_1D3",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_3B1",          # 04, 4
        "Function_5_2A04",         # 05, 5
        "Function_6_3506",         # 06, 6
        "Function_7_354E",         # 07, 7
        "Function_8_35C4",         # 08, 8
        "Function_9_363A",         # 09, 9
        "Function_10_3660",        # 0A, 10
        "Function_11_3686",        # 0B, 11
        "Function_12_36AC",        # 0C, 12
        "Function_13_36D2",        # 0D, 13
        "Function_14_3701",        # 0E, 14
        "Function_15_3716",        # 0F, 15
        "Function_16_372B",        # 10, 16
        "Function_17_3740",        # 11, 17
        "Function_18_37B6",        # 12, 18
        "Function_19_38D1",        # 13, 19
        "Function_20_3957",        # 14, 20
    )


    def Function_0_14E(): pass

    label("Function_0_14E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_15F")
    OP_A3(0x10F0)
    Event(0, 18)
    Jump("loc_179")

    label("loc_15F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_179")

    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_14E end

    def Function_1_19C(): pass

    label("Function_1_19C")

    OP_22(0x1C3, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 3)), scpexpr(EXPR_END)), "loc_1B1")
    OP_64(0x0, 0x1)
    OP_71(0x1, 0x4)

    label("loc_1B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x460), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1")
    Call(0, 2)

    label("loc_1C1")

    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_19C end

    def Function_2_1D3(): pass

    label("Function_2_1D3")

    OP_D2(0x2701C9, 0x2701CE, 0x0)
    OP_D2(0x2900A2, 0x2900A6, 0x1)
    OP_D2(0x2900A3, 0x2900A7, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270130, 0x270140, 0x4)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_236"),
        (5, "loc_243"),
        (3, "loc_250"),
        (4, "loc_25D"),
        (6, "loc_26A"),
        (7, "loc_277"),
        (8, "loc_284"),
        (10, "loc_291"),
        (14, "loc_29E"),
        (15, "loc_2AB"),
        (SWITCH_DEFAULT, "loc_2B8"),
    )


    label("loc_236")

    OP_D2(0x701D0, 0x701DC, 0x5)
    Jump("loc_2B8")

    label("loc_243")

    OP_D2(0x70218, 0x70224, 0x5)
    Jump("loc_2B8")

    label("loc_250")

    OP_D2(0x701E8, 0x701F4, 0x5)
    Jump("loc_2B8")

    label("loc_25D")

    OP_D2(0x27036E, 0x27037B, 0x5)
    Jump("loc_2B8")

    label("loc_26A")

    OP_D2(0x70230, 0x7023C, 0x5)
    Jump("loc_2B8")

    label("loc_277")

    OP_D2(0x70248, 0x70254, 0x5)
    Jump("loc_2B8")

    label("loc_284")

    OP_D2(0x270176, 0x270183, 0x5)
    Jump("loc_2B8")

    label("loc_291")

    OP_D2(0x702B4, 0x702BB, 0x5)
    Jump("loc_2B8")

    label("loc_29E")

    OP_D2(0x2702D6, 0x2702E0, 0x5)
    Jump("loc_2B8")

    label("loc_2AB")

    OP_D2(0x2702C2, 0x2702CC, 0x5)
    Jump("loc_2B8")

    label("loc_2B8")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2E9"),
        (5, "loc_2F6"),
        (3, "loc_303"),
        (4, "loc_310"),
        (6, "loc_31D"),
        (7, "loc_32A"),
        (8, "loc_337"),
        (10, "loc_344"),
        (14, "loc_351"),
        (15, "loc_35E"),
        (SWITCH_DEFAULT, "loc_36B"),
    )


    label("loc_2E9")

    OP_D2(0x701D0, 0x701DC, 0x6)
    Jump("loc_36B")

    label("loc_2F6")

    OP_D2(0x70218, 0x70224, 0x6)
    Jump("loc_36B")

    label("loc_303")

    OP_D2(0x701E8, 0x701F4, 0x6)
    Jump("loc_36B")

    label("loc_310")

    OP_D2(0x27036E, 0x27037B, 0x6)
    Jump("loc_36B")

    label("loc_31D")

    OP_D2(0x70230, 0x7023C, 0x6)
    Jump("loc_36B")

    label("loc_32A")

    OP_D2(0x70248, 0x70254, 0x6)
    Jump("loc_36B")

    label("loc_337")

    OP_D2(0x270176, 0x270183, 0x6)
    Jump("loc_36B")

    label("loc_344")

    OP_D2(0x702B4, 0x702BB, 0x6)
    Jump("loc_36B")

    label("loc_351")

    OP_D2(0x2702D6, 0x2702E0, 0x6)
    Jump("loc_36B")

    label("loc_35E")

    OP_D2(0x2702C2, 0x2702CC, 0x6)
    Jump("loc_36B")

    label("loc_36B")

    OP_D2(0x27026B, 0x270275, 0x7)
    OP_D2(0x27026E, 0x270278, 0x8)
    OP_D2(0x26020D, 0x260212, 0x9)
    OP_D2(0x26008F, 0x260094, 0xA)
    LoadEffect(0x0, "map\\\\mp046_00.eff")
    Return()

    # Function_2_1D3 end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_3A8 end

    def Function_4_3B1(): pass

    label("Function_4_3B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D2")
    Call(0, 19)
    Call(0, 20)

    label("loc_3D2")

    Call(0, 2)
    OP_6D(-720, 0, -17580, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x0, 0x0, 0x9)
    Sleep(80)
    OP_43(0x102, 0x0, 0x0, 0xA)
    Sleep(50)
    OP_43(0xF8, 0x0, 0x0, 0xB)
    Sleep(100)
    OP_43(0xF9, 0x0, 0x0, 0xC)

    def lambda_444():
        OP_6B(3960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_444)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1020F#6PWaa-ah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1042F#6PThis must be an exterior platform\x01",
            "of some sort.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C0():
        OP_6D(-1010, 0, 4630, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C0)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #2
        0x101,
        "#1002F#6PWow, we're way up here already.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #3
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_56C():
        OP_6D(-1540, 0, 34870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_56C)

    def lambda_584():
        OP_67(0, 4200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_584)

    def lambda_59C():
        OP_6B(2780, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_59C)

    def lambda_5AC():
        OP_6E(382, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5AC)

    def lambda_5BC():
        OP_6C(327000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5BC)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    def lambda_5D6():
        OP_8E(0xFE, 0x6AE, 0x0, 0x636A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D6)
    Sleep(50)

    def lambda_5F6():
        OP_8E(0xFE, 0x15E, 0x0, 0x636A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F6)
    Sleep(100)

    def lambda_616():
        OP_8E(0xFE, 0x7C6, 0x0, 0x5DC0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_616)
    Sleep(60)

    def lambda_636():
        OP_8E(0xFE, 0x26C, 0x0, 0x5DC0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_636)

    def lambda_651():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_651)

    def lambda_661():
        OP_6D(-1140, 0, 29790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_661)

    def lambda_679():
        OP_67(0, 4780, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_679)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #4
        0x101,
        "#1015F#5PHey, what's that?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(    #5
        0x108,
        (
            "#072F#5PHmm.\x02\x03",

            "It looks like another information access\x01",
            "point, but the placement seems...ominous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A0")

    ChrTalk(    #6
        0x106,
        (
            "#555F#5PLooks like another computer thing...\x02\x03",

            "...but it sorta feels like bait on a hook.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_7A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81A")

    ChrTalk(    #7
        0x10F,
        (
            "#178F#5PIt looks like a computer access point.\x02\x03",

            "But I can't help but feel nervous\x01",
            "at its placement.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_81A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88A")

    ChrTalk(    #8
        0x104,
        (
            "#033F#5PHmm?\x02\x03",

            "#035FIt looks like another computer, but\x01",
            "it does rather seem like bait, no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_88A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_902")

    ChrTalk(    #9
        0x109,
        (
            "#1063F#5PSome sort of computer thing, I think...\x02\x03",

            "But doesn't this feel juuust a bit\x01",
            "like a trap?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_970")

    ChrTalk(    #10
        0x103,
        (
            "#023F#5POh! I think it's a computer access point.\x02\x03",

            "Though the placement is a bit...odd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_970")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D3")

    ChrTalk(    #11
        0x10B,
        (
            "#212F#5PLooks like another computer thingy.\x02\x03",

            "Why's it way out there, though?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_9D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2F")

    ChrTalk(    #12
        0x110,
        (
            "#270F#5PHmm. A computer of some sort.\x02\x03",

            "And it feels rather like bait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB2")

    label("loc_A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB2")

    ChrTalk(    #13
        0x105,
        (
            "#1164F#5PIt looks like a computer of some sort.\x02\x03",

            "#1162FBut the way it's placed...\x01",
            "something doesn't feel right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B46")

    ChrTalk(    #14
        0x107,
        (
            "#062F#5PWell, um, we should check\x01",
            "it out anyway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        "#1035F#5PNo. We have something to take care of first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x107,
        "#064F#5PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_B46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE0")

    ChrTalk(    #17
        0x105,
        "#1162F#5PSuspicious or not, we have to investigate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#1035F#5PNo. We have something to take care of first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        "#1164F#5PHm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_BE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C60")

    ChrTalk(    #20
        0x110,
        "#272F#5PLet's spring the trap, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#1035F#5PIt's a little late for that, I'm afraid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x110,
        "#270FHm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_C60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CEF")

    ChrTalk(    #23
        0x10B,
        "#212F#5PAll right, let's spring that trap, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1035F#5PIt's a little late for that, I'm afraid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10B,
        "#213F#5PEh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D96")

    ChrTalk(    #26
        0x103,
        (
            "#022F#5PWell, if it is a trap, we may as\x01",
            "well walk into the teeth of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#1035F#5PIt's a little late for that, I'm afraid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        "#023F#5PHm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_D96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E26")

    ChrTalk(    #29
        0x109,
        "#1063F#5PLet's go take a look at it anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1035F#5PNo. We have something to take care of first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        "#1064F#5PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_E26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBE")

    ChrTalk(    #32
        0x104,
        (
            "#035F#5PHmm. Ominous as it is,\x01",
            "let us investigate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#1035F#5PNo. We have something to take care of first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x104,
        "#033F#5POh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4E")

    ChrTalk(    #35
        0x10F,
        "#178F#5PWe have little choice but to go forward.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#1035F#5PNo. We have something to take care of first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#173FHm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_F4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEF")

    ChrTalk(    #38
        0x106,
        (
            "#051F#5PHeh, I don't see a problem.\x01",
            "Let's take a look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        "#1035F#5PNo. We have something to take care of first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x106,
        "#052F#5PWhat...?\x02",
    )

    CloseMessageWindow()

    label("loc_FEF")

    SetChrChipByIndex(0x8, 7)
    SetChrPos(0x8, 3070, 6620, 33000, 180)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_20(0x3E8)
    OP_21()

    NpcTalk(    #41
        0x8,
        "Man's Voice",
        (
            "#6PHeh heh, most impressive, Black Fang.\x02\x03",

            "I had thought my concealment perfect,\x01",
            "but as always, you pick up the most\x01",
            "subtle of signs.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F4")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1132")

    label("loc_10F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111B")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1132")

    label("loc_111B")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1132")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115E")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_119C")

    label("loc_115E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1185")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_119C")

    label("loc_1185")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_119C")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)
    Fade(1000)
    OP_71(0x0, 0x4)
    ClearMapFlags(0x10)
    OP_6D(3030, 4570, 31690, 0)
    OP_67(0, 3680, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(0, 0)
    OP_6E(382, 0)

    def lambda_11FA():
        OP_6D(3030, 7260, 31690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11FA)

    def lambda_1212():
        OP_67(0, 3400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1212)
    Sleep(1500)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(500)

    def lambda_126E():
        OP_6B(2390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_126E)
    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x6)
    Sleep(500)

    def lambda_1292():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1292)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)

    ChrTalk(    #42
        0x101,
        "#1020F#2PPervert mask guy!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F4")

    ChrTalk(    #43
        0x110,
        "#270F(Who in the world?)\x02",
    )

    CloseMessageWindow()

    label("loc_12F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137F")

    ChrTalk(    #44
        0x10F,
        (
            "#178F(The masked man who appeared at Esmelas Tower.)\x02\x03",

            "#176F(So this is the scum who dares\x01",
            "to chase after Her Highness.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137F")


    ChrTalk(    #45
        0x102,
        "#1042F#5PBleublanc.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BF")

    ChrTalk(    #46
        0x8,
        (
            "#231F#6PWelcome, Joshua, and Estelle Bright.\x02\x03",

            "A pity neither my rival in beauty nor\x01",
            "my princess are here...\x02\x03",

            "Even so. Allow me to welcome you\x01",
            "from the depths of my heart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1002F#2P...'Welcome'? Oh, crap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#1042F#5PYou're to be our first obstacle, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A5E")

    label("loc_14BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16FE")

    ChrTalk(    #49
        0x8,
        (
            "#231F#6PJoshua, Estelle Bright, and my proud princess.\x02\x03",

            "I do wish my rival in beauty could have been\x01",
            "here as well, but we shall endure, yes?\x02\x03",

            "Allow me to welcome you from\x01",
            "the depths of my heart!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1610")

    ChrTalk(    #50
        0x101,
        "#1002F#2P...'Welcome'? Oh, crap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x105,
        "#1162F#5PYou intend to be our first obstacle, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16FB")

    label("loc_1610")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16FB")

    ChrTalk(    #52
        0x10F,
        (
            "#176FWelcome, is it?\x02\x03",

            "#172FStep forward, then.\x01",
            "Let me return your hospitality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x105,
        (
            "#1165F(I was afraid Julia wouldn't have\x01",
            "much time for his nonsense...)\x02\x03",

            "#1162FYou intend to be our first obstacle,\x01",
            "then, Bleublanc.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FB")

    Jump("loc_1A5E")

    label("loc_16FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_190B")

    ChrTalk(    #54
        0x8,
        (
            "#231F#6PJoshua, Estelle Bright, and my luminous rival!\x02\x03",

            "Alas that my princess is absent!\x01",
            "But we shall endure.\x02\x03",

            "Allow me to welcome you from\x01",
            "the depths of my heart!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1836")

    ChrTalk(    #55
        0x101,
        "#1002F#2P...'Welcome'? Oh, crap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x104,
        (
            "#035F#5PYou are to be our first obstacle, then,\x01",
            "my rival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1908")

    label("loc_1836")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1908")

    ChrTalk(    #57
        0x110,
        (
            "#276FAh. I see.\x02\x03",

            "#272FSo he's just as obnoxious as this\x01",
            "one here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x104,
        "#34FAs moi? Mueller, how cruel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x110,
        (
            "#272FHmph, am I wrong?\x02\x03",

            "#270FIt seems he does intend to stand\x01",
            "in our way, however.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1908")

    Jump("loc_1A5E")

    label("loc_190B")


    ChrTalk(    #60
        0x8,
        (
            "#231F#6PWelcome, Joshua, and Estelle Bright.\x02\x03",

            "And you have even brought my princess\x01",
            "and my rival with you!\x02\x03",

            "Oh, but you have the gratitude of this\x01",
            "humble Phantom Thief!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1002F#2P...'Welcome'? Oh, crap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x104,
        (
            "#035F#5POh, so help me, your entrances are\x01",
            "as graceless as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x105,
        "#1162F#5PYou intend to be our first obstacle, then.\x02",
    )

    CloseMessageWindow()

    label("loc_1A5E")


    ChrTalk(    #64
        0x8,
        (
            "#230F#6PHeh. Quite.\x01",
            "I am your first and LAST obstacle.\x02\x03",

            "Before you is the terminal which locks\x01",
            "the gate leading further into the pillar.\x02\x03",

            "As long as it goes unmolested,\x01",
            "you can proceed no further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1019F#2PAnd so, of course, you wait here right beside\x01",
            "it for us to show up so you can get in our way.\x01",
            "Real creative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        (
            "#1035F#5P...Bleublanc.\x02\x03",

            "#1042FI still don't understand. Of all the Enforcers\x01",
            "who have come, you are the one with the\x01",
            "least stake in all this.\x02\x03",

            "What reason is there to continue to obey\x01",
            "Weissmann and fight us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#230F#6PAh, I must correct you.\x01",
            "I am not 'obeying' the professor, per se.\x02\x03",

            "Perhaps I should explain for our other guests?\x01",
            "Despite the title, Enforcers need not obey\x01",
            "orders they do not wish to.\x02\x03",

            "Even orders from an Anguis or the Grandmaster.\x01",
            "Ours is a society built on willing cooperation.\x02\x03",

            "#231FMmm... Though, sadly, as the good professor's\x01",
            "puppet, your circumstances are a little different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        "#1043F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1003F#2PJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#232F#6PMy reason for remaining is singular.\x02\x03",

            "There is something here of great\x01",
            "beauty worth stealing.\x02\x03",

            "That, and only that, is why I remain.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_214C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F34")

    ChrTalk(    #71
        0x10F,
        (
            "#178F#5PSomething worth--\x02\x03",

            "If you're saying what I think you are...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_1F34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F91")

    ChrTalk(    #72
        0x106,
        (
            "#555F#5PSomething of 'great beauty'?\x01",
            "What are you on about now, clown?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_1F91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FE8")

    ChrTalk(    #73
        0x103,
        (
            "#022F#5PSomething of 'great beauty'?\x01",
            "What ARE you talking about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_1FE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_202C")

    ChrTalk(    #74
        0x107,
        "#065F#5PUm, what do you mean, 'great beauty'?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_202C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_208C")

    ChrTalk(    #75
        0x10B,
        (
            "#214F#5PSomething of 'great beauty'?\x01",
            "Go look for it somewhere else, then!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_208C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E6")

    ChrTalk(    #76
        0x109,
        (
            "#1063F#5PSomething of 'great beauty.'\x01",
            "And let me guess, we have it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_20E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(    #77
        0x110,
        (
            "#270F#5PSomething of great beauty worth stealing'?\x02\x03",

            "#272FWhat nonsense is this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2149")

    Jump("loc_226C")

    label("loc_214C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21A4")

    ChrTalk(    #78
        0x105,
        "#1163F#5PSomething of great...beauty...worth stealing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_226C")

    label("loc_21A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21FF")

    ChrTalk(    #79
        0x104,
        (
            "#033F#5PGreat beauty?\x01",
            "And what, pray tell, would that be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_226C")

    label("loc_21FF")


    ChrTalk(    #80
        0x105,
        "#1163F#5PSomething of great...beauty...worth stealing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x104,
        "#033F#5PAnd what, pray tell, would that be?\x02",
    )

    CloseMessageWindow()

    label("loc_226C")


    ChrTalk(    #82
        0x8,
        "#231F#6PHeh. That, my doves, would be your hope.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1020F#2P#3SOur WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#231F#6PHope shines ever more beautifully,\x01",
            "the worse one's situation becomes.\x02\x03",

            "And so I have waited for you, for this\x01",
            "moment, when you are so near the end,\x01",
            "and so fair and desperate.\x02\x03",

            "#232FEven if, in the end, your hope flares\x01",
            "and then fades like a summer firework...\x02\x03",

            "#234FJust once, I must see it! Grasp it!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x800)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0xE, 0x7D0)
    Sleep(200)
    Fade(1000)
    OP_72(0x0, 0x4)
    OP_6D(2800, 4330, 23050, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(315000, 0)
    OP_6E(340, 0)
    OP_0D()

    def lambda_2464():
        OP_67(0, 4680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2464)
    OP_43(0x9, 0x0, 0x0, 0x7)
    Sleep(500)
    OP_43(0xA, 0x0, 0x0, 0x8)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E8")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2526")

    label("loc_24E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250F")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2526")

    label("loc_250F")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2526")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2552")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2590")

    label("loc_2552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2579")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2590")

    label("loc_2579")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2590")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0xF8, 5)
    SetChrChipByIndex(0xF9, 6)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_25CD():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_25CD)
    Sleep(100)
    OP_8C(0xF8, 135, 400)
    OP_0D()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(    #85
        0x8,
        (
            "#231FCome! Show me!\x02\x03",

            "Show me what I have so longed to see--\x01",
            "the shine of the gem of hope, as it shatters\x01",
            "to pieces!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_274A")

    ChrTalk(    #86
        0x101,
        (
            "#1005F#5PYou want hope? FINE!\x01",
            "Here's some hope to the face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x105,
        (
            "#1167F#5PYes. Let us, in turn, show you.\x02\x03",

            "#1162FWe will show you that the hope\x01",
            "born of bonds shall never die!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_292B")

    label("loc_274A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2816")

    ChrTalk(    #88
        0x101,
        (
            "#1005F#5PYou want hope? FINE!\x01",
            "Here's some hope to the face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x104,
        (
            "#035F#5PIndeed. Let me teach you, Bleublanc.\x02\x03",

            "#530FThat, with love, the torch of hope\x01",
            "shall burn forever!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_292B")

    label("loc_2816")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_292B")

    ChrTalk(    #90
        0x101,
        (
            "#1005F#5PYou want hope? FINE!\x01",
            "Here's some hope to the face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x105,
        (
            "#1167F#5PYes. Let us, in turn, show you.\x02\x03",

            "#1162FWe will show you that the hope\x01",
            "born of bonds shall never die!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x104,
        (
            "#035F#5PAnd that, with love, the torch of\x01",
            "hope shall burn forever!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292B")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_293F():
        OP_6D(190, 980, 24880, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_293F)

    def lambda_2957():
        OP_67(0, 4830, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2957)

    def lambda_296F():
        OP_6B(2800, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_296F)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 10)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_298E():
        OP_96(0xFE, 0x384, 0x0, 0x6446, 0x320, 0x36B0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_298E)

    def lambda_29AC():
        OP_8E(0xFE, 0xFFFFFE5C, 0x320, 0x5BCC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_29AC)
    Sleep(80)

    def lambda_29CC():
        OP_8E(0xFE, 0x94C, 0x320, 0x5A82, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_29CC)
    WaitChrThread(0x101, 0x1)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0xFF)
    Battle(0x460, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_4_3B1 end

    def Function_5_2A04(): pass

    label("Function_5_2A04")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    OP_44(0x8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    EventBegin(0x0)
    SetChrPos(0x101, 1370, 0, 20520, 0)
    SetChrPos(0x102, -70, 0, 20470, 0)
    SetChrPos(0xF8, 1600, 0, 18950, 0)
    SetChrPos(0xF9, -70, 0, 19040, 0)
    SetChrPos(0x8, 300, 0, 28070, 180)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    OP_6D(-410, 0, 24050, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6B(4000, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #93
        0x8,
        (
            "#236F#4PUn...believable...\x02\x03",

            "To think you would actually be\x01",
            "able to break my mask...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1005F#5P*pant*...How...about that?\x01",
            "You learn something?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#1035F#5PIt seems the only thing shattered\x01",
            "here is your hubris.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C2E")

    ChrTalk(    #96
        0x105,
        (
            "#1162FNow do you understand?\x01",
            "How hope cannot be 'stolen' by men like you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D56")

    label("loc_2C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C9A")

    ChrTalk(    #97
        0x104,
        (
            "#030FDo you now see the immensity and\x01",
            "enduring power of the flame of love?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D56")

    label("loc_2C9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D56")

    ChrTalk(    #98
        0x105,
        (
            "#1162FNow do you understand?\x01",
            "How hope cannot be 'stolen' by men like you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x104,
        (
            "#030FAnd do you now see the immensity and\x01",
            "enduring power of the flame of love?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DC1")

    ChrTalk(    #100
        0x10F,
        (
            "#178FIf you've learned your lesson, never dare\x01",
            "to show your face to Her Highness again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC1")


    ChrTalk(    #101
        0x8,
        (
            "#236F#4P...\x02\x03",

            "#237FVery well. I shall...leave you to it.\x02\x03",

            "Do remember, however: Weissmann's game\x01",
            "has only just begun.\x02\x03",

            "Do not expect your luck to carry\x01",
            "you any further than this.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x8, 8)
    OP_0D()
    Sleep(100)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    def lambda_2EB3():
        OP_6D(-410, 0, 25050, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2EB3)

    def lambda_2ECB():
        OP_67(0, 4800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ECB)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(3000)

    ChrTalk(    #102
        0x8,
        (
            "#238F#4PThat said, I do...hope you continue to\x01",
            "succeed. You bested me, after all.\x02\x03",

            "Go. Overcome the walls of despair that\x01",
            "will rise before you, and let your beauty\x01",
            "shine forth all the greater.\x02\x03",

            "Well, then. Adieu.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    OP_82(0x0, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x6)
    Sleep(1500)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #103
        0x101,
        "#1026F#5PIs he really gone?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #104
        0x102,
        (
            "#1035F#5PIt looks like it, yeah.\x02\x03",

            "#1040FHe IS honorable, in his own way.\x01",
            "I don't think he'll try to stop us again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1025F#5PI guess so, yeah.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_312F")

    ChrTalk(    #106
        0x104,
        (
            "#031F#5PAh... You may have been a foe, but bravo.\x01",
            "That was an exit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_312F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315C")

    ChrTalk(    #107
        0x105,
        "#1168F#5PThat's a relief.\x02",
    )

    CloseMessageWindow()

    label("loc_315C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_318C")

    ChrTalk(    #108
        0x10B,
        "#210F#5PPfft, what a nut.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32AA")

    label("loc_318C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31DC")

    ChrTalk(    #109
        0x103,
        "#524F#5P*sigh* And he just has to get the last word in...\x02",
    )

    CloseMessageWindow()
    Jump("loc_32AA")

    label("loc_31DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3220")

    ChrTalk(    #110
        0x106,
        "#051F#5PWhatever. At least that clown's done.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32AA")

    label("loc_3220")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_325D")

    ChrTalk(    #111
        0x108,
        "#071F#5PHaha! It ends well, I suppose.\x02",
    )

    CloseMessageWindow()
    Jump("loc_32AA")

    label("loc_325D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32AA")

    ChrTalk(    #112
        0x110,
        (
            "#272FHmph. Even more of a fuss than\x01",
            "that nitwit kicks up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32F3")

    ChrTalk(    #113
        0x109,
        "#1068F#5PPhew! Glad we're done with him, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3335")

    label("loc_32F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3335")

    ChrTalk(    #114
        0x107,
        "#067F#5PHeehee! He was sorta nice, at the end.\x02",
    )

    CloseMessageWindow()

    label("loc_3335")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3383")

    ChrTalk(    #115
        0x10F,
        (
            "#176FPhew!\x02\x03",

            "(That's one concern out of\x01",
            "the way, at least.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3383")


    def lambda_3389():
        OP_6D(340, 0, 21000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3389)

    def lambda_33A1():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33A1)

    def lambda_33B9():
        OP_6B(3760, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_33B9)
    WaitChrThread(0x101, 0x0)
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
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #116
        0x102,
        (
            "#1040F#6PAll that's left to do is fiddle with\x01",
            "the terminal over there.\x02\x03",

            "I can't imagine Bleublanc lied.\x01",
            "It SHOULD let us access the upper levels.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #117
        0x101,
        "#1006F#4PCome on, then!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34D8")
    OP_A2(0x223F)

    label("loc_34D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E9")
    OP_A2(0x2241)

    label("loc_34E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34FA")
    OP_A2(0x22D8)

    label("loc_34FA")

    OP_A2(0x2232)
    OP_28(0x9F, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_5_2A04 end

    def Function_6_3506(): pass

    label("Function_6_3506")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_6_3506 end

    def Function_7_354E(): pass

    label("Function_7_354E")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 1)
    SetChrPos(0xFE, -2900, 15000, 20260, 45)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3574():
        OP_96(0xFE, 0xFFFFF4AC, 0x320, 0x4F24, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3574)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)

    def lambda_35B6():

        label("loc_35B6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_35B6")

    QueueWorkItem2(0xFE, 3, lambda_35B6)
    Return()

    # Function_7_354E end

    def Function_8_35C4(): pass

    label("Function_8_35C4")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 1)
    SetChrPos(0xFE, 5630, 15000, 19970, 315)
    ClearChrFlags(0xFE, 0x80)

    def lambda_35EA():
        OP_96(0xFE, 0x15FE, 0x320, 0x4E02, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35EA)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)

    def lambda_362C():

        label("loc_362C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_362C")

    QueueWorkItem2(0xFE, 3, lambda_362C)
    Return()

    # Function_8_35C4 end

    def Function_9_363A(): pass

    label("Function_9_363A")

    SetChrPos(0xFE, 870, 0, -25040, 0)
    OP_8E(0xFE, 0x366, 0x0, 0xFFFFB988, 0xBB8, 0x0)
    Return()

    # Function_9_363A end

    def Function_10_3660(): pass

    label("Function_10_3660")

    SetChrPos(0xFE, -390, 0, -25050, 0)
    OP_8E(0xFE, 0xFFFFFE7A, 0x0, 0xFFFFB97E, 0xBB8, 0x0)
    Return()

    # Function_10_3660 end

    def Function_11_3686(): pass

    label("Function_11_3686")

    SetChrPos(0xFE, 1150, 0, -26400, 0)
    OP_8E(0xFE, 0x47E, 0x0, 0xFFFFB438, 0xBB8, 0x0)
    Return()

    # Function_11_3686 end

    def Function_12_36AC(): pass

    label("Function_12_36AC")

    SetChrPos(0xFE, -210, 0, -26410, 0)
    OP_8E(0xFE, 0xFFFFFF2E, 0x0, 0xFFFFB42E, 0xBB8, 0x0)
    Return()

    # Function_12_36AC end

    def Function_13_36D2(): pass

    label("Function_13_36D2")

    OP_8E(0xFE, 0x23A, 0x0, 0x1162, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_13_36D2 end

    def Function_14_3701(): pass

    label("Function_14_3701")

    OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0x1068, 0xFA0, 0x0)
    Return()

    # Function_14_3701 end

    def Function_15_3716(): pass

    label("Function_15_3716")

    OP_8E(0xFE, 0x3C0, 0x0, 0xBC2, 0xFA0, 0x0)
    Return()

    # Function_15_3716 end

    def Function_16_372B(): pass

    label("Function_16_372B")

    OP_8E(0xFE, 0xFFFFFE66, 0x0, 0xB86, 0xFA0, 0x0)
    Return()

    # Function_16_372B end

    def Function_17_3740(): pass

    label("Function_17_3740")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #118
        "\x07\x05Barrier to upper levels and transport gate now unlocked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5301   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3740 end

    def Function_18_37B6(): pass

    label("Function_18_37B6")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37CD")
    Call(0, 19)
    Call(0, 20)

    label("loc_37CD")

    OP_6D(-390, 0, 32400, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 920, 0, 31200, 0)
    SetChrPos(0x102, -200, 0, 31200, 0)
    SetChrPos(0xF8, 1490, 0, 29660, 0)
    SetChrPos(0xF9, -40, 0, 29880, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #119
        "\x07\x05Barrier to upper levels and transport gate now unlocked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_71(0x1, 0x4)
    OP_0D()
    Sleep(500)
    OP_64(0x0, 0x1)
    OP_A2(0x2233)
    OP_28(0x9F, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_18_37B6 end

    def Function_19_38D1(): pass

    label("Function_19_38D1")

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
        (0, "loc_394A"),
        (1, "loc_3950"),
        (SWITCH_DEFAULT, "loc_3956"),
    )


    label("loc_394A")

    OP_A2(0x1200)
    Jump("loc_3956")

    label("loc_3950")

    OP_A2(0x1201)
    Jump("loc_3956")

    label("loc_3956")

    Return()

    # Function_19_38D1 end

    def Function_20_3957(): pass

    label("Function_20_3957")

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

    # Function_20_3957 end

    SaveToFile()

Try(main)
