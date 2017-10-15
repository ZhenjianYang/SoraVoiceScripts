from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C6002   ._SN',
        MapName             = 'Other',
        Location            = 'C6002.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
        Flags               = 0,
        EntryFunctionIndex  = 16,
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
        'Target',                               # 9
        'Original Gospel',                      # 10
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
        'ED6_DT26/CH20353 ._CH',             # 00
        'ED6_DT26/CH20425 ._CH',             # 01
        'ED6_DT27/CH03000 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT26/CH20353P._CP',             # 00
        'ED6_DT26/CH20425P._CP',             # 01
        'ED6_DT27/CH03000P._CP',             # 02
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
        Unknown3            = 65537,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 2000,
        Y                   = 4500,
        Z                   = 19500,
        Range               = 4000,
        Unknown_10          = 0x1964,
        Unknown_14          = 0x4E20,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -12900,
        Y                   = 0,
        Z                   = 2140,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 18,
    )


    DeclActor(
        TriggerX            = 2000,
        TriggerZ            = 2000,
        TriggerY            = 1560,
        TriggerRange        = 1000,
        ActorX              = 2000,
        ActorZ              = 2000,
        ActorY              = 1560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5200,
        TriggerZ            = 0,
        TriggerY            = 12110,
        TriggerRange        = 1000,
        ActorX              = 5200,
        ActorZ              = 1200,
        ActorY              = 13110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_1BB",          # 01, 1
        "Function_2_220",          # 02, 2
        "Function_3_16F9",         # 03, 3
        "Function_4_1730",         # 04, 4
        "Function_5_1767",         # 05, 5
        "Function_6_179E",         # 06, 6
        "Function_7_17D5",         # 07, 7
        "Function_8_201D",         # 08, 8
        "Function_9_2115",         # 09, 9
        "Function_10_2169",        # 0A, 10
        "Function_11_2ECF",        # 0B, 11
        "Function_12_2F26",        # 0C, 12
        "Function_13_2F78",        # 0D, 13
        "Function_14_2FCA",        # 0E, 14
        "Function_15_301C",        # 0F, 15
        "Function_16_3C01",        # 10, 16
        "Function_17_455F",        # 11, 17
        "Function_18_471D",        # 12, 18
        "Function_19_4828",        # 13, 19
        "Function_20_49E6",        # 14, 20
        "Function_21_4A6C",        # 15, 21
        "Function_22_4AFF",        # 16, 22
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_19B")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_1BA")

    label("loc_19B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1AC")
    OP_A3(0x10F1)
    Event(0, 17)
    Jump("loc_1BA")

    label("loc_1AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1BA")
    OP_A3(0x10F2)
    Event(0, 19)

    label("loc_1BA")

    Return()

    # Function_0_18A end

    def Function_1_1BB(): pass

    label("Function_1_1BB")

    OP_22(0x1C3, 0x1, 0x64)
    StopSound(0x124F8, 0x493E0, 0x0)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 500)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_END)), "loc_20E")
    OP_72(0x1, 0x4)
    OP_6F(0x1, 950)
    OP_6F(0x3, 240)

    label("loc_20E")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    Return()

    # Function_1_1BB end

    def Function_2_220(): pass

    label("Function_2_220")

    EventBegin(0x0)
    OP_72(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F91")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_29C():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29C)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1004F#6PHey, what...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1044F#6PThere's something coming.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_39A():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39A)

    def lambda_3B2():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B2)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_3DD():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3DD)
    Sleep(2000)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x6)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(500)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #2
        0x101,
        "#1004F#5PWhat in the world?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DB")

    ChrTalk(    #3
        0x102,
        (
            "#1040F#5PLooks like this is a Halo Rail car.\x02\x03",

            "I wonder how that rail works.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_4DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54A")

    ChrTalk(    #4
        0x10F,
        (
            "#173FThis must be a car for the Halo Rail.\x02\x03",

            "#178FI can't help but wonder how it works...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_54A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C6")

    ChrTalk(    #5
        0x105,
        (
            "#1165F#5PThis must be a car for the Halo Rail.\x02\x03",

            "You, um, have to wonder how it\x01",
            "works without, well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_5C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_627")

    ChrTalk(    #6
        0x103,
        (
            "#026F#5PThis must be a car for the Halo Rail.\x02\x03",

            "I do wonder how it works...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_627")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69F")

    ChrTalk(    #7
        0x106,
        (
            "#053F#5PIf I had to guess, this is a Halo Rail car.\x02\x03",

            "Not sure how the 'rail' bit works, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_69F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70B")

    ChrTalk(    #8
        0x108,
        (
            "#074F#5PHmmm... This must be a car for the Halo Rail.\x02\x03",

            "I wonder how the 'rail' works.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_70B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_774")

    ChrTalk(    #9
        0x109,
        (
            "#1064F#5PHuh. The Halo Rail, I presume!\x02\x03",

            "I'm kinda lost on how it works, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_774")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D9")

    ChrTalk(    #10
        0x104,
        (
            "#035F#5PAh, this must be a car for the Halo Rail.\x02\x03",

            "Those rails... Fascinating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_7D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_832")

    ChrTalk(    #11
        0x10B,
        (
            "#216F#5PWait, THIS is the Halo Rail?\x02\x03",

            "But, but, the rails! The RAILS!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_832")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_907")

    ChrTalk(    #12
        0x110,
        (
            "#278FIt seems fundamentally similar to inter-city light\x01",
            "rail systems you find in major Imperial cities.\x02\x03",

            "#277FGranted, in the Empire we rather tend\x01",
            "to not make the rails out of actual light.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_907")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AA")

    ChrTalk(    #13
        0x10B,
        (
            "#213F#5PI see. It really is just like trains back home!\x02\x03",

            "#413FNot sure how okay I am with the idea\x01",
            "of riding on rails made of AIR, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_9AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A82")

    ChrTalk(    #14
        0x104,
        (
            "#030F#5PIt's very similar to the light rail systems\x01",
            "used throughout Erebonia, as I thought.\x02\x03",

            "#031FAh, to make the rails out of actual light!\x01",
            "The ancients knew the value of spectacle.\x01",
            "And humor!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_A82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B47")

    ChrTalk(    #15
        0x109,
        (
            "#1064F#5PI see, it's like the train systems you find\x01",
            "in places like Erebonia.\x02\x03",

            "#1068FDon't think I've ever seen 'light rail'\x01",
            "taken to this extreme before, though.\x01",
            "No siree...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_B47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDF")

    ChrTalk(    #16
        0x108,
        (
            "#073F#5PAh, I see. It runs on rails a bit\x01",
            "like a mine cart.\x02\x03",

            "#075FI'm not sure how to feel about the\x01",
            "transparent rails, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_BDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8C")

    ChrTalk(    #17
        0x106,
        (
            "#555F#5PLooks a lot like the train systems\x01",
            "the Imperials use.\x02\x03",

            "#551F'Course, the Imperials aren't crazy enough\x01",
            "to try and make rails out of nothin'...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2A")

    ChrTalk(    #18
        0x103,
        (
            "#020F#5PAh, so it's like the Erebonian train\x01",
            "system. I see.\x02\x03",

            "#524FI...have to wonder just how safe a\x01",
            "rail made out of light is, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBF")

    ChrTalk(    #19
        0x105,
        (
            "#1164F#5PIt seems to be an advanced version of\x01",
            "the trains which run throughout Erebonia.\x02\x03",

            "I wonder what the rails are made of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E29")

    ChrTalk(    #20
        0x10F,
        (
            "#176FIt seems similar to Imperial trains.\x02\x03",

            "#178FI'm unsure about the rails, however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ECF")

    ChrTalk(    #21
        0x107,
        (
            "#064F#5PWooooooooooooooow...\x01",
            "It uses a projected force field in\x01",
            "place of a solid rail!\x02\x03",

            "#067FThat... That's the most amazing\x01",
            "thing I've ever seen!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECF")


    ChrTalk(    #22
        0x101,
        (
            "#1006F#5PIt all feels a little over my head, but if\x01",
            "it'll get us where we need to go without\x01",
            "dropping us into the clouds, I'm all for it!\x02\x03",

            "#1018FC'mon, let's hop on and try it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2205)
    OP_28(0x9D, 0x1, 0x20)
    Jump("loc_1653")

    label("loc_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1209")
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_1001():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1001)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()

    ChrTalk(    #23
        0x101,
        "#1006F#6PHere it comes!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_10D3():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10D3)

    def lambda_10EB():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10EB)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1116():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1116)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x6)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #24
        0x101,
        (
            "#1006F#5PSo we should finally be able\x01",
            "to use these things, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1040F#5PI think so.\x01",
            "Let's get on and try.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220A)
    Jump("loc_1653")

    label("loc_1209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141B")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_127E():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_127E)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_12EB():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12EB)

    def lambda_1303():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1303)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_132E():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_132E)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x6)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #26
        0x101,
        (
            "#1015F#5PLet's see, we can use three\x01",
            "stations now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#1040F#5PYes. This makes things much easier.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x220B)
    Jump("loc_1653")

    label("loc_141B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1653")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_1490():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1490)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_14FD():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14FD)

    def lambda_1515():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1515)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_1540():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1540)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x6)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #28
        0x102,
        (
            "#1035F#5PAll right...\x02\x03",

            "#1040FNow we can easily go everywhere,\x01",
            "from Calmare to the Axis Pillar!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1007F#5P*pheeeew* That was a bit of work.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x220C)
    OP_28(0x9F, 0x1, 0x2)

    label("loc_1653")

    OP_A2(0x2208)
    OP_28(0x9E, 0x1, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3060, 5000, 18520, 0)
    SetChrPos(0x1, 3060, 5000, 18520, 0)
    SetChrPos(0x2, 3060, 5000, 18520, 0)
    SetChrPos(0x3, 3060, 5000, 18520, 0)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_2_220 end

    def Function_3_16F9(): pass

    label("Function_3_16F9")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xA3C, 0x1388, 0x47B8, 0x1388, 0x0)

    def lambda_1724():

        label("loc_1724")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1724")

    QueueWorkItem2(0xFE, 2, lambda_1724)
    Return()

    # Function_3_16F9 end

    def Function_4_1730(): pass

    label("Function_4_1730")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xE2E, 0x1388, 0x47CC, 0x1388, 0x0)

    def lambda_175B():

        label("loc_175B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_175B")

    QueueWorkItem2(0xFE, 2, lambda_175B)
    Return()

    # Function_4_1730 end

    def Function_5_1767(): pass

    label("Function_5_1767")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0x8C0, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_1792():

        label("loc_1792")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1792")

    QueueWorkItem2(0xFE, 2, lambda_1792)
    Return()

    # Function_5_1767 end

    def Function_6_179E(): pass

    label("Function_6_179E")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xFE6, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_17C9():

        label("loc_17C9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_17C9")

    QueueWorkItem2(0xFE, 2, lambda_17C9)
    Return()

    # Function_6_179E end

    def Function_7_17D5(): pass

    label("Function_7_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DE")
    Return()

    label("loc_17DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5B")
    EventBegin(0x0)
    Fade(500)
    OP_6D(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2620, 5000, 18360, 0)
    SetChrPos(0x102, 3630, 5000, 18380, 0)
    SetChrPos(0xF8, 2240, 5000, 17190, 0)
    SetChrPos(0xF9, 4070, 5000, 17190, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #30
        (
            "\x07\x05Currently, no other stations are operating in\x01",
            "Emergency Operations Mode.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Machine Voice")

    AnonymousTalk(    #31
        (
            "\x07\x05We are sorry, but the Halo Rail service is not currently\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1997")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_19CB")

    label("loc_1997")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B9")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_19CB")

    label("loc_19B9")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_19CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19ED")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1A21")

    label("loc_19ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A0F")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1A21")

    label("loc_1A0F")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_1A21")

    Sleep(1000)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0xF8)
    OP_63(0xF9)
    Sleep(500)

    ChrTalk(    #32
        0x101,
        (
            "#1019F#5P...Real informative.\x01",
            "Thanks, Creepy Disembodied Voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#1035F#5PIt sounds like the other stations need to be in\x01",
            "this 'Emergency Operations Mode' if we intend to\x01",
            "get around.\x02\x03",

            "#1040FFor now, I'm afraid the 'Halo Rail'\x01",
            "isn't of much use to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007F#5PNuts. And here I was, getting hopeful for once.\x02\x03",

            "#1015FWell, let's see if we can\x01",
            "find another way around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220E)
    OP_28(0x9D, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3060, 5000, 18520, 0)
    SetChrPos(0x1, 3060, 5000, 18520, 0)
    SetChrPos(0x2, 3060, 5000, 18520, 0)
    SetChrPos(0x3, 3060, 5000, 18520, 0)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_1D43")

    label("loc_1C5B")

    EventBegin(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #35
        (
            "\x07\x05Currently, no other stations are operating in\x01",
            "Emergency Operations Mode.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Machine Voice")

    AnonymousTalk(    #36
        (
            "\x07\x05We are sorry, but the Halo Rail service is not currently\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1D43")

    Jump("loc_201C")

    label("loc_1D46")

    EventBegin(0x0)
    Fade(500)
    OP_6D(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2620, 5000, 18360, 0)
    SetChrPos(0x102, 3630, 5000, 18380, 0)
    SetChrPos(0xF8, 2240, 5000, 17190, 0)
    SetChrPos(0xF9, 4070, 5000, 17190, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_END)), "loc_1E27")
    OP_CC(0x1, 0x0, "West Calmare Station")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_END)), "loc_1E4E")
    OP_CC(0x1, 0x0, "Cradle Station #35")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_END)), "loc_1E76")
    OP_CC(0x1, 0x0, "Axis Pillar Station")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1E76")

    OP_CC(0x1, 0x0, "Quit")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1EB1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F33")

    label("loc_1EB1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F33")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED5")
    Jump("loc_1F33")

    label("loc_1ED5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F26")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1F0F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F0C")

    Jump("loc_1F26")

    label("loc_1F0F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1ED5")

    label("loc_1F26")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EBB")

    label("loc_1F33")

    SetMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1F51"),
        (1, "loc_1F8F"),
        (2, "loc_1FCD"),
        (3, "loc_200B"),
        (SWITCH_DEFAULT, "loc_200E"),
    )


    label("loc_1F51")

    OP_A2(0x2212)
    OP_A2(0x2214)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1F64():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F64)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_200E")

    label("loc_1F8F")

    OP_A2(0x2212)
    OP_A2(0x2215)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1FA2():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FA2)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_200E")

    label("loc_1FCD")

    OP_A2(0x2212)
    OP_A2(0x2217)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1FE0():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FE0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_200E")

    label("loc_200B")

    Jump("loc_200E")

    label("loc_200E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    EventEnd(0x0)

    label("loc_201C")

    Return()

    # Function_7_17D5 end

    def Function_8_201D(): pass

    label("Function_8_201D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_43(0x101, 0x2, 0x0, 0x9)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x9)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    Sleep(1500)
    OP_6F(0x1, 950)
    OP_70(0x1, 0x44C)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 5)), scpexpr(EXPR_END)), "loc_20C9")
    OP_6F(0x1, 1100)
    OP_70(0x1, 0x514)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_2094():
        OP_6D(8300, 5000, 21350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2094)

    def lambda_20AC():
        OP_6C(12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20AC)

    def lambda_20BC():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_20BC)
    Jump("loc_2104")

    label("loc_20C9")

    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_20E2():
        OP_6D(-2860, 5000, 21710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20E2)

    def lambda_20FA():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20FA)

    label("loc_2104")

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_8_201D end

    def Function_9_2115(): pass

    label("Function_9_2115")

    OP_8E(0xFE, 0xC08, 0x1388, 0x4A56, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x13F6, 0x4F6A, 0x7D0, 0x0)

    def lambda_2143():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2143)
    OP_8E(0xFE, 0xC1C, 0x13F6, 0x5E9C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_2115 end

    def Function_10_2169(): pass

    label("Function_10_2169")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(3100, 5110, 23900, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 3050, 5110, 21510, 180)
    SetChrPos(0x102, 3050, 5110, 21510, 180)
    SetChrPos(0xF8, 3050, 5110, 21510, 180)
    SetChrPos(0xF9, 3050, 5110, 21510, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 3)), scpexpr(EXPR_END)), "loc_2272")
    OP_6D(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_225D():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_225D)
    Jump("loc_22EA")

    label("loc_2272")

    OP_6D(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_22C8():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22C8)

    def lambda_22E0():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22E0)

    label("loc_22EA")

    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    FadeToBright(1000, 0)
    OP_73(0x1)
    OP_23(0x13E)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC5")
    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_2346():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2346)

    def lambda_235E():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_235E)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xE)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #37
        0x101,
        "#1004F#2PWhoaaaaaa, that didn't take very long!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#1035F#5PFor as fast as it went, there was barely\x01",
            "any vibration or unsteadiness, either.\x02\x03",

            "#1040FTo be honest, this technology is a bit\x01",
            "mind-blowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1015F#2PNo kidding. Still...\x02\x03",

            "#1016FAs nice as it is to go fast, the view was\x01",
            "amazing, too. I kinda wish it went a\x01",
            "bit slower so you could enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2585")

    ChrTalk(    #40
        0x10B,
        (
            "#413FIt'd be a tourist attraction in that case,\x01",
            "not a train system. Duh.\x02\x03",

            "#210FIt IS kinda a waste of a good view,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_2585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25B6")

    ChrTalk(    #41
        0x107,
        "#067FHeehee! It is, sorta.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_25B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25EE")

    ChrTalk(    #42
        0x105,
        "#1168FHaha. It is, unfortunately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_25EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2627")

    ChrTalk(    #43 op#A
        0x103,
        "#021Ahh, the perils of technology.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_2627")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_265E")

    ChrTalk(    #44
        0x109,
        "#1061FHaha! Yeah, unfortunately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_265E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2695")

    ChrTalk(    #45
        0x104,
        "#031FHaha! Lamentable, but true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_2695")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C8")

    ChrTalk(    #46
        0x10F,
        "#171FHah... I suppose it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_26C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26FD")

    ChrTalk(    #47
        0x108,
        "#071FHaha! Unfortunately, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_26FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2725")

    ChrTalk(    #48
        0x106,
        "#051FHeh, I suppose.\x02",
    )

    CloseMessageWindow()

    label("loc_2725")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E6")

    ChrTalk(    #49
        0x110,
        (
            "#278FFar more important is how much easier\x01",
            "this will make our investigations.\x02\x03",

            "#277FI would recommend making the discovery of\x01",
            "these stations a top priority in a new area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_27E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_288B")

    ChrTalk(    #50
        0x106,
        (
            "#051FMore importantly, this'll make gettin'\x01",
            "around a hell of a lot easier.\x02\x03",

            "We should try 'n find these stations\x01",
            "as soon as we hit a new area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_288B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_291B")

    ChrTalk(    #51
        0x108,
        (
            "#070FThis makes getting around the\x01",
            "city quite a bit easier.\x02\x03",

            "We should try and find the other\x01",
            "stations as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_291B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29DF")

    ChrTalk(    #52
        0x10F,
        (
            "#179FI'm more impressed with what this does\x01",
            "to the speed at which we can investigate.\x02\x03",

            "#170FI think it would be wise to make finding\x01",
            "these stations a priority going forward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_29DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA6")

    ChrTalk(    #53
        0x104,
        (
            "#035FHeh, and of course, this also solves\x01",
            "the travel problems we have had.\x02\x03",

            "#030FIt would behoove us to locate the local\x01",
            "rail station as soon as we enter a new\x01",
            "area, I believe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B5C")

    ChrTalk(    #54
        0x109,
        (
            "#1060FI kinda think the important bit is what\x01",
            "this does to the speed at which we can\x01",
            "get around.\x02\x03",

            "We oughtta try and find the other\x01",
            "stations as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2B5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C39")

    ChrTalk(    #55
        0x103,
        (
            "#027FI'm more impressed with how\x01",
            "this improves our ability to get around.\x02\x03",

            "It's just a suggestion from the itinerant\x01",
            "circus girl, but we may just want to focus\x01",
            "on finding the rest of these stations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2C39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D14")

    ChrTalk(    #56
        0x105,
        (
            "#1167FAnd in addition to the view, this also\x01",
            "allows us to travel across the Ark\x01",
            "incredibly quickly.\x02\x03",

            "#1168FI think it would be a good idea to find\x01",
            "the other stations as soon as we enter\x01",
            "new areas.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2D14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DBF")

    ChrTalk(    #57
        0x107,
        (
            "#061FHeehee, yeah, and it lets us get around\x01",
            "really fast too! ♪\x02\x03",

            "#560FI think we should try and find the other\x01",
            "stations as soon as we find a new area!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBF")

    OP_A2(0x220F)
    Jump("loc_2E1D")

    label("loc_2DC5")

    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_2DE3():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2DE3)

    def lambda_2DFB():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2DFB)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xE)
    Sleep(500)

    label("loc_2E1D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    SetChrPos(0x0, 3060, 5000, 18520, 180)
    SetChrPos(0x1, 3060, 5000, 18520, 180)
    SetChrPos(0x2, 3060, 5000, 18520, 180)
    SetChrPos(0x3, 3060, 5000, 18520, 180)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    ClearMapFlags(0x100000)
    Return()

    # Function_10_2169 end

    def Function_11_2ECF(): pass

    label("Function_11_2ECF")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2EE5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EE5)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xECE, 0x1388, 0x4376, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_11_2ECF end

    def Function_12_2F26(): pass

    label("Function_12_2F26")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F3C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F3C)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9F6, 0x1388, 0x4362, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_2F26 end

    def Function_13_2F78(): pass

    label("Function_13_2F78")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F8E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F8E)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1086, 0x1388, 0x4808, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_13_2F78 end

    def Function_14_2FCA(): pass

    label("Function_14_2FCA")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2FE0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FE0)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7B2, 0x1388, 0x47A4, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_14_2FCA end

    def Function_15_301C(): pass

    label("Function_15_301C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3041")
    Call(0, 20)
    Call(0, 21)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_3041")

    Fade(500)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2480, 2000, 500, 0)
    SetChrPos(0x102, 1480, 2000, 500, 0)
    SetChrPos(0xF8, 2450, 1600, -1400, 0)
    SetChrPos(0xF9, 1560, 1600, -1220, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 78, 34, 12)

    AnonymousTalk(    #58
        (
            "\x07\x05#1SHalo Rail, Factoria Station #7\x01",
            "The Halo Rail system is currently operating at limited\x01",
            "capacity. We apologize for the inconvenience.\x01",
            "Please select a service from this terminal.\x01\x01",
            "- Liber Ark Transit Authority\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B53")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        20,
        100,
        1,
        (
            "Factoria District Information\x01",      # 0
            "Halo Rail Service Information\x01",      # 1
            "Online Shop\x01",                        # 2
            "Gate Lock Release\x01",                  # 3
            "Cease Service\x01",                      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3263"),
        (1, "loc_33B7"),
        (2, "loc_350B"),
        (3, "loc_3528"),
        (4, "loc_3B36"),
        (SWITCH_DEFAULT, "loc_3B43"),
    )


    label("loc_3263")

    OP_56(0x0)

    AnonymousTalk(    #59
        (
            "\x07\x05#1SFactoria is Liber Ark's beating industrial heart, located on\x01",
            "the eastern side of the Ark. All daily necessities, from\x01",
            "food to clothes to medicines to even homes, are produced in\x01",
            "Factoria's round-the-clock workshops.\x01\x01",
            "The district is made up of 64 blocks, with blocks one\x01",
            "through eight designed as the Ark's primary trade port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B50")

    label("loc_33B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3498")
    OP_56(0x0)

    AnonymousTalk(    #60
        (
            "\x07\x05#1SHalo Rail service is currently limited.\x01",
            "Would you like to activate Emergency Operation Mode\x01",
            "for Cradle Station No. 35?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        130,
        240,
        0,
        (
            "Activate\x01",             # 0
            "Do Not Activate\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3476"),
        (1, "loc_348F"),
        (SWITCH_DEFAULT, "loc_3495"),
    )


    label("loc_3476")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Call(0, 2)
    Return()

    label("loc_348F")

    OP_5F(0x1)
    Jump("loc_3495")

    label("loc_3495")

    Jump("loc_3508")

    label("loc_3498")

    OP_56(0x0)

    AnonymousTalk(    #61
        (
            "\x07\x05#1SHalo Rail service is currently limited.\x01",
            "Factoria Station #7 is currently in Emergency Operation\x01",
            "Mode.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3508")

    Jump("loc_3B50")

    label("loc_350B")

    FadeToBright(300, 0)

    AnonymousTalk(    #62
        "\x07\x05\x02",
    )

    OP_A9(0xF2)
    FadeToDark(300, 0, 100)
    Jump("loc_3B50")

    label("loc_3528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEA")
    OP_56(0x0)

    AnonymousTalk(    #63
        (
            "\x07\x05#1SIn the event of service disruption of the Halo Rail, a gate\x01",
            "may be unlocked at each station, leading to substratum\x01",
            "access passages.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #64
        (
            "\x07\x05#1S[!!WARNING!!] By order of the Axis Pillar, the Factoria\x01",
            "district is currently on security lockdown. Please present\x01",
            "your Gospel ID and enter the password to access this\x01",
            "function.\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_56(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_380D")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as first time examined\x01",                                                           # 0
            "Set as second+ time examined (Haven't talked to Kyle & haven't rescued pirates)\x01",      # 1
            "Set as second+ time examined (Haven't talked to Kyle & have rescued pirates)\x01",         # 2
            "Set as second+ time examined (Have talked to Kyle)\x01",                                   # 3
            "No Change\x01",                                                                            # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_37DD"),
        (1, "loc_37E9"),
        (2, "loc_37F5"),
        (3, "loc_3801"),
        (SWITCH_DEFAULT, "loc_380D"),
    )


    label("loc_37DD")

    OP_A3(0x221F)
    OP_A3(0x222D)
    OP_A3(0x222C)
    Jump("loc_380D")

    label("loc_37E9")

    OP_A2(0x221F)
    OP_A3(0x222D)
    OP_A3(0x222C)
    Jump("loc_380D")

    label("loc_37F5")

    OP_A2(0x221F)
    OP_A3(0x222D)
    OP_A2(0x222C)
    Jump("loc_380D")

    label("loc_3801")

    OP_A2(0x221F)
    OP_A2(0x222D)
    OP_A2(0x222C)
    Jump("loc_380D")

    label("loc_380D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D0")

    ChrTalk(    #65
        0x101,
        "#1004F#6PA password?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        (
            "#1035F#6PI get the feeling this 'lockdown' is recent.\x02\x03",

            "#1042FLooks like the society has mastered\x01",
            "quite a few of the city controls already.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #67
        "\x07\x05\x02",
    )

    Jump("loc_3AD4")

    label("loc_38D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3972")

    ChrTalk(    #68
        0x102,
        (
            "#1035F#6PWe have no real choice but\x01",
            "to leave this alone for now.\x02\x03",

            "#1040FOnce we have some idea what\x01",
            "the password is, we can return.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #69
        "\x07\x05\x02",
    )

    Jump("loc_3AD4")

    label("loc_3972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A3B")

    ChrTalk(    #70
        0x102,
        (
            "#1035F#6PIf the society set the password recently,\x01",
            "then our guesses are...limited, given\x01",
            "what we know at the moment.\x02\x03",

            "#1040FI can think of someone who might know,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #71
        "\x07\x05\x02",
    )

    Jump("loc_3AD4")

    label("loc_3A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_END)), "loc_3AD4")

    ChrTalk(    #72
        0x102,
        (
            "#1040F#6PI think we can figure this out given\x01",
            "what we learned from Kyle.\x02\x03",

            "Use the Gospel, and let's try speaking\x01",
            "the password.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #73
        "\x07\x05\x02",
    )


    label("loc_3AD4")

    OP_A2(0x221F)
    OP_28(0x9E, 0x1, 0x2)
    FadeToDark(300, 0, 100)
    Jump("loc_3B33")

    label("loc_3AEA")

    OP_56(0x0)

    AnonymousTalk(    #74
        (
            "\x07\x05#1SThe Factoria Station #7 Substratum Gate is currently\x01",
            "unlocked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B33")

    Jump("loc_3B50")

    label("loc_3B36")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B50")

    label("loc_3B43")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B50")

    label("loc_3B50")

    Jump("loc_31BC")

    label("loc_3B53")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(100, 0)
    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    EventEnd(0x0)
    Return()

    # Function_15_301C end

    def Function_16_3C01(): pass

    label("Function_16_3C01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x40F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C0E")
    Return()

    label("loc_3C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15E0), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4071")
    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_48()
    EventBegin(0x0)
    Fade(1000)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2480, 2000, 500, 0)
    SetChrPos(0x102, 1480, 2000, 500, 0)
    SetChrPos(0xF8, 2450, 1600, -1400, 0)
    SetChrPos(0xF9, 1560, 1600, -1220, 0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #75
        (
            "\x07\x05[!!WARNING!!] By order of the Axis Pillar, the Factoria\x01",
            "district is currently on security lockdown.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #76
        "\x07\x05Please enter the security password to access this function.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E95")

    ChrTalk(    #77
        0x101,
        "#1004F#6PA password?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1035F#6PI get the feeling this 'lockdown' is recent.\x02\x03",

            "#1042FLooks like the society has mastered\x01",
            "quite a few of the city controls already.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x221F)
    Jump("loc_3FE1")

    label("loc_3E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F29")

    ChrTalk(    #79
        0x102,
        (
            "#1035F#6PWe have no real choice but\x01",
            "to leave this alone for now.\x02\x03",

            "#1040FOnce we have some idea what\x01",
            "the password is, we can return.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE1")

    label("loc_3F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE1")

    ChrTalk(    #80
        0x102,
        (
            "#1035F#6PIf the society set the password recently,\x01",
            "then our guesses are...limited, given\x01",
            "what we know at the moment.\x02\x03",

            "#1040FI can think of someone who might know,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE1")

    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    EventEnd(0x0)
    Jump("loc_455E")

    label("loc_4071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15E0), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_450D")
    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_48()
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40F4")
    Call(0, 20)
    Call(0, 21)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_40F4")

    Fade(1000)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2730, 2000, 270, 315)
    SetChrPos(0x102, 1150, 2000, 310, 45)
    SetChrPos(0xF8, 2430, 1600, -1200, 0)
    SetChrPos(0xF9, 1550, 1600, -1200, 0)
    OP_0D()
    Sleep(1000)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 9)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 1)
    SetChrPos(0x9, 2400, 2650, 500, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp007_00.eff")
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x9, 0, 150, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_82(0x0, 0x2)
    OP_23(0x90)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #81
        "\x07\x05ID confirmed. Welcome, Ms. Auslese!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #82
        "\x07\x05Please enter the security password to access this function.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x9, 0x80)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #83
        "\x18\x07\x05What is the password?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "ORPHEN\x01",       # 0
            "ORPHEUS\x01",      # 1
            "OLORIN\x01",       # 2
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
        (0, "loc_4379"),
        (2, "loc_4379"),
        (1, "loc_44BD"),
        (SWITCH_DEFAULT, "loc_450A"),
    )


    label("loc_4379")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #84
        "\x07\x05Password incorrect.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Machine Voice")

    AnonymousTalk(    #85
        (
            "\x07\x05Please present your Gospel again and enter the correct\x01",
            "password.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    EventEnd(0x0)
    EventEnd(0x0)
    Jump("loc_450A")

    label("loc_44BD")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #86
        "\x07\x05Password confirmed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5701   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_450A")

    label("loc_450A")

    Jump("loc_455E")

    label("loc_450D")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_48()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #87
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    ClearMapFlags(0x80)
    Return()

    label("loc_455E")

    Return()

    # Function_16_3C01 end

    def Function_17_455F(): pass

    label("Function_17_455F")

    EventBegin(0x0)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2480, 2000, 500, 0)
    SetChrPos(0x102, 1480, 2000, 500, 0)
    SetChrPos(0xF8, 2450, 1600, -1400, 0)
    SetChrPos(0xF9, 1560, 1600, -1220, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #88
        "\x07\x05Locks on gate in station vicinity have been removed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #89
        "\x07\x05Tunnel #246 is now usable.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    OP_0D()
    OP_A2(0x222E)
    OP_28(0x9E, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_17_455F end

    def Function_18_471D(): pass

    label("Function_18_471D")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-13000, 0, 2000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_89(0x101, -12000, 0, 2000, 90)
    OP_89(0x102, -13000, 0, 3000, 90)
    OP_89(0xF8, -13000, 0, 1000, 90)
    OP_89(0xF9, -14000, 0, 2000, 90)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x4B0)

    def lambda_47C9():
        OP_6D(-13000, -25000, 490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47C9)

    def lambda_47E1():
        OP_67(0, 3890, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47E1)

    def lambda_47F9():
        OP_6B(5200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_47F9)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    Sleep(500)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5701   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_471D end

    def Function_19_4828(): pass

    label("Function_19_4828")

    EventBegin(0x0)
    OP_6D(-13000, -12750, 490, 0)
    OP_67(0, 3890, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_6F(0x0, 300)
    OP_48()
    OP_89(0x101, -12000, -23000, 2000, 90)
    OP_89(0x102, -13000, -23000, 3000, 90)
    OP_89(0xF8, -13000, -23000, 1000, 90)
    OP_89(0xF9, -14000, -23000, 2000, 90)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_70(0x0, 0x0)

    def lambda_48CE():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48CE)

    def lambda_48E6():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48E6)
    Sleep(4000)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    OP_73(0x0)
    Sleep(200)
    Fade(500)
    OP_6D(-7000, 0, 2000, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, -7000, 0, 2000, 90)
    SetChrPos(0x1, -7000, 0, 2000, 90)
    SetChrPos(0x2, -7000, 0, 2000, 90)
    SetChrPos(0x3, -7000, 0, 2000, 90)
    OP_0D()
    OP_A2(0x222F)
    EventEnd(0x0)
    Return()

    # Function_19_4828 end

    def Function_20_49E6(): pass

    label("Function_20_49E6")

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
        (0, "loc_4A5F"),
        (1, "loc_4A65"),
        (SWITCH_DEFAULT, "loc_4A6B"),
    )


    label("loc_4A5F")

    OP_A2(0x1200)
    Jump("loc_4A6B")

    label("loc_4A65")

    OP_A2(0x1201)
    Jump("loc_4A6B")

    label("loc_4A6B")

    Return()

    # Function_20_49E6 end

    def Function_21_4A6C(): pass

    label("Function_21_4A6C")

    FadeToDark(0, 0, -1)
    OP_6D(-545830, 30000, 755590, 0)
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

    # Function_21_4A6C end

    def Function_22_4AFF(): pass

    label("Function_22_4AFF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #90
        "\x07\x05Platform This Way⇒ Factoria Station #7 \x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_4AFF end

    SaveToFile()

Try(main)
