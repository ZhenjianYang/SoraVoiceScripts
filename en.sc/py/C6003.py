from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C6003   ._SN',
        MapName             = 'Other',
        Location            = 'C6003.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        'Target',                               # 9
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
        NpcIndex            = 0x80,
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
        Unknown_1C          = 16,
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
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_172",          # 01, 1
        "Function_2_1D7",          # 02, 2
        "Function_3_16B0",         # 03, 3
        "Function_4_16E7",         # 04, 4
        "Function_5_171E",         # 05, 5
        "Function_6_1755",         # 06, 6
        "Function_7_178C",         # 07, 7
        "Function_8_1FD5",         # 08, 8
        "Function_9_20CD",         # 09, 9
        "Function_10_2121",        # 0A, 10
        "Function_11_2E88",        # 0B, 11
        "Function_12_2EDF",        # 0C, 12
        "Function_13_2F31",        # 0D, 13
        "Function_14_2F83",        # 0E, 14
        "Function_15_2FD5",        # 0F, 15
        "Function_16_3E2D",        # 10, 16
        "Function_17_3F38",        # 11, 17
        "Function_18_40F3",        # 12, 18
        "Function_19_4179",        # 13, 19
        "Function_20_420C",        # 14, 20
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_163")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_171")

    label("loc_163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_171")
    OP_A3(0x10F1)
    Event(0, 17)

    label("loc_171")

    Return()

    # Function_0_152 end

    def Function_1_172(): pass

    label("Function_1_172")

    OP_22(0x1C3, 0x1, 0x64)
    StopSound(0x124F8, 0x493E0, 0x0)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 500)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_END)), "loc_1C5")
    OP_72(0x1, 0x4)
    OP_6F(0x1, 950)
    OP_6F(0x3, 240)

    label("loc_1C5")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    Return()

    # Function_1_172 end

    def Function_2_1D7(): pass

    label("Function_2_1D7")

    EventBegin(0x0)
    OP_72(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F48")
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

    def lambda_253():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_253)
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

    def lambda_351():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_351)

    def lambda_369():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_369)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_394():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_394)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_492")

    ChrTalk(    #3
        0x102,
        (
            "#1040F#5PLooks like this is a Halo Rail car.\x02\x03",

            "I wonder how that rail works.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_492")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_501")

    ChrTalk(    #4
        0x10F,
        (
            "#173FThis must be a car for the Halo Rail.\x02\x03",

            "#178FI can't help but wonder how it works...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_501")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D")

    ChrTalk(    #5
        0x105,
        (
            "#1165F#5PThis must be a car for the Halo Rail.\x02\x03",

            "You, um, have to wonder how it\x01",
            "works without, well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_57D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DE")

    ChrTalk(    #6
        0x103,
        (
            "#026F#5PThis must be a car for the Halo Rail.\x02\x03",

            "I do wonder how it works...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_5DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_656")

    ChrTalk(    #7
        0x106,
        (
            "#053F#5PIf I had to guess, this is a Halo Rail car.\x02\x03",

            "Not sure how the 'rail' bit works, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_656")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C2")

    ChrTalk(    #8
        0x108,
        (
            "#074F#5PHmmm... This must be a car for the Halo Rail.\x02\x03",

            "I wonder how the 'rail' works.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_6C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72B")

    ChrTalk(    #9
        0x109,
        (
            "#1064F#5PHuh. The Halo Rail, I presume!\x02\x03",

            "I'm kinda lost on how it works, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_72B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_790")

    ChrTalk(    #10
        0x104,
        (
            "#035F#5PAh, this must be a car for the Halo Rail.\x02\x03",

            "Those rails... Fascinating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E9")

    ChrTalk(    #11
        0x10B,
        (
            "#216F#5PWait, THIS is the Halo Rail?\x02\x03",

            "But, but, the rails! The RAILS!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BE")

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
    Jump("loc_DE0")

    label("loc_8BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_961")

    ChrTalk(    #13
        0x10B,
        (
            "#213F#5PI see. It really is just like trains back home!\x02\x03",

            "#413FNot sure how okay I am with the idea\x01",
            "of riding on rails made of AIR, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE0")

    label("loc_961")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A39")

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
    Jump("loc_DE0")

    label("loc_A39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFE")

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
    Jump("loc_DE0")

    label("loc_AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B96")

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
    Jump("loc_DE0")

    label("loc_B96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C43")

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
    Jump("loc_DE0")

    label("loc_C43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE1")

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
    Jump("loc_DE0")

    label("loc_CE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D76")

    ChrTalk(    #19
        0x105,
        (
            "#1164F#5PIt seems to be an advanced version of\x01",
            "the trains which run throughout Erebonia.\x02\x03",

            "I wonder what the rails are made of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE0")

    label("loc_D76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE0")

    ChrTalk(    #20
        0x10F,
        (
            "#176FIt seems similar to Imperial trains.\x02\x03",

            "#178FI'm unsure about the rails, however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E86")

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

    label("loc_E86")


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
    Jump("loc_160A")

    label("loc_F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C0")
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

    def lambda_FB8():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FB8)
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

    def lambda_108A():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_108A)

    def lambda_10A2():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10A2)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_10CD():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10CD)
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
    Jump("loc_160A")

    label("loc_11C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D2")
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

    def lambda_1235():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1235)
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

    def lambda_12A2():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12A2)

    def lambda_12BA():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12BA)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_12E5():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12E5)
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
    Jump("loc_160A")

    label("loc_13D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160A")
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

    def lambda_1447():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1447)
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

    def lambda_14B4():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14B4)

    def lambda_14CC():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14CC)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_14F7():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14F7)
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

    label("loc_160A")

    OP_A2(0x2209)
    OP_28(0x9F, 0x1, 0x1)
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

    # Function_2_1D7 end

    def Function_3_16B0(): pass

    label("Function_3_16B0")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xA3C, 0x1388, 0x47B8, 0x1388, 0x0)

    def lambda_16DB():

        label("loc_16DB")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_16DB")

    QueueWorkItem2(0xFE, 2, lambda_16DB)
    Return()

    # Function_3_16B0 end

    def Function_4_16E7(): pass

    label("Function_4_16E7")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xE2E, 0x1388, 0x47CC, 0x1388, 0x0)

    def lambda_1712():

        label("loc_1712")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1712")

    QueueWorkItem2(0xFE, 2, lambda_1712)
    Return()

    # Function_4_16E7 end

    def Function_5_171E(): pass

    label("Function_5_171E")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0x8C0, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_1749():

        label("loc_1749")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1749")

    QueueWorkItem2(0xFE, 2, lambda_1749)
    Return()

    # Function_5_171E end

    def Function_6_1755(): pass

    label("Function_6_1755")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xFE6, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_1780():

        label("loc_1780")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1780")

    QueueWorkItem2(0xFE, 2, lambda_1780)
    Return()

    # Function_6_1755 end

    def Function_7_178C(): pass

    label("Function_7_178C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1795")
    Return()

    label("loc_1795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C12")
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_194E")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1982")

    label("loc_194E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1970")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1982")

    label("loc_1970")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_1982")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A4")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_19D8")

    label("loc_19A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C6")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_19D8")

    label("loc_19C6")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_19D8")

    Sleep(1500)
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
    Jump("loc_1CFA")

    label("loc_1C12")

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

    label("loc_1CFA")

    Jump("loc_1FD4")

    label("loc_1CFD")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_END)), "loc_1DDE")
    OP_CC(0x1, 0x0, "West Calmare Station")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_END)), "loc_1E05")
    OP_CC(0x1, 0x0, "Cradle Station #35")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_END)), "loc_1E2E")
    OP_CC(0x1, 0x0, "Factoria Station #7 ")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1E2E")

    OP_CC(0x1, 0x0, "Quit")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E69")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EEB")

    label("loc_1E69")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E73")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EEB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8D")
    Jump("loc_1EEB")

    label("loc_1E8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EDE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1EC7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EC4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1EC4")

    Jump("loc_1EDE")

    label("loc_1EC7")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E8D")

    label("loc_1EDE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E73")

    label("loc_1EEB")

    SetMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1F09"),
        (1, "loc_1F47"),
        (2, "loc_1F85"),
        (3, "loc_1FC3"),
        (SWITCH_DEFAULT, "loc_1FC6"),
    )


    label("loc_1F09")

    OP_A2(0x2213)
    OP_A2(0x2214)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1F1C():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F1C)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FC6")

    label("loc_1F47")

    OP_A2(0x2213)
    OP_A2(0x2215)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1F5A():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F5A)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FC6")

    label("loc_1F85")

    OP_A2(0x2213)
    OP_A2(0x2216)
    OP_43(0x101, 0x1, 0x0, 0x8)

    def lambda_1F98():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F98)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FC6")

    label("loc_1FC3")

    Jump("loc_1FC6")

    label("loc_1FC6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    EventEnd(0x0)

    label("loc_1FD4")

    Return()

    # Function_7_178C end

    def Function_8_1FD5(): pass

    label("Function_8_1FD5")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 6)), scpexpr(EXPR_END)), "loc_2081")
    OP_6F(0x1, 1100)
    OP_70(0x1, 0x514)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_204C():
        OP_6D(8300, 5000, 21350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_204C)

    def lambda_2064():
        OP_6C(12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2064)

    def lambda_2074():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2074)
    Jump("loc_20BC")

    label("loc_2081")

    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_209A():
        OP_6D(-2860, 5000, 21710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_209A)

    def lambda_20B2():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20B2)

    label("loc_20BC")

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_8_1FD5 end

    def Function_9_20CD(): pass

    label("Function_9_20CD")

    OP_8E(0xFE, 0xC08, 0x1388, 0x4A56, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x13F6, 0x4F6A, 0x7D0, 0x0)

    def lambda_20FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_20FB)
    OP_8E(0xFE, 0xC1C, 0x13F6, 0x5E9C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_20CD end

    def Function_10_2121(): pass

    label("Function_10_2121")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 0)), scpexpr(EXPR_END)), "loc_222A")
    OP_6D(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_2215():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2215)
    Jump("loc_22A2")

    label("loc_222A")

    OP_6D(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_2280():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2280)

    def lambda_2298():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2298)

    label("loc_22A2")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7E")
    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_22FE():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22FE)

    def lambda_2316():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2316)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253D")

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
    Jump("loc_26DE")

    label("loc_253D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_256E")

    ChrTalk(    #41
        0x107,
        "#067FHeehee! It is, sorta.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DE")

    label("loc_256E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A6")

    ChrTalk(    #42
        0x105,
        "#1168FHaha. It is, unfortunately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DE")

    label("loc_25A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E0")

    ChrTalk(    #43
        0x103,
        "#021FAhh, the perils of technology.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DE")

    label("loc_25E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2617")

    ChrTalk(    #44
        0x109,
        "#1061FHaha! Yeah, unfortunately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DE")

    label("loc_2617")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_264E")

    ChrTalk(    #45
        0x104,
        "#031FHaha! Lamentable, but true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DE")

    label("loc_264E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2681")

    ChrTalk(    #46
        0x10F,
        "#171FHah... I suppose it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DE")

    label("loc_2681")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B6")

    ChrTalk(    #47
        0x108,
        "#071FHaha! Unfortunately, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DE")

    label("loc_26B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26DE")

    ChrTalk(    #48
        0x106,
        "#051FHeh, I suppose.\x02",
    )

    CloseMessageWindow()

    label("loc_26DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_279F")

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
    Jump("loc_2D78")

    label("loc_279F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2844")

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
    Jump("loc_2D78")

    label("loc_2844")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28D4")

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
    Jump("loc_2D78")

    label("loc_28D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2998")

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
    Jump("loc_2D78")

    label("loc_2998")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A5F")

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
    Jump("loc_2D78")

    label("loc_2A5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B15")

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
    Jump("loc_2D78")

    label("loc_2B15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BF2")

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
    Jump("loc_2D78")

    label("loc_2BF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CCD")

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
    Jump("loc_2D78")

    label("loc_2CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D78")

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

    label("loc_2D78")

    OP_A2(0x220F)
    Jump("loc_2DD6")

    label("loc_2D7E")

    OP_43(0x101, 0x1, 0x0, 0xB)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(800)

    def lambda_2D9C():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D9C)

    def lambda_2DB4():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2DB4)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xE)
    Sleep(500)

    label("loc_2DD6")

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

    # Function_10_2121 end

    def Function_11_2E88(): pass

    label("Function_11_2E88")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2E9E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E9E)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xECE, 0x1388, 0x4376, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_11_2E88 end

    def Function_12_2EDF(): pass

    label("Function_12_2EDF")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2EF5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EF5)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9F6, 0x1388, 0x4362, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_2EDF end

    def Function_13_2F31(): pass

    label("Function_13_2F31")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F47():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F47)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1086, 0x1388, 0x4808, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_13_2F31 end

    def Function_14_2F83(): pass

    label("Function_14_2F83")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F99():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F99)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7B2, 0x1388, 0x47A4, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_14_2F83 end

    def Function_15_2FD5(): pass

    label("Function_15_2FD5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FFA")
    Call(0, 18)
    Call(0, 19)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2FFA")

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
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #58
        (
            "\x07\x05#1SHalo Rail, Axis Pillar Station\x01",
            "The Halo Rail system is currently operating at limited\x01",
            "capacity. We apologize for the inconvenience.\x01",
            "Please select a service from this terminal.\x01\x01",
            "- Liber Ark Transit Authority\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3175")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D7F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        20,
        100,
        0,
        (
            "Axis Pillar Information\x01",            # 0
            "Halo Rail Service Information\x01",      # 1
            "Online Shop\x01",                        # 2
            "Gate Lock Release\x01",                  # 3
            "Cease Service\x01",                      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3216"),
        (1, "loc_3B43"),
        (2, "loc_3C95"),
        (3, "loc_3CD1"),
        (4, "loc_3D62"),
        (SWITCH_DEFAULT, "loc_3D6F"),
    )


    label("loc_3216")

    OP_56(0x0)

    AnonymousTalk(    #59
        (
            "\x07\x02#1SWelcome, my lovely, lovely bracers! I'm leaving this message\x01",
            "here as, knowing your pig-headedness, you will eventually\x01",
            "see it. Our little plan has entered its very last stage, and\x01",
            "the true awakening of the Shining Ring is near. I dearly\x01",
            "wish for you to see the moment...but just inviting you up\x01",
            "would be a bit droll, wouldn't you agree?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #60
        (
            "\x07\x02#1SSo let us have a bit of sport here. My co-conspirators await\x01",
            "you within the pillar. Should you manage to best them and\x01",
            "reach the pinnacle, you shall behold the Aureole's\x01",
            "resurrection. I eagerly await your arrival.\x01\x01",
            "Don't disappoint me!\x01\x01",
            "- Georg Weissmann\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #61
        (
            "\x07\x02#1SP.S. Joshua, I am so very glad to hear that you've gotten\x01",
            "together with your friends again. Don't you think\x01",
            "you're being a bit of a cad in ignoring Loewe and Renne,\x01",
            "though? I'm sure they'd love to say hello.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B40")
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #62
        0x102,
        "#1042F#1P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35B0")

    ChrTalk(    #63
        0x10F,
        "#173FThis is...\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_35B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35D7")

    ChrTalk(    #64
        0x107,
        "#065FWhat the...\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_35D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35FF")

    ChrTalk(    #65
        0x105,
        "#1163FWhat in...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_35FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_362A")

    ChrTalk(    #66
        0x109,
        "#1063FOh, seriously?\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_362A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3655")

    ChrTalk(    #67
        0x103,
        "#022FHow ridiculous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_3655")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3687")

    ChrTalk(    #68
        0x104,
        "#032FHmph. How very...cute.\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_3687")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36BC")

    ChrTalk(    #69
        0x106,
        "#057FStill screwin' with us...\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_36BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E2")

    ChrTalk(    #70
        0x108,
        "#072FWeissmann.\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_36E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_370C")

    ChrTalk(    #71
        0x10B,
        "#216FWHAT in the hell?\x02",
    )

    CloseMessageWindow()

    label("loc_370C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_374E")

    ChrTalk(    #72
        0x110,
        "#270FNot nearly as cute as he thinks he is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_374E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C7")

    ChrTalk(    #73
        0x10B,
        (
            "#212FHmph. I don't really know this Weissmann\x01",
            "character too well, but...\x02\x03",

            "...talk about bad taste.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_37C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37EF")

    ChrTalk(    #74
        0x108,
        "#072FVery...cute.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_37EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3837")

    ChrTalk(    #75
        0x106,
        "#057FTch. Son of a bitch thinks he's clever, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_3837")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B2")

    ChrTalk(    #76
        0x104,
        (
            "#035FHmm. Goodness.\x02\x03",

            "#030FI must say, Weissmann's level of poor\x01",
            "taste reaches impressive new depths.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_38B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38E3")

    ChrTalk(    #77
        0x103,
        "#022FHow very cute of him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_38E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3932")

    ChrTalk(    #78
        0x109,
        (
            "#1063FYeah, real cute there, buddy.\x01",
            "You sure are clever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_3932")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3984")

    ChrTalk(    #79
        0x105,
        (
            "#1162FAt least he's consistently horrible,\x01",
            "if nothing else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_3984")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39AD")

    ChrTalk(    #80
        0x107,
        "#065FThat's horrible!\x02",
    )

    CloseMessageWindow()

    label("loc_39AD")


    ChrTalk(    #81
        0x101,
        (
            "#1007F#2PYeah, if anyone was ever in need\x01",
            "of a butt kicking, it's him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #82
        0x101,
        "#1025F#2PJoshua, don't let him get to you, okay?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #83
        0x102,
        (
            "#1035F#1PDon't worry. I won't.\x02\x03",

            "#1040FMore importantly, we now know that all the\x01",
            "Enforcers--Loewe included--are inside.\x02\x03",

            "It's time for the biggest fight of our lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1006F#2PBring it on!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2231)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    SetMessageWindowPos(330, 78, 34, 12)

    AnonymousTalk(    #85
        "\x07\x05\x02",
    )


    label("loc_3B40")

    Jump("loc_3D7C")

    label("loc_3B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C22")
    OP_56(0x0)

    AnonymousTalk(    #86
        (
            "\x07\x05#1SHalo Rail service is currently limited.\x01",
            "Would you like to activate Emergency Operation Mode\x01",
            "for Axis Pillar Station?\x02",
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
        (0, "loc_3C00"),
        (1, "loc_3C19"),
        (SWITCH_DEFAULT, "loc_3C1F"),
    )


    label("loc_3C00")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Call(0, 2)
    Return()

    label("loc_3C19")

    OP_5F(0x1)
    Jump("loc_3C1F")

    label("loc_3C1F")

    Jump("loc_3C92")

    label("loc_3C22")

    OP_56(0x0)

    AnonymousTalk(    #87
        (
            "\x07\x05#1SHalo Rail service is currently limited.\x01",
            "Axis Pillar Station is currently in Emergency Operation\x01",
            "Mode.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C92")

    Jump("loc_3D7C")

    label("loc_3C95")

    FadeToBright(300, 0)

    AnonymousTalk(    #88
        "\x07\x05\x02",
    )

    OP_A9(0xF3)

    AnonymousTalk(    #89
        (
            "\x07\x05　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x02",
        )
    )

    FadeToDark(300, 0, 100)
    Jump("loc_3D7C")

    label("loc_3CD1")

    OP_56(0x0)

    AnonymousTalk(    #90
        (
            "\x07\x05#1SSubstratum Route 246 is already open.\x01",
            "The opposite gate is an evacuation route to Calmare,\x01",
            "reserved for use in extreme emergencies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D7C")

    label("loc_3D62")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D7C")

    label("loc_3D6F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D7C")

    label("loc_3D7C")

    Jump("loc_3175")

    label("loc_3D7F")

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

    # Function_15_2FD5 end

    def Function_16_3E2D(): pass

    label("Function_16_3E2D")

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

    def lambda_3ED9():
        OP_6D(-13000, -25000, 490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ED9)

    def lambda_3EF1():
        OP_67(0, 3890, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3EF1)

    def lambda_3F09():
        OP_6B(5200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F09)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3E2D end

    def Function_17_3F38(): pass

    label("Function_17_3F38")

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

    def lambda_3FDE():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FDE)

    def lambda_3FF6():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FF6)
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
    EventEnd(0x0)
    Return()

    # Function_17_3F38 end

    def Function_18_40F3(): pass

    label("Function_18_40F3")

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
        (0, "loc_416C"),
        (1, "loc_4172"),
        (SWITCH_DEFAULT, "loc_4178"),
    )


    label("loc_416C")

    OP_A2(0x1200)
    Jump("loc_4178")

    label("loc_4172")

    OP_A2(0x1201)
    Jump("loc_4178")

    label("loc_4178")

    Return()

    # Function_18_40F3 end

    def Function_19_4179(): pass

    label("Function_19_4179")

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

    # Function_19_4179 end

    def Function_20_420C(): pass

    label("Function_20_420C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #91
        "\x07\x05Platform This Way⇒ Axis Pillar Station\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_420C end

    SaveToFile()

Try(main)
