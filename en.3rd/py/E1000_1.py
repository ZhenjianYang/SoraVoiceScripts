from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E1000_1 ._SN',
        MapName             = 'Event',
        Location            = 'E1000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E1000   ._SN',
            'ED6_DT21/E1000_1 ._SN',
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
        'Campanella',                           # 9
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT26/CH20305 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT26/CH20305P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_DA",           # 00, 0
        "Function_1_F2",           # 01, 1
        "Function_2_F3",           # 02, 2
        "Function_3_240E",         # 03, 3
        "Function_4_4624",         # 04, 4
    )


    def Function_0_DA(): pass

    label("Function_0_DA")

    Event(0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_F1")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_F1")

    Return()

    # Function_0_DA end

    def Function_1_F2(): pass

    label("Function_1_F2")

    Return()

    # Function_1_F2 end

    def Function_2_F3(): pass

    label("Function_2_F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_C4(0x0, 0x800)
    Sleep(1000)
    OP_1D(0x21)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS336._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00Orbments are devices that use the orbal energy\x01",
            "contained within septium to cause a variety of\x01",
            "useful effects.\x02\x01",

            "It has only been a little over half a century since they\x01",
            "were first invented, but even in such a short time,\x01",
            "they have already revolutionized the world\x01",
            "as we know it.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x00From daily necessities, such as lighting and heating,\x01",
            "to tanks and other similar weapons used to defend our\x01",
            "nations, orbments are used in just about every facet\x01",
            "of our lives.\x02\x01",

            "In fact, it's now hard to imagine life without them--\x01",
            "so much of what we take for granted in life now\x01",
            "involves them in some way.\x02\x01",

            "And it is to proliferate and advance the development\x01",
            "of these orbments that we exist.\x02\x01",

            "We, the Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        (
            "\x07\x00Our foundation was first established in year 1155\x01",
            "of the Septian Calendar.\x02\x01",

            "That was the year after Professor Epstein's passing, and\x01",
            "was created by his brilliant-minded disciples in\x01",
            "order to honor his wishes.\x02\x01",

            "The foundation is based in his home state of Leman,\x01",
            "where it remains in operation to this day.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x00It was rather limited in size in the beginning, and its\x01",
            "attempts to spread orbal technology was initially met\x01",
            "with little success.\x02\x01",

            "Sensing that the professor's dream would never be\x01",
            "realized at the rate they were going, three key\x01",
            "researchers left Leman to try and spread the seeds\x01",
            "of orbal technology across the continent themselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        (
            "\x07\x00One of these was Professor G. Schmidt.\x02\x01",

            "The professor, who had gained a fine reputation of his\x01",
            "own for his skill in the field of mechanical engineering,\x01",
            "went around and visited corporations in various nations\x01",
            "to persuade them of the benefits of orbments.\x02\x03",

            "The second was Professor L. Hamilton.\x02\x01",

            "Mindful of the technological gap between regions,\x01",
            "he long believed it was rural and remote areas that\x01",
            "needed orbment technology more than any other. \x02\x01",

            "As such, he enlisted the help of the Bracer Guild,\x01",
            "which already had a close relationship with the\x01",
            "foundation, and formed a mission with the intent\x01",
            "of promoting and spreading the technology where\x01",
            "applicable.\x02\x01",

            "The professor himself also toured the regions with\x01",
            "the aim of spreading public awareness and laying\x01",
            "foundations for others to build on in the future. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #5
        (
            "\x07\x00The third was Professor A. Russell, now known far\x01",
            "and wide as the 'father of the Orbal Revolution.'\x02\x03",

            "Professor Russell returned to his home nation of\x01",
            "Liberl and continued to work tirelessly to advance\x01",
            "orbment technology there...\x02\x01",

            "and within a year of returning, he had set up the\x01",
            "Zeiss Engineering Factory (now known as Zeiss\x01",
            "Central Factory/ZCF) and created the first orbment\x01",
            "to be made outside Leman State.\x02\x01",

            "Three years later, the reigning king of Liberl at the\x01",
            "time, Edgar III, visited the factory to inspect it,\x01",
            "and he decided to donate a large amount of money to\x01",
            "further its research.\x02\x01",

            "With His Majesty's endorsement, orbments began to\x01",
            "spread like wildfire throughout the kingdom, bringing\x01",
            "such prosperity that the people of other nations were\x01",
            "filled with envy.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #6
        (
            "\x07\x00Up until then, most people didn't see orbments in a\x01",
            "particularly positive light, but their success in Liberl\x01",
            "changed those impressions virtually overnight.\x02\x01",

            "One nation after another began to reach out to our\x01",
            "foundation to share orbment technology, and both\x01",
            "our foundation's financial and social standing became\x01",
            "that much more secure.\x02\x01",

            "In the eyes of the world, the Orbal Revolution was a\x01",
            "sudden, far-reaching transformation...\x02\x01",

            "but it was only because of years of reaching out to\x01",
            "people and diligent, largely-unnoticed research that\x01",
            "it was able to happen at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS337._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(3500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        (
            "\x07\x00The foundation's activities center around the\x01",
            "following three guiding principles:\x02\x01",

            "1. Carrying out fundamental research on orbments.\x02\x01",

            "2. Spreading orbal technology and informing the\x01",
            "public of its benefits.\x02\x01",

            "3. Contributing to world peace through technology.\x02\x01",

            "Now, then, let's discuss each of these three guiding\x01",
            "principles in more depth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #8
        (
            "\x07\x00[1. Carrying out fundamental research on orbments.]\x02\x01",

            "The foundation's most important mission is, naturally,\x01",
            "the improvement and development of orbal technology.\x02\x01",

            "The fundamental principles behind how orbments work\x01",
            "need no improvement as such, but their architectures--\x01",
            "their internal structures--have been improved upon\x01",
            "countless times in the past and will surely continue to\x01",
            "be perfected by the curious mind as the years go on.\x02\x01",

            "Orbments' architecture concerns the mechanical parts\x01",
            "inside them such as the cogs and screws, and there is\x01",
            "still plenty of room for change as this new technology\x01",
            "develops.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        (
            "\x07\x00These improvements can reap great rewards, but the\x01",
            "research necessary to make them is known to be as\x01",
            "lengthy as it is expensive. As a result, companies who\x01",
            "prioritize profit over all else are less inclined to pursue\x01",
            "them.\x02\x01",

            "That makes our foundation's research all the more\x01",
            "important from a social perspective.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #10
        (
            "\x07\x00[2. Spreading orbal technology and informing the\x01",
            "public of its benefits.]\x02\x01",

            "Two other important goals of the foundation are to\x01",
            "spread orbal technology as widely as possible and\x01",
            "to educate the public on the correct way to use it.\x02\x01",

            "While orbments have become part of the daily lives\x01",
            "of most who live in advanced nations and populated\x01",
            "urban areas, the reality in remote and mountainous\x01",
            "regions is very different.\x02\x01",

            "To counter this, we have long worked to send missions\x01",
            "of engineers and bracers to these regions to try and\x01",
            "better the standard of living for these people, and will\x01",
            "continue to do so.\x02\x03",

            "We also continue to work on other ways to spread \x01",
            "awareness of orbal technology, such as working\x01",
            "closely with the Septian Church to have it added to\x01",
            "the curriculum of Sunday School classes.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #11
        (
            "\x07\x00[3. Contributing to world peace through technology.]\x02\x01",

            "\x07\x00It is to pursue this noble yet extremely difficult goal\x01",
            "that the foundation has had a close relationship with\x01",
            "the Bracer Guild ever since its initial founding.\x02\x01",

            "The guild was established as an international peace-\x01",
            "keeping organization and can mediate on conflicts\x01",
            "between nations from a neutral point of view, making\x01",
            "it essential to the stability of our world as it stands.\x02\x01",

            "The Epstein Foundation continues to back them up\x01",
            "fully in their cause, both with financial aid and using\x01",
            "the fact that Leman State is the only place where\x01",
            "tactical orbments are produced to provide them with\x01",
            "equipment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "\x07\x00Just as well, this relationship also provides ideal\x01",
            "feedback towards tweaking the quality of tactical\x01",
            "orbments as they are used in combat, too.\x02\x01",

            "Every machine and every invention goes through\x01",
            "a long, grueling process behind the scenes before \x01",
            "eventually reaching its finished, refined form, \x01",
            "and tactical orbments are no exception.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #13
        (
            "\x07\x00Then, in S1190...\x02\x01",

            "Our foundation unveiled the Orbal Network Project,\x01",
            "which will be implemented in partnership with ZCF.\x02\x01",

            "Said project aims to join all of Zemuria together with\x01",
            "a single united communications network, but our hope\x01",
            "is that it will do much more than that.\x02\x01",

            "Our hope is that it will help to realize a peaceful world\x01",
            "through communication.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #14
        (
            "\x07\x00Sadly, orbments' relationship with peace as a\x01",
            "concept has become somewhat complicated.\x02\x01",

            "Are they aiding in its realization, or are they doing the exact\x01",
            "opposite? Professor Epstein expressed his hopes that\x01",
            "their ability to realize the limitless looping of energy\x01",
            "would be able to bring lasting peace to the world.\x02\x01",

            "Instead, recent years have thoroughly betrayed\x01",
            "those hopes, and the post-revolution world has\x01",
            "been a chaotic one indeed.\x02\x01",

            "The conflict between Liberl and Erebonia, for one,\x01",
            "made significant use of orbal weaponry--airships\x01",
            "included.\x02\x01",

            "It seems beyond a doubt that orbal weaponry will\x01",
            "continue to become more and more advanced,\x01",
            "making war an even more tragic event than ever.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        (
            "\x07\x00In the face of all of this, how should we go about\x01",
            "trying to create a peaceful world?\x02\x01",

            "We believe the best way to do this is to rely on the\x01",
            "power of communication and a means to do so with\x01",
            "people of different nationalities and races.\x02\x01",

            "If these people can more easily interact and more\x01",
            "easily deepen their understanding of one another,\x01",
            "perhaps that will allow us to create the world we all\x01",
            "so dearly desire.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x00In the end, one thing is for certain: our challenges\x01",
            "to try and realize Professor Epstein's ideals are only\x01",
            "just beginning.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x20000000)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_59()
    OP_20(0x7D0)
    OP_21()
    OP_C7(0x1, 0xFF, 0x0)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_F7(0x9, 0x7, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00Side Story [The Epstein Foundation] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2401")
    Sleep(1000)
    OP_28(0x15, 0x4, 0x10)
    OP_28(0x15, 0x4, 0x20)
    OP_3E(0x2EC, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Received \x1F\xEC\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(7000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #19
        "\x07\x05Received \x07\x027,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2401")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_F3 end

    def Function_3_240E(): pass

    label("Function_3_240E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_C4(0x0, 0x800)
    Sleep(1500)
    OP_1D(0x38)
    Sleep(1500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS340._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(2500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #20
        (
            "\x07\x00#80W[Report on the Attack on Erebonia's Bracer Guilds]\x02\x01",

            "　\x01",
            "　\x01\x01",
            "　#20W\x01",
            "In S1202, many of the branches of the Bracer Guild\x01",
            "in Erebonia came under attack in quick succession.\x02\x01",

            "　\x01",
            "The perpetrators were an armed group, but all else\x01",
            "about them was unknown, \x02",

            "and the guild along with\x01",
            "all connected to it in the nation fell into a state of\x01",
            "confusion.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #21
        (
            "\x07\x00Before long, the orbal communications network in\x01",
            "the capital was rife with calls and messages...\x02\x01",

            "and the situation grew increasingly grave.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0xC3, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #22
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x02\x01",

            "[At dawn yesterday, the capital's guildhouses were\x01",
            "completely destroyed by powerful explosives.\x02\x01",

            "According to the 2nd subdivision's analysis,\x01",
            "the explosives were likely set directly below those\x01",
            "buildings in the city's underground waterways.\x02\x01",

            "Judging by explosives used and means employed,\x01",
            "this was the work of professionals.\x02\x01",

            "Currently working to confirm the locations of\x01",
            "potentially dangerous persons within the country.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 240, -1, -1)

    AnonymousTalk(    #23
        (
            "\x07\x0C[From: Intelligence Division, 3rd Subdivision]\x01",
            "[To: Intelligence Division, 1st Subdivision]\x02\x01",

            "[A jaeger member has been found among those\x01",
            "suspected of entering the country illegally.\x02\x01",

            "Confirmed to be responsible for logistics in\x01",
            "the Jester jaeger corps. \x02",

            "Keep an eye on other\x01",
            "members of the same corps in the country.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(420, 20, -1, -1)

    AnonymousTalk(    #24
        (
            "\x07\x04[From: Erebonian Bracer Guild]\x01",
            "[To: Liberlian Bracer Guild, Grancel Branch]\x01\x02",

            "[At dawn today, the guildhouses in Heimdallr\x01",
            "came under attack.\x02\x01",

            "We are unable to contact the bracers\x01",
            "charged with overseeing them.\x02\x01",

            "We request the aid of high-ranking bracers.\x01",
            "This is urgent. We repeat: this is urgent.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(420, 240, -1, -1)

    AnonymousTalk(    #25
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x01\x02",

            "[The Bracer Guild here in Erebonia has sent a\x01",
            "message to the guild's Grancel branch.\x02\x01",

            "Judging by the content of the message, at least\x01",
            "one high-ranking bracer will be entering Erebonia\x01",
            "in the coming days.\x02\x01",

            "We request they be pursued and put under strict\x01",
            "surveillance upon arrival.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS341._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #26
        (
            "\x07\x00Two days after the assaults began, Cassius Bright\x01",
            "(S-rank) arrived in the Imperial capital.\x02\x01",

            "He assumed the post of provisional representative\x01",
            "of the Erebonian guild.\x02\x01",

            "After doing so, he assessed the damage to the guilds\x01",
            "and called for the bracers assigned to them, who had\x01",
            "become scattered in the chaos, to reconvene outside\x01",
            "the city.\x02\x01",

            "He also ordered a halt to all orbal communications\x01",
            "to prevent interception by the enemy.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #27
        (
            "\x07\x00By this point, guilds in six cities had been attacked,\x01",
            "and the Bracer Guild in Erebonia was beginning to\x01",
            "struggle to function.\x02\x01",

            "The branches that had not yet been attacked\x01",
            "requested the army's protection...\x02\x01",

            "However, they seemed to be in no hurry to grant \x01",
            "their support, making it clear that they could not\x01",
            "be counted upon.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #28
        (
            "\x07\x00Meanwhile, the provisional representative was able\x01",
            "to estimate the rough location of the enemy supply\x01",
            "base from their movements up to that point...\x02\x01",

            "and after choosing a small number of bracers who\x01",
            "were familiar with the area, he sent them to try and\x01",
            "find it.\x02\x01",

            "His reasoning for going with this approach was that\x01",
            "he had concluded the enemy would have to build a\x01",
            "supply base inside the country because of how strict\x01",
            "Erebonia's border controls are.\x02\x01",

            "It did not take long for his 'lose the battle, but win\x01",
            "the war' strategy to produce results.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #29
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x02\x01",

            "[The bracer sent by Liberl's guild is confirmed to be\x01",
            "one Cassius Bright.\x02\x01",

            "Bright is an S-rank bracer \x02",

            "whose file in our subdivision\x01",
            "has him rated as a L4 threat, the second-highest level\x01",
            "possible.\x02\x01",

            "He is also the man believed to have commanded the\x01",
            "counteroffensive against the Imperial Army during\x01",
            "the Hundred Days War.\x02\x01",

            "May potentially pose a threat to national security,\x02\x01",

            "so he is being carefully watched.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    Sleep(1000)
    SetMessageWindowPos(20, 240, -1, -1)

    AnonymousTalk(    #30
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x02\x01",

            "[Attempt to track CB failed.\x02\x01",

            "Current whereabouts are unknown.\x02\x01",

            "However, as requested by HQ, we have not raised\x01",
            "the alert level and have left it at it stands.\x02\x01",

            "Several bracers are currently traveling aboard\x01",
            "a train. \x02",

            "We believe them to be taking part in\x01",
            "some kind of operation.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #31
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x02\x01",

            "[Six bracers assaulted the jaegers' base.\x02\x01",

            "The jaegers inside the base were apprehended.\x02\x01",

            "We have identified them to be members of the\x01",
            "Jester jaeger corps.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS342._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #32
        (
            "\x07\x00The discovery of the enemy's base revealed that it\x01",
            "was a jaeger corps known as Jester who was behind\x01",
            "the attacks.\x02\x01",

            "After this, however, the jaegers' movements became\x01",
            "much more passive, and the two sides entered a \x01",
            "deadlock.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
        (
            "\x07\x00The stalemate continued for roughly two months.\x02\x01",

            "During this time, the guild representative made\x01",
            "contact with the Intelligence Division...\x02\x01",

            "and began preparing for an operation that would\x01",
            "ultimately allow him to bring the trouble to an end.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #34
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x02\x01",

            "[CB has made contact with a member of our subdivision.\x02",

            "Currently in the process of confirming...]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 240, -1, -1)

    AnonymousTalk(    #35
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x02\x01",

            "[The target, CB, has proposed a joint operation.\x02",

            "Intending to meet him again at the specified date and time.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS343._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #36
        (
            "\x07\x00--Strategic Analysis of the Bracer Guild Attack--\x02\x01",

            "         Intelligence Division, 2nd Subdivision\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #37
        (
            "\x07\x00What eventually broke the deadlock was a brilliant\x01",
            "strategy devised by CB.\x02\x01",

            "Having successfully made contact with a member\x01",
            "of the Intelligence Division, he made them send a\x01",
            "message to HQ in the hopes it would be intercepted\x01",
            "by the enemy.\x02\x01",

            "What happened was exactly that; from the message,\x01",
            "they were able to deduce the time and place the next\x01",
            "meeting would be happen, and set about plotting his\x01",
            "assassination.\x02\x01",

            "...Exactly what CB hoped would happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #38
        (
            "\x07\x00During the meeting, CB had also given said \x01",
            "Intelligence Division member an encoded message...\x02\x01",

            "It contained detailed plans for an operation in \x01",
            "which the Imperial Army would defeat the jaegers\x01",
            "after they had been lured out by false information.\x02\x01",

            "The general staff office chose to go ahead with\x01",
            "the proposed plan, \x02",

            "and after a joint operation\x01",
            "with the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #39
        (
            "\x07\x00...the jaegers, who had gathered to assassinate CB,\x01",
            "were surrounded and forced to surrender.\x02\x01",

            "Furthermore, the remnants of their forces who were\x01",
            "in other bases were also defeated after the initial\x01",
            "prisoners gave up their locations.\x02\x01",

            "Several months after the trouble began, Jester was\x01",
            "completely dismantled.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_20(0x9C4)
    OP_21()
    Sleep(1000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #40
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x01",
            "[Raising the threat level of Cassius Bright\x01",
            "(S-rank bracer), effectively immediately.\x02\x01",

            "Henceforth, he will be regarded as a L5 threat.\x02\x01",

            "He poses a severe threat to national security\x02\x01",

            "and must be placed under strict surveillance if\x01",
            "he ever enters the country again.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(420, 240, -1, -1)

    AnonymousTalk(    #41
        (
            "\x07\x0C[From: Intelligence Division, 1st Subdivision]\x01",
            "[To: General Staff Office]\x01",
            "[Confirmed that the surveillance target left the\x01",
            "country today.\x02",

            "His departure was without incident.\x02\x01",

            "Handing control over the mission over to our\x01",
            "foreign agencies.\x02",

            "Transmission over.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05[From: GSO Special Investigative Department]\x01",
            "[To: His Excellency the Imperial Chancellor]\x01",
            "[We have also confirmed CB's departure.\x02\x01",

            "We shall continue to pursue him, but he has not\x01",
            "shown any suspicious behaviors to date.\x02\x01",

            "We have yet to confirm any interactions between\x01",
            "him and the minstrel. \x02",

            "Will continue to follow\x01",
            "their movements.]\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x20000000)
    OP_C4(0x1, 0x800)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(2000)
    Sleep(1000)
    OP_F7(0x9, 0xD, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #43
        "\x07\x00Side Story [Assault on the Imperial Guilds] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4617")
    Sleep(1000)
    OP_28(0x16, 0x4, 0x10)
    OP_28(0x16, 0x4, 0x20)
    OP_3E(0x61E, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05Received \x1F\x1E\x06\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #45
        "\x07\x05Received \x07\x0210,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_4617")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5404   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_3_240E end

    def Function_4_4624(): pass

    label("Function_4_4624")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    Sleep(2000)
    OP_22(0x9C, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #46
        "\x07\x05Loading#200W　>　>　>　>　>　#20WComplete\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_1D(0x3D)
    Sleep(1500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS344._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_22(0x9D, 0x0, 0x64)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x9C, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #47
        (
            "\x07\x00Gordias-Class Tactical Archaism Development Plan\x01",
            "Author: Thirteen Factories\x02\x03",

            "Codename: Pater-Mater\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        80,
        280,
        0,
        "Plan Overview\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #48
        (
            "\x07\x00We intend to develop a cutting-edge archaism that inherits the DNA of the\x01",
            "rest of the Gordias series while containing a more advanced control system.\x02\x03",

            "It will retain the same tactical effectiveness that was the primary development\x01",
            "goal in previous models while allowing for more flexible and precise strategic\x01",
            "usage as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        2,
        210,
        280,
        0,
        "Effective Radius\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #49
        (
            "\x07\x00The archaism is intended to be accessible across the whole continent.\x02\x03",

            "Powerful main and sub engines should allow it to operate for several years\x01",
            "without resupplying.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        3,
        340,
        280,
        0,
        "Autonomous Combat Ability\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #50
        (
            "\x07\x00The use of the Mars integrated orbal arithmetic logic unit will allow for\x01",
            "advanced autonomous combat and effective identifying of targets.\x02\x03",

            "In addition, the archaism's control system will make use of the operator's\x01",
            "nervous system, allowing for reflexive, instinctive movements in combat.\x02\x03",

            "The operator will communicate with the archaism without being in physical\x01",
            "contact with it. This will require a compatible candidate to be found and\x01",
            "chosen.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x3)
    Sleep(400)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x2)
    Sleep(400)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x1)
    Sleep(400)
    Sleep(400)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        80,
        280,
        0,
        "Dimensions\x01",
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS345._CH")
    OP_22(0x9D, 0x0, 0x64)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        30,
        280,
        0,
        "Height/Weight\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(220, 290, 48, 4)

    AnonymousTalk(    #51
        (
            "\x07\x00Overall Height: 15.5 arge\x02\x01",

            "Unit Weight: 55 torim\x01",
            "(68 torim when fully armed)\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        2,
        30,
        340,
        0,
        "Armaments\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #52
        (
            "\x07\x00The archaism's primary weaponry will be its orbal energy cannons,\x01",
            "but it will have other kinds of orbal weaponry and even several\x01",
            "gunpowder-powered weapons as backup.\x02\x03",

            "It will also have a Revival System, which will use an orbment to\x01",
            "generate healing energy to heal or revive its operator in times of\x01",
            "danger.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        3,
        30,
        400,
        0,
        "Armor Material\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #53
        (
            "\x07\x00The armor plating will be made using kurdalegon alloy.\x02\x03",

            "Kurdalegon is the most fitting material to use, given that it is the\x01",
            "most capable we have access to in all regards.\x02\x03",

            "For data regarding strength, see files on Gospel Plan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x3)
    Sleep(400)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x2)
    Sleep(400)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(400)
    Sleep(400)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        30,
        280,
        0,
        "Current Progress\x01",
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1500)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        260,
        310,
        0,
        "New Engines\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(310, 360, -1, -1)

    AnonymousTalk(    #54
        (
            "\x07\x00Development is proceeding smoothly in line with the\x01",
            "plans drawn up by Professor Novartis.\x02\x03",

            "Tests have also confirmed that they are already\x01",
            "capable of providing power to the actuators.\x02\x03",

            "However, the professor has raised concerns about the\x01",
            "low responsiveness of the flight engine.\x01",
            "(This is especially true for the anti-gravity generator.)\x02\x03",

            "He concluded that the engine as it stands cannot be\x01",
            "put into actual use. The possibility of using boosters\x01",
            "to provide additional propulsion is under consideration.\x02",
        )
    )

    CloseMessageWindow()
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        40,
        255,
        0,
        "Actuators\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(120, 295, -1, -1)

    AnonymousTalk(    #55
        (
            "\x07\x00Development of the actuators is experiencing\x01",
            "significant difficulty, as it isn't possible to simply\x01",
            "use the same ones as other archaisms.\x02\x03",

            "The increased size of the main weaponry means\x01",
            "the archaism's weight during combat is significant,\x01",
            "and as a result, problems have been occurring in\x01",
            "durability tests, especially with the leg joints.\x02\x03",

            "It may be possible to make improvements in this\x01",
            "area by using precise control so the weight burden\x01",
            "is spread evenly rather than focused on one point.\x02",
        )
    )

    CloseMessageWindow()
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        20,
        75,
        0,
        "Main Armaments\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(20, 115, -1, -1)

    AnonymousTalk(    #56
        (
            "\x07\x00The orbal energy cannons that will serve as its\x01",
            "primary armaments have been successfully tested.\x02\x03",

            "However, by order of Professor Novartis, the\x01",
            "possibility of them becoming twin mounts is\x01",
            "being analyzed, so they have yet to be equipped.\x02\x03",

            "The new orbal engines are expected to be able\x01",
            "to provide enough energy to compensate for the\x01",
            "necessary increase in output.\x02",
        )
    )

    CloseMessageWindow()
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        200,
        75,
        0,
        "Control System\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(220, 115, -1, -1)

    AnonymousTalk(    #57
        (
            "\x07\x00Experiments regarding the control system are\x01",
            "currently ongoing.\x02\x03",

            "For the results of the experiments that have been\x01",
            "carried out so far, see a separate entry.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        2,
        340,
        75,
        0,
        "Experiment Results\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    OP_5F(0x1)
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS346._CH")
    OP_22(0x9D, 0x0, 0x64)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_43(0x0, 0x0, 0x0, 0x12)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #58
        (
            "\x07\x00Tests of the control system continue to be performed.\x02\x03",

            "However, none of the test subjects have been able to realize the expected\x01",
            "level of precision we are aiming for.\x02\x03",

            "The results of the main tests conducted by Professor Novartis and his team\x01",
            "can be viewed above.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        80,
        280,
        0,
        "Test Results\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    SetMessageWindowPos(310, 40, -1, -1)

    AnonymousTalk(    #59
        (
            "\x07\x00Test Subject: Subject A1\x02\x01",

            "Abnormality during phase 2. Comatose.\x02\x01",

            "Test Subject: Subject B3\x02\x01",

            "Abnormality during phase 3. Cardiac arrest.\x02\x01",

            "Test Subject: Subject C1\x02\x01",

            "Abnormality during phase 1. Insanity.\x02\x01",

            "Test Subject: Subject D7\x02\x01",

            "Abnormality during phase 2. Comatose.\x02\x01",

            "Test Subject: Subject E3\x02\x01",

            "Abnormality during phase 2. Cardiac arrest.\x02\x03",

            "Test Subject: Subject F2\x02\x01",

            "Abnormality during phase 2. Comatose.\x02\x01",

            "Test Subject: Subject G4\x02\x01",

            "Abnormality during phase 3. Comatose.\x02\x01",

            "Test Subject: Subject H1\x02\x01",

            "Abnormality during phase 2. Comatose.\x02\x01",

            "Test Subject: Subject I6\x02\x01",

            "Abnormality during phase 4. Mental breakdown.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #60
        (
            "\x07\x00As can be seen, all of the test subjects failed to adapt to the control system.\x02\x03",

            "Nonetheless, the society continues to supply test subjects, and we intend to\x01",
            "keep performing further experiments.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        80,
        280,
        0,
        "Future Development\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #61
        (
            "\x07\x00We have received word from the society that development is to be\x01",
            "temporarily frozen.\x02\x03",

            "Their reasoning is that the stability of the control system is in question.\x02\x03",

            "From now on, only test subjects carefully chosen by the society will be taking\x01",
            "part in connection tests.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xBB8)
    OP_21()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS347._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_22(0x9C, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #62
        (
            "\x07\x05Test Subject: Subject R3\x02\x01",

            "Successfully completed all four testing phases.\x02\x01",

            "Note: the subject did experience a small degree of flashbacks.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)

    AnonymousTalk(    #63
        (
            "\x07\x05Test Subject: Subject R3\x02\x01",

            "Succeeded in communicating with Pater-Mater.\x02\x03",

            "Ascertaining the society's intentions in regards to resuming development...\x01",
            "Subject R3 has succeeded in operating Pater-Mater.\x02\x03",

            "Ascertaining the society's intentions in regards to resuming development...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x20000000)
    OP_C6(0x0, 0x3, 16777215, 2500, 0)
    Sleep(3000)
    Sleep(1500)
    OP_E3(0x1, 0x0)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_F7(0x9, 0xA, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #64
        "\x07\x00Side Story [Gordias-Class Experiment Report] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6105")
    Sleep(1000)
    OP_28(0x17, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #65
        "\x07\x05Received \x07\x0210,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_6105")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5612   ._SN", 130, 0, 0)
    IdleLoop()
    Return()

    # Function_4_4624 end

    SaveToFile()

Try(main)
