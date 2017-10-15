from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5315   ._SN',
        MapName             = 'Other',
        Location            = 'C5315.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60035",
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
        'Dragion ①',                           # 9
        'Dragion ②',                           # 10
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_EA",           # 00, 0
        "Function_1_F9",           # 01, 1
        "Function_2_11E",          # 02, 2
        "Function_3_127",          # 03, 3
        "Function_4_2F95",         # 04, 4
        "Function_5_35F7",         # 05, 5
        "Function_6_361B",         # 06, 6
        "Function_7_363F",         # 07, 7
        "Function_8_3663",         # 08, 8
        "Function_9_36E9",         # 09, 9
    )


    def Function_0_EA(): pass

    label("Function_0_EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_F8")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_F8")

    Return()

    # Function_0_EA end

    def Function_1_F9(): pass

    label("Function_1_F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x450), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xEB, 0x1, 0x64)

    label("loc_113")

    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    Return()

    # Function_1_F9 end

    def Function_2_11E(): pass

    label("Function_2_11E")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_11E end

    def Function_3_127(): pass

    label("Function_3_127")

    EventBegin(0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_163")
    Call(0, 8)
    Call(0, 9)
    RemoveParty(0x1, 0xFF)

    label("loc_163")

    OP_D2(0x270110, 0x270120, 0x0)
    OP_D2(0x270111, 0x270121, 0x1)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_1A8"),
        (5, "loc_1BF"),
        (3, "loc_1D6"),
        (4, "loc_1ED"),
        (6, "loc_204"),
        (7, "loc_21B"),
        (8, "loc_232"),
        (10, "loc_249"),
        (14, "loc_260"),
        (15, "loc_277"),
        (SWITCH_DEFAULT, "loc_28E"),
    )


    label("loc_1A8")

    OP_D2(0x701D0, 0x701DC, 0x2)
    OP_D2(0x701D1, 0x701DD, 0x3)
    Jump("loc_28E")

    label("loc_1BF")

    OP_D2(0x70218, 0x70224, 0x2)
    OP_D2(0x70219, 0x70225, 0x3)
    Jump("loc_28E")

    label("loc_1D6")

    OP_D2(0x701E8, 0x701F4, 0x2)
    OP_D2(0x701E9, 0x701F5, 0x3)
    Jump("loc_28E")

    label("loc_1ED")

    OP_D2(0x27036E, 0x27037B, 0x2)
    OP_D2(0x27036F, 0x27037C, 0x3)
    Jump("loc_28E")

    label("loc_204")

    OP_D2(0x70230, 0x7023C, 0x2)
    OP_D2(0x70231, 0x7023D, 0x3)
    Jump("loc_28E")

    label("loc_21B")

    OP_D2(0x70248, 0x70254, 0x2)
    OP_D2(0x70249, 0x70255, 0x3)
    Jump("loc_28E")

    label("loc_232")

    OP_D2(0x270176, 0x270183, 0x2)
    OP_D2(0x270177, 0x270184, 0x3)
    Jump("loc_28E")

    label("loc_249")

    OP_D2(0x702B4, 0x702BB, 0x2)
    OP_D2(0x702B5, 0x702BC, 0x3)
    Jump("loc_28E")

    label("loc_260")

    OP_D2(0x2702D6, 0x2702E0, 0x2)
    OP_D2(0x2702D7, 0x2702E1, 0x3)
    Jump("loc_28E")

    label("loc_277")

    OP_D2(0x2702C2, 0x2702CC, 0x2)
    OP_D2(0x2702C3, 0x2702CD, 0x3)
    Jump("loc_28E")

    label("loc_28E")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2BF"),
        (5, "loc_2D6"),
        (3, "loc_2ED"),
        (4, "loc_304"),
        (6, "loc_31B"),
        (7, "loc_332"),
        (8, "loc_349"),
        (10, "loc_360"),
        (14, "loc_377"),
        (15, "loc_38E"),
        (SWITCH_DEFAULT, "loc_3A5"),
    )


    label("loc_2BF")

    OP_D2(0x701D0, 0x701DC, 0x4)
    OP_D2(0x701D1, 0x701DD, 0x5)
    Jump("loc_3A5")

    label("loc_2D6")

    OP_D2(0x70218, 0x70224, 0x4)
    OP_D2(0x70219, 0x70225, 0x5)
    Jump("loc_3A5")

    label("loc_2ED")

    OP_D2(0x701E8, 0x701F4, 0x4)
    OP_D2(0x701E9, 0x701F5, 0x5)
    Jump("loc_3A5")

    label("loc_304")

    OP_D2(0x27036E, 0x27037B, 0x4)
    OP_D2(0x27036F, 0x27037C, 0x5)
    Jump("loc_3A5")

    label("loc_31B")

    OP_D2(0x70230, 0x7023C, 0x4)
    OP_D2(0x70231, 0x7023D, 0x5)
    Jump("loc_3A5")

    label("loc_332")

    OP_D2(0x70248, 0x70254, 0x4)
    OP_D2(0x70249, 0x70255, 0x5)
    Jump("loc_3A5")

    label("loc_349")

    OP_D2(0x270176, 0x270183, 0x4)
    OP_D2(0x270177, 0x270184, 0x5)
    Jump("loc_3A5")

    label("loc_360")

    OP_D2(0x702B4, 0x702BB, 0x4)
    OP_D2(0x702B5, 0x702BC, 0x5)
    Jump("loc_3A5")

    label("loc_377")

    OP_D2(0x2702D6, 0x2702E0, 0x4)
    OP_D2(0x2702D7, 0x2702E1, 0x5)
    Jump("loc_3A5")

    label("loc_38E")

    OP_D2(0x2702C2, 0x2702CC, 0x4)
    OP_D2(0x2702C3, 0x2702CD, 0x5)
    Jump("loc_3A5")

    label("loc_3A5")

    StopSound(0x7530, 0x493E0, 0x0)
    OP_6D(270, 1350, 1450, 0)
    OP_67(0, 12650, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(27000, 0)
    OP_6E(514, 0)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x10E)
    SetChrPos(0x101, 0, 1350, 1000, 0)
    SetChrPos(0xF8, -1000, 1350, -1000, 225)
    SetChrPos(0xF9, 1000, 1350, -1000, 135)
    FadeToBright(1000, 0)
    StopSound(0x7530, 0x27100, 0x1F40)

    def lambda_44C():
        OP_6D(300, 1350, -10, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44C)

    def lambda_464():
        OP_67(0, 7550, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_464)

    def lambda_47C():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_47C)

    def lambda_48C():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_48C)

    def lambda_49C():
        OP_6E(320, 8000)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_49C)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_523")

    ChrTalk(    #0
        0x10B,
        (
            "#212FI didn't really think this was an\x01",
            "elevator shaft...\x02\x03",

            "How far down do you think it goes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_523")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_590")

    ChrTalk(    #1
        0x110,
        (
            "#276FDidn't think this would be an\x01",
            "elevator shaft.\x02\x03",

            "Seems to go down very, very far...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_590")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F5")

    ChrTalk(    #2
        0x106,
        (
            "#057FDidn't think this'd be an elevator shaft.\x02\x03",

            "How deep do you think it goes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_5F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66C")

    ChrTalk(    #3
        0x103,
        (
            "#022FI never would have imagined this\x01",
            "was an elevator shaft.\x02\x03",

            "How far down do you think it goes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_66C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DF")

    ChrTalk(    #4
        0x105,
        (
            "#1163FI would not have thought this was\x01",
            "an elevator shaft...\x02\x03",

            "I wonder how far down it goes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_6DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_755")

    ChrTalk(    #5
        0x104,
        (
            "#032FTo think this was an elevator shaft...\x02\x03",

            "It must plunge into the very center\x01",
            "of the island.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_755")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B6")

    ChrTalk(    #6
        0x10F,
        (
            "#178FAn elevator shaft... What a surprise.\x02\x03",

            "I wonder how far down it goes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_7B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_824")

    ChrTalk(    #7
        0x109,
        (
            "#1063FSure didn't have this pegged for an\x01",
            "elevator shaft.\x02\x03",

            "Gotta wonder how deep it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_824")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_891")

    ChrTalk(    #8
        0x108,
        (
            "#072FI did not think this would be an\x01",
            "elevator shaft.\x02\x03",

            "How far does it go down, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_891")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_931")

    ChrTalk(    #9
        0x107,
        (
            "#063FHmmmm. The Axis Pillar is really tall,\x01",
            "so it's gotta be really deep.\x02\x03",

            "It probably goes go all the way to\x01",
            "the center of the island...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D3")

    ChrTalk(    #10
        0x108,
        (
            "#072F#6PConsidering the height of the Axis Pillar,\x01",
            "it must be incredibly deep.\x02\x03",

            "I suspect it goes all the way to the\x01",
            "center of this island.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_9D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4B")

    ChrTalk(    #11
        0x109,
        (
            "#1063FWell, given how tall the pillar is...\x02\x03",

            "I bet this thing runs into the middle\x01",
            "of the island.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF0")

    ChrTalk(    #12
        0x10F,
        (
            "#178FConsidering the height of the Axis Pillar,\x01",
            "it must be incredibly deep.\x02\x03",

            "It must, at a minimum, cover the\x01",
            "entirety of the pillar's height.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B92")

    ChrTalk(    #13
        0x104,
        (
            "#032FAt the very least, it must cover the\x01",
            "entirety of the height of the pillar.\x02\x03",

            "I fear it goes down to the center of\x01",
            "this floating island.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_B92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C26")

    ChrTalk(    #14
        0x105,
        (
            "#1163FIt must, at a minimum, cover the\x01",
            "entirety of the pillar's height.\x02\x03",

            "And I suspect it goes even deeper\x01",
            "into the island...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_C26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBE")

    ChrTalk(    #15
        0x103,
        (
            "#022FOne would imagine it goes down past the\x01",
            "height of the Axis Pillar.\x02\x03",

            "I wouldn't be surprised if it goes deep\x01",
            "into the island.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_CBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D43")

    ChrTalk(    #16
        0x106,
        (
            "#057FProbably at least as deep as the tower is tall.\x02\x03",

            "Bet this thing goes right into the middle\x01",
            "of the island.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_D43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBC")

    ChrTalk(    #17
        0x110,
        (
            "#270FI would imagine it runs the length of\x01",
            "the tower.\x02\x03",

            "It must run straight into the island, as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBC")


    ChrTalk(    #18
        0x101,
        "#1003F#6PYeah...\x02",
    )

    CloseMessageWindow()

    def lambda_DD8():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_DD8)
    Sleep(100)
    OP_8C(0xF9, 0, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1142")

    ChrTalk(    #19
        0x105,
        (
            "#1162FEstelle...don't worry.\x02\x03",

            "Joshua promised to walk by your side until\x01",
            "the end, didn't he?\x02\x03",

            "#1168FYou will bring him back to us.\x01",
            "I know you will.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #20
        0x101,
        (
            "#1025F#6PKloe...thanks.\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x105,
        "#1161FHaha! Yes!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFC")

    ChrTalk(    #22
        0x110,
        "#275FHeh, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_113F")

    label("loc_FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1032")

    ChrTalk(    #23
        0x108,
        "#071F#7PYes, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_113F")

    label("loc_1032")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1066")

    ChrTalk(    #24
        0x10F,
        "#171FHaha! That's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_113F")

    label("loc_1066")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109F")

    ChrTalk(    #25
        0x106,
        "#051FHell yeah. That's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_113F")

    label("loc_109F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D9")

    ChrTalk(    #26
        0x109,
        "#1061FHah, yeah, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_113F")

    label("loc_10D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1112")

    ChrTalk(    #27
        0x103,
        "#021FAll right! That's my Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_113F")

    label("loc_1112")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113F")

    ChrTalk(    #28
        0x107,
        "#061FHeehee! Go, Estelle!\x02",
    )

    CloseMessageWindow()

    label("loc_113F")

    Jump("loc_2594")

    label("loc_1142")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(    #29
        0x10B,
        (
            "#214FOh, come ON!\x01",
            "What are you looking so torn up for?!\x02\x03",

            "What, you think Joshua won't overcome\x01",
            "that glasses-wearing creep for you?\x02\x03",

            "He'll come back! Believe in him!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #30
        0x101,
        (
            "#1025F#6PJosette...\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10B,
        "#211FYeah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1354")

    ChrTalk(    #32
        0x110,
        "#275FHeh, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_1354")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138A")

    ChrTalk(    #33
        0x108,
        "#071F#7PYes, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_138A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BE")

    ChrTalk(    #34
        0x10F,
        "#171FHaha! That's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_13BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F7")

    ChrTalk(    #35
        0x106,
        "#051FHell yeah. That's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_13F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1431")

    ChrTalk(    #36
        0x109,
        "#1061FHah, yeah, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_1431")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_146A")

    ChrTalk(    #37
        0x103,
        "#021FAll right! That's my Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_146A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1497")

    ChrTalk(    #38
        0x107,
        "#061FHeehee! Go, Estelle!\x02",
    )

    CloseMessageWindow()

    label("loc_1497")

    Jump("loc_2594")

    label("loc_149A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1750")

    ChrTalk(    #39
        0x10B,
        (
            "#214FOh, come ON!\x01",
            "What are you looking so torn up for?!\x02\x03",

            "What, you think Joshua won't overcome\x01",
            "that glasses-wearing creep for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        (
            "#1168FBesides, Joshua promised to walk by your\x01",
            "side until the end, didn't he?\x02\x03",

            "You will bring him back to us.\x01",
            "I know you will.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1025F#6PAww, Kloe, Josette...\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1718")

    ChrTalk(    #42
        0x105,
        "#1161F#1K#1PHaha! Yes!\x02",
    )


    ChrTalk(    #43
        0x10B,
        "#211F#1KHeck yeah!\x02",
    )

    Jump("loc_174A")

    label("loc_1718")


    ChrTalk(    #44
        0x105,
        "#1161F#1KHaha! Yes!\x02",
    )


    ChrTalk(    #45
        0x10B,
        "#211F#1K#1PHeck yeah!\x02",
    )


    label("loc_174A")

    OP_56(0x1)
    OP_59()
    Jump("loc_2594")

    label("loc_1750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1907")

    ChrTalk(    #46
        0x107,
        (
            "#062FEstelle... Umm, don't worry, okay?\x02\x03",

            "Joshua promised to stay with you\x01",
            "forever and ever, right?\x02\x03",

            "#560FHe'll come back! I know he will!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #47
        0x101,
        (
            "#1025F#6PD'aww, Tita...thanks.\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_1907")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AE2")

    ChrTalk(    #48
        0x103,
        (
            "#026FEstelle...don't worry, all right?\x02\x03",

            "#027FOur little wayward assassin promised\x01",
            "he'd stay with you forever, didn't he?\x02\x03",

            "Since when have you known him to\x01",
            "break his word, hmmmmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #49
        0x101,
        (
            "#1025F#6PSchera...thanks.\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_1AE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB5")

    ChrTalk(    #50
        0x109,
        (
            "#1065FEstelle, don't worry, all right?\x02\x03",

            "#1060FHe promised he'd stay with you\x01",
            "to the end, right?\x02\x03",

            "So don't worry. He'll come back.\x01",
            "I got a good feeling, you might say.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #51
        0x101,
        (
            "#1025F#6PAww, Kevin...thanks.\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_1CB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E99")

    ChrTalk(    #52
        0x106,
        (
            "#053FC'mon, Estelle. This ain't you.\x02\x03",

            "#556FDidn't you two promise each other you'd\x01",
            "stay together until the end or somethin'?\x02\x03",

            "That kid doesn't know HOW to break promise.\x01",
            "He'll come around.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #53
        0x101,
        (
            "#1025F#6PAgate...thanks.\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_1E99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207D")

    ChrTalk(    #54
        0x10F,
        (
            "#176FEstelle, do not worry.\x01",
            "He spent time in General Bright's care.\x02\x03",

            "#170FIt seems clear to me that he learned from\x01",
            "the general not to forsake a promise.\x02\x03",

            "He will return to us.\x01",
            "Believe in him.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #55
        0x101,
        (
            "#1025FThanks, Julia.\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_207D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_224B")

    ChrTalk(    #56
        0x108,
        (
            "#074FEstelle. Do not despair.\x02\x03",

            "#070FDid he not promise to walk The Way\x01",
            "with you, for the rest of time?\x02\x03",

            "So do not fear! I cannot imagine he would\x01",
            "forsake that so easily.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #57
        0x101,
        (
            "#1025F#6PThanks, Zin.\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_224B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2421")

    ChrTalk(    #58
        0x110,
        (
            "#272FThere's no need for that face, Ms. Bright.\x02\x03",

            "#277FYou and he have overcome countless\x01",
            "struggles together.\x02\x03",

            "This is simply one last struggle.\x01",
            "Look it in the eye and overcome it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #59
        0x101,
        (
            "#1025FThanks, Mueller.\x02\x03",

            "#1012FYeah... He'll never break a promise\x01",
            "if he can help it.\x02\x03",

            "#1019FBesides, like heck I'm just gonna abandon\x01",
            "him and let that creep Weissmann do what\x01",
            "he wants with MY Joshua.\x02\x03",

            "#1005FIt's time to take back my man with\x01",
            "GIRL POWER!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2421")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2454")

    ChrTalk(    #60
        0x110,
        "#275FHeh, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2594")

    label("loc_2454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2487")

    ChrTalk(    #61
        0x108,
        "#071FYes, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2594")

    label("loc_2487")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24BB")

    ChrTalk(    #62
        0x10F,
        "#171FHaha! That's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2594")

    label("loc_24BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F4")

    ChrTalk(    #63
        0x106,
        "#051FHell yeah. That's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2594")

    label("loc_24F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_252E")

    ChrTalk(    #64
        0x109,
        "#1061FHah, yeah, that's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2594")

    label("loc_252E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2567")

    ChrTalk(    #65
        0x103,
        "#021FAll right! That's my Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2594")

    label("loc_2567")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2594")

    ChrTalk(    #66
        0x107,
        "#061FHeehee! Go, Estelle!\x02",
    )

    CloseMessageWindow()

    label("loc_2594")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2663")

    ChrTalk(    #67
        0x104,
        (
            "#031FAnd never fear! Should things possibly\x01",
            "go wrong, I shall intervene!\x02\x03",

            "The overwhelming power of my love\x01",
            "shall return Joshua to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1016F#6PYeah, I...bet.\x01",
            "Haha...Thanks, Olivier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2663")

    OP_22(0x158, 0x1, 0x64)

    def lambda_266E():

        label("loc_266E")

        OP_7C(0xA, 0xA, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_266E")

    QueueWorkItem2(0x101, 2, lambda_266E)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C1")
    OP_62(0xF8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_26F5")

    label("loc_26C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E3")
    OP_62(0xF8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_26F5")

    label("loc_26E3")

    OP_62(0xF8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_26F5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271C")
    OP_62(0xF9, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_2750")

    label("loc_271C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273E")
    OP_62(0xF9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_2750")

    label("loc_273E")

    OP_62(0xF9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_2750")

    Sleep(1000)

    ChrTalk(    #69
        0x101,
        "#1020F#6PHuh...? What's that?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_279C")

    ChrTalk(    #70
        0x107,
        "#065FOh, no!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_279C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27BF")

    ChrTalk(    #71
        0x105,
        "#1163FNo...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_27BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E4")

    ChrTalk(    #72
        0x10B,
        "#216FAw, nuts!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_27E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2807")

    ChrTalk(    #73
        0x103,
        "#023FOh, no!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_2807")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2831")

    ChrTalk(    #74
        0x109,
        "#1063FOhhh, hell...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_2831")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2852")

    ChrTalk(    #75
        0x110,
        "#273FDamn!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_2852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287A")

    ChrTalk(    #76
        0x10F,
        "#178FDamn it all!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_287A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_289C")

    ChrTalk(    #77
        0x104,
        "#032FBlast!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_289C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28BE")

    ChrTalk(    #78
        0x106,
        "#052FAw, hell!\x02",
    )

    CloseMessageWindow()

    label("loc_28BE")

    OP_DB()
    Sleep(200)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(270, 1350, 1450, 0)
    OP_67(0, 12650, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(27000, 0)
    OP_6E(514, 0)
    OP_6F(0x1, 30)
    OP_70(0x1, 0x10E)

    def lambda_2928():
        OP_6D(-650, 6000, 5500, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2928)

    def lambda_2940():
        OP_67(0, 4600, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2940)

    def lambda_2958():
        OP_6B(3880, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2958)

    def lambda_2968():
        OP_6C(27000, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2968)

    def lambda_2978():
        OP_6E(449, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_2978)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 0, 30000, 15980, 180)
    ClearChrFlags(0x8, 0x100)
    OP_D1(8, 0, -45000, 0, 100)
    OP_72(0x0, 0x4)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 320)
    OP_70(0x0, 0x154)

    def lambda_29D2():
        OP_8F(0xFE, 0x0, 0x3E8, 0x3E6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29D2)

    def lambda_29ED():
        OP_D1(254, 0, 180000, 0, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_29ED)

    def lambda_2A07():
        OP_97(0xFE, 0xFFFFFFA6, 0x118, 0xB2390, 0x61A8, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2A07)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 0)
    Sleep(150)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 2)
    Sleep(100)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 4)

    def lambda_2A50():

        label("loc_2A50")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2A50")

    QueueWorkItem2(0x101, 0, lambda_2A50)

    def lambda_2A61():

        label("loc_2A61")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2A61")

    QueueWorkItem2(0xF8, 0, lambda_2A61)

    def lambda_2A72():

        label("loc_2A72")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2A72")

    QueueWorkItem2(0xF9, 0, lambda_2A72)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)

    def lambda_2A92():
        OP_8F(0xFE, 0xFFFFFF1A, 0x7D0, 0x17CA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A92)

    def lambda_2AAD():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2AAD)
    OP_D8(0x0, 0x12C)
    OP_B0(0x0, 0xF)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 25)
    OP_70(0x0, 0x23)
    OP_73(0x0)
    OP_D8(0x0, 0x12C)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x14)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(1320, 2560, 4050, 0)
    OP_67(0, 2000, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(33000, 0)
    OP_6E(423, 0)
    OP_A1(0x9, 0x2)
    SetChrPos(0x9, -230, 2000, 6090, 0)
    ClearChrFlags(0x9, 0x100)
    OP_72(0x2, 0x4)
    OP_72(0x2, 0x20)
    OP_B0(0x2, 0xF)
    OP_6F(0x2, 300)
    OP_71(0x0, 0x4)
    OP_8C(0x9, 180, 0)

    def lambda_2B90():
        OP_8F(0xFE, 0xFFFFFEF2, 0x546, 0x1748, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B90)
    OP_6F(0x2, 300)
    OP_70(0x2, 0x136)
    OP_43(0xF9, 0x0, 0x0, 0x7)
    Sleep(30)
    OP_43(0xF8, 0x0, 0x0, 0x6)
    Sleep(50)
    OP_43(0x101, 0x0, 0x0, 0x5)
    WaitChrThread(0x9, 0x1)
    OP_23(0x158)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0xBB8, 0x3E8)
    OP_44(0x101, 0x2)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x14)
    Sleep(1000)
    OP_DC()

    ChrTalk(    #79
        0x101,
        (
            "#1020F#2PThere's MORE of those dragon things?\x02\x03",

            "#1002FWe really do need to be ready for anything.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CAE")

    ChrTalk(    #80
        0x108,
        "#076F#2PRight! Let's get serious!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2CAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CE9")

    ChrTalk(    #81
        0x106,
        "#054F#2PDamn right. Bring it ALL on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2CE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D2F")

    ChrTalk(    #82
        0x104,
        "#035F#2PHeh. A fitting opening for a final act.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D70")

    ChrTalk(    #83
        0x10F,
        "#177FVery well! It is time to get serious!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2D70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DA7")

    ChrTalk(    #84
        0x110,
        "#277FHmph! It's only just begun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2DA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DE3")

    ChrTalk(    #85
        0x109,
        "#1069F#2PYeah! Let's bust some heads!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2DE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E16")

    ChrTalk(    #86
        0x103,
        "#024F#2PYes. Let's be ready!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2E16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E5B")

    ChrTalk(    #87
        0x10B,
        "#214F#2PYeah! Totally time to bust some heads!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2E5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E98")

    ChrTalk(    #88
        0x105,
        "#1162F#2PYes... The true test begins now!\x02",
    )

    CloseMessageWindow()

    label("loc_2E98")

    OP_22(0xF3, 0x0, 0x64)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 320)
    OP_70(0x2, 0x154)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 340)
    OP_70(0x2, 0x15E)

    def lambda_2ECC():
        OP_6D(810, 1350, 5810, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ECC)

    def lambda_2EE4():
        OP_67(0, 4710, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EE4)

    def lambda_2EFC():
        OP_6B(2440, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2EFC)

    def lambda_2F0C():
        OP_8F(0xFE, 0xFFFFFEFC, 0x546, 0x92E, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F0C)

    def lambda_2F27():
        OP_8F(0xFE, 0xFFFFF8DA, 0x546, 0x5A0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_2F27)

    def lambda_2F42():
        OP_8F(0xFE, 0x230, 0x546, 0x50A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_2F42)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_23(0x1C3)
    OP_23(0xEB)
    OP_23(0x79)
    OP_23(0x158)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x191), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x450, 0x0, 0x0, 0x80, 0xFF)
    Return()

    # Function_3_127 end

    def Function_4_2F95(): pass

    label("Function_4_2F95")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    OP_DB()
    OP_D2(0x270110, 0x270120, 0x0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_2FE9"),
        (5, "loc_2FF6"),
        (3, "loc_3003"),
        (4, "loc_3010"),
        (6, "loc_301D"),
        (7, "loc_302A"),
        (8, "loc_3037"),
        (10, "loc_3044"),
        (14, "loc_3051"),
        (15, "loc_305E"),
        (SWITCH_DEFAULT, "loc_306B"),
    )


    label("loc_2FE9")

    OP_D2(0x701D0, 0x701DC, 0x2)
    Jump("loc_306B")

    label("loc_2FF6")

    OP_D2(0x70218, 0x70224, 0x2)
    Jump("loc_306B")

    label("loc_3003")

    OP_D2(0x701E8, 0x701F4, 0x2)
    Jump("loc_306B")

    label("loc_3010")

    OP_D2(0x27036E, 0x27037B, 0x2)
    Jump("loc_306B")

    label("loc_301D")

    OP_D2(0x70230, 0x7023C, 0x2)
    Jump("loc_306B")

    label("loc_302A")

    OP_D2(0x70248, 0x70254, 0x2)
    Jump("loc_306B")

    label("loc_3037")

    OP_D2(0x270176, 0x270183, 0x2)
    Jump("loc_306B")

    label("loc_3044")

    OP_D2(0x702B4, 0x702BB, 0x2)
    Jump("loc_306B")

    label("loc_3051")

    OP_D2(0x2702D6, 0x2702E0, 0x2)
    Jump("loc_306B")

    label("loc_305E")

    OP_D2(0x2702C2, 0x2702CC, 0x2)
    Jump("loc_306B")

    label("loc_306B")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_309C"),
        (5, "loc_30A9"),
        (3, "loc_30B6"),
        (4, "loc_30C3"),
        (6, "loc_30D0"),
        (7, "loc_30DD"),
        (8, "loc_30EA"),
        (10, "loc_30F7"),
        (14, "loc_3104"),
        (15, "loc_3111"),
        (SWITCH_DEFAULT, "loc_311E"),
    )


    label("loc_309C")

    OP_D2(0x701D0, 0x701DC, 0x4)
    Jump("loc_311E")

    label("loc_30A9")

    OP_D2(0x70218, 0x70224, 0x4)
    Jump("loc_311E")

    label("loc_30B6")

    OP_D2(0x701E8, 0x701F4, 0x4)
    Jump("loc_311E")

    label("loc_30C3")

    OP_D2(0x27036E, 0x27037B, 0x4)
    Jump("loc_311E")

    label("loc_30D0")

    OP_D2(0x70230, 0x7023C, 0x4)
    Jump("loc_311E")

    label("loc_30DD")

    OP_D2(0x70248, 0x70254, 0x4)
    Jump("loc_311E")

    label("loc_30EA")

    OP_D2(0x270176, 0x270183, 0x4)
    Jump("loc_311E")

    label("loc_30F7")

    OP_D2(0x702B4, 0x702BB, 0x4)
    Jump("loc_311E")

    label("loc_3104")

    OP_D2(0x2702D6, 0x2702E0, 0x4)
    Jump("loc_311E")

    label("loc_3111")

    OP_D2(0x2702C2, 0x2702CC, 0x4)
    Jump("loc_311E")

    label("loc_311E")

    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 0, 1350, 2430, 0)
    OP_8C(0x8, 180, 0)
    ClearChrFlags(0x8, 0x100)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 260)
    OP_70(0x0, 0x104)
    OP_71(0x2, 0x4)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0xF8, 2)
    SetChrChipByIndex(0xF9, 4)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrPos(0x101, 0, 1350, -2880, 0)
    SetChrPos(0xF8, -820, 1350, -4370, 0)
    SetChrPos(0xF9, 820, 1350, -4370, 0)
    LoadEffect(0x1, "battle\\\\btbomb00.eff")
    LoadEffect(0x2, "monster\\\\ms30109a.eff")
    LoadEffect(0x3, "monster\\\\ms30109b.eff")
    OP_6D(-170, 3000, 3490, 0)
    OP_67(0, 2590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(308, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    FadeToBright(2000, 0)

    def lambda_324F():
        OP_6D(-170, 4019, 12490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_324F)

    def lambda_3267():
        OP_6B(4300, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3267)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 260)
    OP_70(0x0, 0x136)
    PlayEffect(0x2, 0x0, 0x8, 180, 3800, 500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 180, 2560, 1060, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x0, 0x8, 180, 2300, 1400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 460, 3000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x8, 1000, 3500, 2500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0x0, 0x8, 300, 3500, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x0, 0x8, 400, 1600, 4000, 0, 0, 0, 1300, 1067869798, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xFF, -750, 3000, 4150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x8, -1000, 3000, 5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_347F():
        OP_6D(-60, 1350, 12530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_347F)

    def lambda_3497():
        OP_67(0, 22350, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3497)

    def lambda_34AF():
        OP_6B(500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34AF)

    def lambda_34BF():
        OP_6E(513, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_34BF)
    Sleep(900)
    PlayEffect(0x1, 0xFF, 0xFF, 840, 4500, 8400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_B0(0x0, 0x5)
    PlayEffect(0x1, 0xFF, 0xFF, -900, 2560, 10090, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x101, 0, 1350, 1000, 0)
    SetChrPos(0xF8, -1000, 1350, -1000, 0)
    SetChrPos(0xF9, 1000, 1350, -1000, 0)

    def lambda_3592():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x2710, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3592)

    def lambda_35AD():
        OP_67(0, 23350, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35AD)

    def lambda_35C5():
        OP_6B(2600, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35C5)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetMapFlags(0x100000)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5314   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2F95 end

    def Function_5_35F7(): pass

    label("Function_5_35F7")

    OP_8C(0xFE, 0, 0)
    OP_96(0xFE, 0xFFFFFEB6, 0x546, 0xFFFFF344, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_5_35F7 end

    def Function_6_361B(): pass

    label("Function_6_361B")

    OP_8C(0xFE, 0, 0)
    OP_96(0xFE, 0xFFFFF90C, 0x546, 0xFFFFECBE, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_6_361B end

    def Function_7_363F(): pass

    label("Function_7_363F")

    OP_8C(0xFE, 0, 0)
    OP_96(0xFE, 0xE6, 0x546, 0xFFFFEBA6, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_7_363F end

    def Function_8_3663(): pass

    label("Function_8_3663")

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
        (0, "loc_36DC"),
        (1, "loc_36E2"),
        (SWITCH_DEFAULT, "loc_36E8"),
    )


    label("loc_36DC")

    OP_A2(0x1200)
    Jump("loc_36E8")

    label("loc_36E2")

    OP_A2(0x1201)
    Jump("loc_36E8")

    label("loc_36E8")

    Return()

    # Function_8_3663 end

    def Function_9_36E9(): pass

    label("Function_9_36E9")

    FadeToDark(0, 0, -1)
    OP_6D(-211220, -20490, -48190, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xE, 0xF, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_36E9 end

    SaveToFile()

Try(main)
