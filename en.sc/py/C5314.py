from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5314   ._SN',
        MapName             = 'Other',
        Location            = 'C5314.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60065",
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
        'エレベータ',                           # 9
        'Broken Dragion',                       # 10
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


    DeclActor(
        TriggerX            = 29120,
        TriggerZ            = 0,
        TriggerY            = 5080,
        TriggerRange        = 1200,
        ActorX              = 29120,
        ActorZ              = 0,
        ActorY              = 5080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_10E",          # 00, 0
        "Function_1_11D",          # 01, 1
        "Function_2_279",          # 02, 2
        "Function_3_E86",          # 03, 3
        "Function_4_F0C",          # 04, 4
        "Function_5_FA3",          # 05, 5
    )


    def Function_0_10E(): pass

    label("Function_0_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_11C")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_11C")

    Return()

    # Function_0_10E end

    def Function_1_11D(): pass

    label("Function_1_11D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 5)), scpexpr(EXPR_END)), "loc_135")
    OP_72(0x0, 0x8)
    OP_6F(0x0, 300)
    OP_72(0x0, 0x20)

    label("loc_135")

    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 29120, 1000, 5080, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xFA)
    Jump("loc_1AF")

    label("loc_1A3")

    OP_72(0x1, 0x20)
    OP_6F(0x1, 250)

    label("loc_1AF")

    SetChrPos(0x9, 4500, -9000, 24000, 260)
    OP_A1(0x9, 0x2)
    OP_72(0x2, 0x4)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 1150)
    LoadEffect(0x2, "map\\\\mpsmk0.eff")
    LoadEffect(0x3, "Scraft\\\\sc000_31.eff")
    PlayEffect(0x2, 0xFF, 0x9, 4500, 3200, -3200, 0, 0, 0, 800, 1000, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x9, 11500, 2000, -200, 0, 0, 0, 1600, 1800, 1600, 0xFF, 0, 0, 0, 0)
    SetMapFlags(0x2000000)
    OP_E8(0xD0, 0x7, 0x0, 0x0)
    Return()

    # Function_1_11D end

    def Function_2_279(): pass

    label("Function_2_279")

    EventBegin(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_294")
    Call(0, 3)
    Call(0, 4)
    RemoveParty(0x1, 0xFF)

    label("loc_294")

    OP_6D(12460, 4000, 12240, 0)
    OP_67(0, 12140, -10000, 0)
    OP_6B(10700, 0)
    OP_6C(45000, 0)
    OP_6E(221, 0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x14A)
    OP_48()
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_89(0x101, 880, 40000, 130, 90)
    OP_89(0xF8, -410, 40000, -520, 90)
    OP_89(0xF9, -330, 40000, 620, 90)
    OP_22(0xEB, 0x1, 0x64)
    ClearMapFlags(0x100000)
    FadeToBright(2000, 0)

    def lambda_340():
        OP_6D(1960, 10, 2380, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_340)

    def lambda_358():
        OP_67(0, 6930, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_358)
    OP_C8(0x200, 0x46, "C_PLAC28._CH", 0x0, 0x5DC)
    OP_73(0x0)
    OP_23(0xEB)
    OP_22(0xC8, 0x0, 0x64)

    def lambda_390():
        OP_7C(0x0, 0x64, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_390)
    OP_6F(0x0, 330)
    OP_70(0x0, 0x12C)
    OP_73(0x0)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(220, 710, 270, 0)
    OP_67(0, 8310, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(45000, 0)
    OP_6E(221, 0)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #0
        0x101,
        (
            "#1007F#6PI guess this is the end of the line...\x02\x03",

            "#1002FSo this is the Core Sector, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BF")

    ChrTalk(    #1
        0x110,
        (
            "#270FYou can feel the air humming with\x01",
            "power ahead...\x02\x03",

            "There's no mistake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804")

    label("loc_4BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_537")

    ChrTalk(    #2
        0x104,
        (
            "#032FYes... Do you feel how the air pulses\x01",
            "with barely-contained power?\x02\x03",

            "There can be no mistake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804")

    label("loc_537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A5")

    ChrTalk(    #3
        0x109,
        (
            "#1065FYeah. You feel that power in the air?\x02\x03",

            "#1063FDon't think there's any mistake now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804")

    label("loc_5A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_604")

    ChrTalk(    #4
        0x103,
        (
            "#026FWhat power... You can feel it in the air.\x02\x03",

            "#022FThere's no mistake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804")

    label("loc_604")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_676")

    ChrTalk(    #5
        0x105,
        (
            "#1167FThe air positively throbs with energy...\x02\x03",

            "#1162FI think this must be our destination.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804")

    label("loc_676")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E1")

    ChrTalk(    #6
        0x106,
        (
            "#053FDamn.\x01",
            "Can you feel all the power in the air?\x02\x03",

            "#057FLooks like this is our stop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804")

    label("loc_6E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_749")

    ChrTalk(    #7
        0x108,
        (
            "#074FCan you feel the chi flowing\x01",
            "through the air?\x02\x03",

            "#072FThis is our destination.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804")

    label("loc_749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A9")

    ChrTalk(    #8
        0x10F,
        (
            "#176FThere's such power in the air...\x02\x03",

            "#178FThis must be our destination.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_804")

    label("loc_7A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_804")

    ChrTalk(    #9
        0x10B,
        (
            "#216FHoly crap, can you feel that in the air?\x02\x03",

            "#212FThis's gotta be it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_804")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_854")

    ChrTalk(    #10
        0x107,
        (
            "#062FSo, so Joshua and the Aureole are\x01",
            "just ahead, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA4")

    label("loc_854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_898")

    ChrTalk(    #11
        0x10B,
        "#212FSo Joshua and the Aureole're just ahead.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA4")

    label("loc_898")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DD")

    ChrTalk(    #12
        0x10F,
        "#178FSo. The Aureole and Joshua must be ahead.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA4")

    label("loc_8DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91E")

    ChrTalk(    #13
        0x108,
        "#072FThe Aureole and Joshua must be ahead.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA4")

    label("loc_91E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96D")

    ChrTalk(    #14
        0x106,
        (
            "#057FOur boy and the Aureole must\x01",
            "be just ahead of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA4")

    label("loc_96D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B4")

    ChrTalk(    #15
        0x105,
        "#1162FSo...Joshua and the Aureole must be ahead.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA4")

    label("loc_9B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FA")

    ChrTalk(    #16
        0x103,
        "#022FJoshua and the Aureole must be just ahead.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA4")

    label("loc_9FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A50")

    ChrTalk(    #17
        0x109,
        (
            "#1063FNo doubt about it. The Aureole and\x01",
            "Joshua are just ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA4")

    label("loc_A50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA4")

    ChrTalk(    #18
        0x104,
        (
            "#032FYes. The Aureole and our wayward bracer\x01",
            "must be just ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA4")


    ChrTalk(    #19
        0x101,
        (
            "#1002F#6PThey have to be, I think.\x02\x03",

            "#1003FGuys...\x01",
            "This'll probably be our last fight.\x02\x03",

            "#1010FThis is where we're gonna stop Ouroboros\x01",
            "and the shutdown phenomenon...\x02\x03",

            "...and it's gonna be where we free Joshua\x01",
            "from Weissmann once and for all.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)

    ChrTalk(    #20
        0x101,
        "#1005F#4PGuys, please, give me everything you still have!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C19")

    ChrTalk(    #21
        0x108,
        "#070Fof course!\x02",
    )

    CloseMessageWindow()

    label("loc_C19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4F")

    ChrTalk(    #22
        0x106,
        "#051FLike you'd get anything less!\x02",
    )

    CloseMessageWindow()

    label("loc_C4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9B")

    ChrTalk(    #23
        0x105,
        (
            "#1168FI'm not sure how much it will be...\x01",
            "but of course!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC5")

    ChrTalk(    #24
        0x103,
        "#027FHeehee... Always!\x02",
    )

    CloseMessageWindow()

    label("loc_CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF9")

    ChrTalk(    #25
        0x109,
        "#1061FHeheh! You leave it to me!\x02",
    )

    CloseMessageWindow()

    label("loc_CF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D28")

    ChrTalk(    #26
        0x107,
        "#061FYeah! I'll do my best!\x02",
    )

    CloseMessageWindow()

    label("loc_D28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D54")

    ChrTalk(    #27
        0x110,
        "#277FAlways, Ms. Bright.\x02",
    )

    CloseMessageWindow()

    label("loc_D54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9B")

    ChrTalk(    #28
        0x10B,
        (
            "#210FHeh. Well, guess Joshua deserves it,\x01",
            "at least!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCC")

    ChrTalk(    #29
        0x10F,
        "#171FI shall give you my all!\x02",
    )

    CloseMessageWindow()

    label("loc_DCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E21")

    ChrTalk(    #30
        0x104,
        (
            "#031FAlways, my rose.\x01",
            "Come! The curtain rises on the final scene!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E21")

    OP_A2(0x223D)
    OP_28(0x9F, 0x1, 0x2000)
    OP_28(0xA0, 0x4, 0x2)
    OP_28(0xA0, 0x4, 0x8)
    OP_28(0xA0, 0x1, 0x1)
    Sleep(100)
    Fade(1000)

    def lambda_E4A():
        OP_6B(4000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4A)

    def lambda_E5A():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E5A)

    def lambda_E68():
        OP_6E(262, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E68)
    OP_30(0x0)
    WaitChrThread(0x101, 0x1)
    SetMapFlags(0x1)
    EventEnd(0x2)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_279 end

    def Function_3_E86(): pass

    label("Function_3_E86")

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
        (0, "loc_EFF"),
        (1, "loc_F05"),
        (SWITCH_DEFAULT, "loc_F0B"),
    )


    label("loc_EFF")

    OP_A2(0x1200)
    Jump("loc_F0B")

    label("loc_F05")

    OP_A2(0x1201)
    Jump("loc_F0B")

    label("loc_F0B")

    Return()

    # Function_3_E86 end

    def Function_4_F0C(): pass

    label("Function_4_F0C")

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

    # Function_4_F0C end

    def Function_5_FA3(): pass

    label("Function_5_FA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1009")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_11AB")

    label("loc_1009")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #32
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1190")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_73(0x1)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x2BC)
    OP_71(0x1, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 29120, 1000, 5080, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 29120, 1000, 5080, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1190")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11AA")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_11AA")

    Return()

    label("loc_11AB")

    Return()

    # Function_5_FA3 end

    SaveToFile()

Try(main)
